"""Bridge ControlNet generated previews into ImageStitch Integrated.

The extension listens for Forge's ControlNet generated-preview canvases and the
ImageStitch Integrated reference gallery, then adds small transfer buttons that
copy the preview image into the gallery.
"""

import base64
from io import BytesIO

import gradio as gr
import numpy as np
from PIL import Image

from modules import scripts, shared
from modules.ui_components import InputAccordion


IMAGESTITCH_GALLERY_ID = "script_{tab}_imagestitch_integrated_ref_latent"
CONTROLNET_PREVIEW_PREFIX = "{tab}_controlnet_ControlNet-"
CONTROLNET_PREVIEW_SUFFIX = "_generated_image"
FORGE_CANVAS_BACKGROUND_CLASS = "logical_image_background"


class RefControlBridge(scripts.Script):
    sorting_priority = 560
    _components = {
        "txt2img": {"gallery": None, "previews": {}},
        "img2img": {"gallery": None, "previews": {}},
    }
    _pending_preview = None

    def title(self):
        return "RefControl Bridge"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def after_component(self, component, **_kwargs):
        elem_id = getattr(component, "elem_id", None)
        if not elem_id:
            return

        for tab in ("txt2img", "img2img"):
            if elem_id == IMAGESTITCH_GALLERY_ID.format(tab=tab):
                self._components[tab]["gallery"] = component
                return

            prefix = CONTROLNET_PREVIEW_PREFIX.format(tab=tab)
            suffix = CONTROLNET_PREVIEW_SUFFIX
            if elem_id.startswith(prefix) and elem_id.endswith(suffix):
                unit_text = elem_id[len(prefix) : -len(suffix)]
                try:
                    unit_index = int(unit_text)
                except ValueError:
                    return
                self._pending_preview = {"tab": tab, "unit": unit_index}
                return

        if self._pending_preview is None:
            return

        elem_classes = getattr(component, "elem_classes", None) or []
        if FORGE_CANVAS_BACKGROUND_CLASS not in elem_classes:
            return

        tab = self._pending_preview["tab"]
        unit = self._pending_preview["unit"]
        self._components[tab]["previews"][unit] = component
        self._pending_preview = None

    def ui(self, is_img2img):
        tab = "img2img" if is_img2img else "txt2img"
        components = self._components[tab]
        gallery = components.get("gallery")
        previews = components.get("previews") or {}

        with InputAccordion(False, label=self.title()):
            gr.Markdown(
                "Send a ControlNet preprocessor preview into ImageStitch Integrated. "
                "Run the ControlNet preview first, then use one of these buttons."
            )
            status = gr.Textbox(label="Status", value="", interactive=False, max_lines=2)

            if gallery is None:
                gr.Markdown("ImageStitch Integrated was not found on this tab.")
            elif not previews:
                gr.Markdown("No ControlNet preview canvases were found on this tab.")
            else:
                max_units = int(shared.opts.data.get("control_net_unit_count", 3) or 3)
                for unit_index in sorted(previews):
                    if unit_index >= max_units:
                        continue

                    preview = previews[unit_index]
                    label = f"Unit {unit_index + 1}"
                    with gr.Row():
                        append_btn = gr.Button(f"Append {label} Preview")
                        insert_btn = gr.Button(f"Insert {label} as Image 1")

                    append_btn.click(
                        fn=self._make_handler(label, mode="append"),
                        inputs=[gallery, preview],
                        outputs=[gallery, status],
                        queue=False,
                        show_progress=False,
                    )
                    insert_btn.click(
                        fn=self._make_handler(label, mode="insert_first"),
                        inputs=[gallery, preview],
                        outputs=[gallery, status],
                        queue=False,
                        show_progress=False,
                    )

            gr.Markdown(
                "For RefControl, ImageStitch image 1 should be the control map and "
                "image 2 should be the visual reference."
            )

        return []

    @classmethod
    def _make_handler(cls, label, mode):
        def handler(gallery, preview):
            return cls._transfer_preview(gallery, preview, label, mode)

        return handler

    @staticmethod
    def _transfer_preview(gallery, preview, label, mode):
        image = RefControlBridge._to_pil(preview)
        if image is None:
            return gr.skip(), f"{label}: no preview image found. Run the ControlNet preview first."

        gallery_items = RefControlBridge._normalize_gallery(gallery)
        item = (image, None)

        if mode == "insert_first":
            gallery_items.insert(0, item)
            action = "inserted as Image 1"
        else:
            gallery_items.append(item)
            action = f"appended as Image {len(gallery_items)}"

        return gr.update(value=gallery_items), f"{label}: preview {action} in ImageStitch."

    @staticmethod
    def _normalize_gallery(gallery):
        if not gallery:
            return []

        normalized = []
        for item in gallery:
            if isinstance(item, tuple):
                normalized.append(item)
            else:
                normalized.append((item, None))
        return normalized

    @staticmethod
    def _to_pil(value):
        if value is None:
            return None

        if isinstance(value, Image.Image):
            return value.convert("RGB")

        if isinstance(value, np.ndarray):
            array = value
            if array.dtype != np.uint8:
                if array.max() <= 1.0:
                    array = array * 255.0
                array = np.clip(array, 0, 255).astype(np.uint8)
            if array.ndim == 2:
                return Image.fromarray(array, mode="L").convert("RGB")
            if array.ndim == 3:
                return Image.fromarray(array).convert("RGB")
            return None

        if isinstance(value, str) and value.startswith("data:image"):
            try:
                payload = value.split(",", 1)[1]
                return Image.open(BytesIO(base64.b64decode(payload))).convert("RGB")
            except Exception:
                return None

        return None
