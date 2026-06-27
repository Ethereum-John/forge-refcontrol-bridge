# Install And Update

## Install With Git

From your Forge/ForgeNeo root folder:

```powershell
git clone https://github.com/YOUR-USERNAME/forge-refcontrol-bridge.git extensions\forge-refcontrol-bridge
```

Restart Forge/ForgeNeo.

## Manual Install

Download the repository ZIP from GitHub, extract it, and place the extracted
folder here:

```text
extensions/forge-refcontrol-bridge
```

The final structure should look like:

```text
extensions/
  forge-refcontrol-bridge/
    README.md
    REFCONTROL_KLEIN_GUIDE.md
    scripts/
      refcontrol_bridge.py
```

Restart Forge/ForgeNeo.

## Update

If installed with Git:

```powershell
cd extensions\forge-refcontrol-bridge
git pull
```

Then restart Forge/ForgeNeo.

## Remove

Delete:

```text
extensions/forge-refcontrol-bridge
```

No Forge core files are modified by this extension.

