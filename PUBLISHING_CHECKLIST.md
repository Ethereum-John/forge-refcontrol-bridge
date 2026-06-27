# Publishing Checklist

Use this before making the repository public.

## Repo Decisions

- Pick the GitHub repository name.
  - Recommended: `forge-refcontrol-bridge`
- License selected: MIT.
- Decide whether to include screenshots or a demo GIF before launch.

## Suggested GitHub Description

```text
Forge/ForgeNeo extension that sends ControlNet preprocessor previews into ImageStitch Integrated for RefControl LoRA workflows.
```

## Suggested Topics

```text
stable-diffusion
forge
forgeneo
controlnet
imagestitch
flux
klein
lora
refcontrol
```

## Local Preflight

Run from a Forge/ForgeNeo root after installing the extension:

```powershell
venv\Scripts\python.exe -B -c "import importlib.util; p=r'extensions\forge-refcontrol-bridge\scripts\refcontrol_bridge.py'; spec=importlib.util.spec_from_file_location('refcontrol_bridge_smoke', p); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); print(m.RefControlBridge().title())"
```

## First Commit

```powershell
cd C:\Codex_Workspace\forge-refcontrol-bridge-public
git init
git add .
git commit -m "Initial public release"
```

## Create GitHub Repo With GitHub CLI

Replace `YOUR-USERNAME` if needed:

```powershell
gh repo create YOUR-USERNAME/forge-refcontrol-bridge --public --source . --remote origin --push
```

## Create GitHub Repo Manually

1. Create a new public GitHub repository named `forge-refcontrol-bridge`.
2. Do not initialize it with a README, license, or gitignore.
3. Run:

```powershell
cd C:\Codex_Workspace\forge-refcontrol-bridge-public
git remote add origin https://github.com/YOUR-USERNAME/forge-refcontrol-bridge.git
git branch -M main
git push -u origin main
```

## After Publishing

- Add the suggested topics in GitHub settings.
- Add screenshots or a short GIF to the README.
- Create a `v0.1.0` release.
- Test install with:

```powershell
git clone https://github.com/YOUR-USERNAME/forge-refcontrol-bridge.git extensions\forge-refcontrol-bridge
```
