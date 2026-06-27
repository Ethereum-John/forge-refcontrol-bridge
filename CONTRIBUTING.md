# Contributing

Thanks for taking a look at Forge RefControl Bridge.

This project is intentionally small. The main goal is to keep the extension easy
to inspect, easy to remove, and friendly to upstream Forge updates.

## Development Rules

- Do not patch Forge, ControlNet, or ImageStitch core files.
- Keep changes inside this extension folder.
- Avoid new Python dependencies unless there is a strong reason.
- Prefer readable component detection over broad monkey-patching.
- Test both txt2img and img2img when changing UI behavior.

## Local Testing

From a Forge/ForgeNeo root folder:

```powershell
venv\Scripts\python.exe -B -c "import importlib.util; p=r'extensions\forge-refcontrol-bridge\scripts\refcontrol_bridge.py'; spec=importlib.util.spec_from_file_location('refcontrol_bridge_smoke', p); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); print(m.RefControlBridge().title())"
```

For a deeper Forge script discovery check, run a UI-debug script load from the
Forge/ForgeNeo root:

```powershell
venv\Scripts\python.exe -B -c "import sys; sys.argv.append('--ui-debug-mode'); from modules_forge.initialization import initialize_forge; initialize_forge(); from modules import initialize, scripts; initialize.imports(); initialize.initialize_rest(); print([d.path for d in scripts.scripts_data if 'forge-refcontrol-bridge' in d.path])"
```

## Useful Reports

When filing an issue, include:

- Forge or ForgeNeo commit/build if known
- Python version
- Whether ControlNet Integrated is present
- Whether ImageStitch Integrated is present
- Any startup traceback
- Which tab you tested: txt2img, img2img, or both

