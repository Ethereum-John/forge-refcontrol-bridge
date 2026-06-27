# RefControl Klein Guide

This guide is for ForgeNeo1 with the RefControl LoRAs in:

```text
F:\Links\Lora\Klein
```

## The Pattern

```text
1. Make a control map
   [ControlNet preprocessor preview]

2. Send it into ImageStitch
   [RefControl Bridge: Append / Insert as Image 1]

3. Add the visual reference
   [ImageStitch Integrated: Append Pasted Image]

4. Prompt with LoRA + trigger
   [Klein checkpoint + ImageStitch + LoRA token]
```

Final ImageStitch order:

```text
+----------------------------+-----------------------------+
| Image 1                    | Image 2                     |
+----------------------------+-----------------------------+
| control map                | identity / style reference  |
| pose, canny, depth, etc.   | person, character, object   |
+----------------------------+-----------------------------+
```

Recommended starting weight for all RefControl LoRAs:

```text
0.8 to 1.0
```

For the final generation, usually disable the ControlNet unit after the preview
has been copied. The RefControl LoRA and ImageStitch references are doing the
control work.

## Pose

What it is for:

```text
[pose skeleton] + [reference character] -> same character in that pose
```

Illustration:

```text
pose photo -> OpenPose/DWPose preview -> ImageStitch Image 1
character/reference image ----------------> ImageStitch Image 2

Image 1 controls the body pose.
Image 2 supplies the character, outfit, identity, or style.
```

Local LoRA:

```text
F:\Links\Lora\Klein\klein_trig-apply pose from image 1 with reference from image 2-_poses.safetensors
```

Prompt token:

```text
<lora:klein_trig-apply pose from image 1 with reference from image 2-_poses:0.9>
```

Trigger phrase:

```text
apply pose from image 1 with reference from image2
```

The filename contains `image 2` with a space, but use your configured trigger
phrase above first.

Exact steps:

1. In ControlNet Unit 1, upload the source pose image.
2. Choose an OpenPose/DWPose preprocessor.
3. Click the ControlNet preview/run-preprocessor button.
4. In RefControl Bridge, click `Insert Unit 1 as Image 1`.
5. In ImageStitch Integrated, append the character/reference image.
6. Put the LoRA token and trigger phrase in the prompt.
7. Disable ControlNet for the final generation unless you are intentionally
   testing a combined setup.
8. Generate with a FLUX.2 Klein checkpoint.

Prompt skeleton:

```text
<lora:klein_trig-apply pose from image 1 with reference from image 2-_poses:0.9>
apply pose from image 1 with reference from image2, your subject and scene details
```

## Canny

What it is for:

```text
[edge map] + [reference image] -> preserve silhouette, layout, and hard edges
```

Illustration:

```text
source image -> Canny preview -> ImageStitch Image 1
style/reference image ---------> ImageStitch Image 2

Image 1 controls crisp edges and silhouette.
Image 2 supplies the look, subject, or identity.
```

Good for:

```text
objects, architecture, props, outlines, logos, strong composition
```

Local LoRA:

```text
F:\Links\Lora\Klein\klein_trig-refcontrol-_canny.safetensors
```

Prompt token:

```text
<lora:klein_trig-refcontrol-_canny:0.9>
```

Trigger word:

```text
refcontrol
```

Exact steps:

1. In ControlNet Unit 1, upload the image whose edges should guide the result.
2. Choose the `canny` preprocessor.
3. Adjust low/high thresholds if needed.
4. Click the ControlNet preview/run-preprocessor button.
5. In RefControl Bridge, click `Insert Unit 1 as Image 1`.
6. In ImageStitch Integrated, append the identity/style reference image.
7. Put the LoRA token and `refcontrol` in the prompt.
8. Disable ControlNet for the final generation unless testing.

Prompt skeleton:

```text
<lora:klein_trig-refcontrol-_canny:0.9>
refcontrol, your subject and scene details
```

## Depth

What it is for:

```text
[depth map] + [reference image] -> preserve broad 3D structure and camera depth
```

Illustration:

```text
source image -> Depth preview -> ImageStitch Image 1
style/reference image --------> ImageStitch Image 2

Image 1 controls near/far structure and volume.
Image 2 supplies the visible subject or style.
```

Good for:

