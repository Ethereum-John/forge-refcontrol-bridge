# Forge RefControl Bridge

Forge RefControl Bridge is a small Forge/ForgeNeo extension that sends a
ControlNet preprocessor preview into ImageStitch Integrated.

It is designed for workflows where ControlNet is useful as a map maker, but the
final generation is driven by ImageStitch references and a RefControl LoRA.

```text
ControlNet preprocessor preview -> RefControl Bridge -> ImageStitch Integrated
```

## What It Does

- Copies the current ControlNet generated preview into ImageStitch Integrated.
- Can append the preview to the ImageStitch gallery.
- Can insert the preview as ImageStitch image 1.
- Works on both txt2img and img2img tabs.
- Does not modify Forge, ControlNet, or ImageStitch source files.
- Adds no Python package dependencies.

## Intended Workflow

```text
ImageStitch image 1 = control map
ImageStitch image 2 = visual reference
prompt = RefControl LoRA token + trigger + generation prompt
```

For example, with a pose RefControl LoRA:

```text
pose source -> OpenPose/DWPose preview -> ImageStitch Image 1
character reference --------------------> ImageStitch Image 2
```

The detailed Klein RefControl LoRA workflows are in
[REFCONTROL_KLEIN_GUIDE.md](REFCONTROL_KLEIN_GUIDE.md).

## Requirements

- Forge/ForgeNeo-style WebUI
- Built-in or installed ControlNet extension with preprocessor previews
- ImageStitch Integrated
- A compatible model and LoRA workflow, such as FLUX.2 Klein RefControl LoRAs

This extension does not include model files, LoRA files, or ControlNet
preprocessors.

## Installation

From your Forge/ForgeNeo root folder:

```powershell
cd D:\StableDiffusion\ForgeNeo1
git clone https://github.com/YOUR-USERNAME/forge-refcontrol-bridge.git extensions\forge-refcontrol-bridge
```

Then restart Forge/ForgeNeo.

If you are installing manually, copy this repository folder into:

```text
extensions/forge-refcontrol-bridge
```

## Usage

1. Open Forge/ForgeNeo.
2. Open the ControlNet Integrated panel.
3. Upload the source image for the control map.
4. Choose a preprocessor such as OpenPose, Canny, Depth, Lineart, or Normal.
5. Run the ControlNet preprocessor preview.
6. Open the RefControl Bridge accordion.
7. Click `Insert Unit 1 as Image 1` or `Append Unit 1 Preview`.
8. Add the visual reference image in ImageStitch Integrated.
9. Add the matching RefControl LoRA token and trigger to the prompt.
10. Usually disable ControlNet for the final generation.

## Buttons

`Insert Unit N as Image 1`

Places the ControlNet preview at the front of the ImageStitch gallery. This is
usually the right choice for RefControl because image 1 should be the control
map.

`Append Unit N Preview`

Adds the ControlNet preview to the end of the ImageStitch gallery.

## Notes

- Run the ControlNet preview first. The bridge cannot copy a preview that does
  not exist yet.
- If ImageStitch or ControlNet is disabled or unavailable, the bridge will show
  a short status message instead of failing hard.
- The final generation normally uses ImageStitch plus the RefControl LoRA, not
  an enabled ControlNet model.

## Compatibility

This was developed against ForgeNeo with:

- ControlNet Integrated
- ImageStitch Integrated
- Python 3.13 venv
- PyTorch CUDA workflow

The bridge uses Forge/A1111-style script hooks and Gradio components, so future
Forge UI changes may require small selector updates.

## Project Status

Early public release candidate. The extension is intentionally small and focused.

Good next improvements:

- Add screenshots or a short demo GIF.
- Add compatibility reports from other Forge builds.
- Add optional presets/help text for common RefControl LoRA families.

## License

MIT. See [LICENSE](LICENSE).
