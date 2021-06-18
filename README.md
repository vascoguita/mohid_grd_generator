# MOHID Grid Generator
MOHID Grid Generator is a [QGIS](https://qgis.org/) plugin for generating regular and irregular grids with the [MOHID](http://www.mohid.com/) format.

## Compile and Deploy

Use [pb_tool](https://github.com/g-sherman/plugin_build_tool) to compile and deploy the MOHID Grid Generator plugin, specifying the directory where to deploy the plugin:

```bash
pbt deploy -p PATH
```

>  **_NOTE:_**  To find the plugin path open [QGIS](https://qgis.org/):
> 1. Select `Settings` on the Menu Toolbar
> 2. Select `User profiles` -> `Open active profile folder`
> 3. Open the `python/plugins` subdirectory - that is the plugin path for QGIS.

## Activate the MOHID Grid Generator plugin

To activate the MOHID Grid Generator plugin on [QGIS](https://qgis.org/):
1. Select `Plugins` on the Menu Toolbar
2. Select `Manage and Install Plugins...`
3. Select `Installed` on the left-side menu
4. Use the `MOHID Grid Generator` checkbox to activate the MOHID Grid Generator plugin

Once activated, a new plugin button should appear in the Toolbar.