```text
body volume, room layout, foreground/background separation, camera angle
```

Local LoRA:

```text
F:\Links\Lora\Klein\klein_trig-refcontrol-_depth.safetensors
```

Prompt token:

```text
<lora:klein_trig-refcontrol-_depth:0.9>
```

Trigger word:

```text
refcontrol
```

Exact steps:

1. In ControlNet Unit 1, upload the structure/depth source image.
2. Choose a depth preprocessor, such as MiDaS, Zoe, or Depth Anything if
   available.
3. Click the ControlNet preview/run-preprocessor button.
4. In RefControl Bridge, click `Insert Unit 1 as Image 1`.
5. In ImageStitch Integrated, append the identity/style reference image.
6. Put the LoRA token and `refcontrol` in the prompt.
7. Disable ControlNet for the final generation unless testing.

Prompt skeleton:

```text
<lora:klein_trig-refcontrol-_depth:0.9>
refcontrol, your subject and scene details
```

## Lineart

What it is for:

```text
[line drawing] + [reference image] -> follow drawn contours more cleanly than canny
```

Illustration:

```text
sketch/image -> Lineart preview -> ImageStitch Image 1
style/reference image ---------> ImageStitch Image 2

Image 1 controls clean drawn contours.
Image 2 supplies color, rendering style, identity, or material.
```

Good for:

```text
illustration, comics, character outlines, cleaner pose/action reads
```

Local LoRA:

```text
F:\Links\Lora\Klein\klein_trig-refcontrol-_lineart.safetensors
```

Prompt token:

```text
<lora:klein_trig-refcontrol-_lineart:0.9>
```

Trigger word:

```text
refcontrol
```

Exact steps:

1. In ControlNet Unit 1, upload the image or sketch to extract lines from.
2. Choose a lineart preprocessor.
3. Click the ControlNet preview/run-preprocessor button.
4. In RefControl Bridge, click `Insert Unit 1 as Image 1`.
5. In ImageStitch Integrated, append the identity/style reference image.
6. Put the LoRA token and `refcontrol` in the prompt.
7. Disable ControlNet for the final generation unless testing.

Prompt skeleton:

```text
<lora:klein_trig-refcontrol-_lineart:0.9>
refcontrol, your subject and scene details
```

## Normal

What it is for:

```text
[normal map] + [reference image] -> preserve surface orientation and form
```

Illustration:

```text
source image -> Normal preview -> ImageStitch Image 1
style/reference image --------> ImageStitch Image 2

Image 1 controls surface direction and form.
Image 2 supplies the subject, identity, style, or material.
```

Good for:

```text
human/body form, sculptural objects, hard-surface form, lighting-aware volume
```

Local LoRA:

```text
F:\Links\Lora\Klein\klein_trig-refcontrol-_normal.safetensors
```

Prompt token:

```text
<lora:klein_trig-refcontrol-_normal:0.9>
```

Trigger word:

```text
refcontrol
```

Exact steps:

1. In ControlNet Unit 1, upload the image whose form should guide the result.
2. Choose a normal-map preprocessor, such as `normal_bae` if available.
3. Click the ControlNet preview/run-preprocessor button.
4. In RefControl Bridge, click `Insert Unit 1 as Image 1`.
5. In ImageStitch Integrated, append the identity/style reference image.
6. Put the LoRA token and `refcontrol` in the prompt.
7. Disable ControlNet for the final generation unless testing.

Prompt skeleton:

```text
<lora:klein_trig-refcontrol-_normal:0.9>
refcontrol, your subject and scene details
```

## Practical Defaults

Start here:

```text
LoRA weight: 0.9
ImageStitch Maximum Side Length: 1024
ControlNet final generation: disabled
One RefControl LoRA at a time
```

If the result ignores the map:

```text
Increase LoRA weight toward 1.0
Make sure ImageStitch image 1 is the map
Make sure the trigger word/phrase is present
Use a cleaner control map
```

If the result copies the map too rigidly:

```text
Lower LoRA weight toward 0.75
Use a less detailed control map
Add stronger style/content language in the prompt
```

If identity drifts:

```text
Use a clearer reference image as ImageStitch image 2
Keep the pose/control map proportional to the reference
Prefer the FLUX.2 Klein Base model when available
```
