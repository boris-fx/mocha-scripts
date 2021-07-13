# Example Python Scripts for Mocha Pro

These scripts are examples of how to use the Mocha Pro Python API.

You can run them via the Script Editor or call them using the `init.py` Scripts

For more expansive details on using the Mocha Pro Python API, go to the [Mocha Python Documentation Page](https://borisfx.com/support/documentation/mocha/python/)

## Using the Python Scripts with `init.py`

To load scripts into Mocha as tools or menu items, you need to import and initalise them via `init.py`

We generate a blank `init.py` script on the first run of mocha for you to add functionality on startup.

### The `init.py` path

The default init.py path is the Imaginer Systems Scripts directory.

The mocha `init.py` script is generated per system in the following default locations:

-   **OS X:** '~/Library/Application Support/Imagineer Systems Ltd/Scripts/init.py'
-   **Windows:** 'C:\\Users\[username]\\AppData\\Roaming\\Imagineer Systems Ltd\\Scripts\\init.py'
-   **Linux:** '~/.config/Imagineer Systems Ltd/Scripts/init.py'

You can also set the environment variable 'MOCHA_INIT_SCRIPT' to control where the path of the `init.py` initialization script resides.

If the 'MOCHA_INIT_SCRIPT' environment variable points to a file, that file will be used, if it points to a directory, it will look specifically for `init.py` in that directory.
If unset, the default locations above will be used.

### Setting up `init.py`

Below we show a detailed example of using `init.py` for creating a user-entry tool to prepend a word onto the front of all selected layers.

We also list code at the end to show how to add this to the file menu in mocha and load a dialog for user entry.

Some knowledge of PySide and Qt is helpful here, but if you follow along the script you can see how the widgets are created.

Example of using the `init.py` script

```python:
from mocha import ui

mocha_widget = ui.get_widgets()
main_window = mocha_widget['MainWindow'] # Define the MainWidget UI to use as a parent

mocha_menubar = list(filter(lambda wgt: isinstance(wgt, QMenuBar), widgets))[0]
scripts_menu = mocha_menubar.addMenu('Scripts') #create a new Scripts menu option

# import example script classes

from frame_jump import FrameJump
from set_surface_to_spline import SetSurfaceToSpline
from randomise_layer_colours import RandomiseColours
from layer_prepend import LayerPrepend
from shade_layers_by_order import ShadeMattesByOrder

def frame_jump():
    dialog = FrameJump(parent=main_window) #Set parent so dialog doesn't sit behind Mocha window
    dialog.show()

def set_surface():
    surface = SetSurfaceToSpline()
    surface.set_surface_corners()

def random_colors():
    color = RandomiseColours()
    color.do_color()

def shade_mattes():
    color = ShadeMattesByOrder()
    color.do_shading()

def layer_label():
    dialog = LayerPrepend()

# add the scripts as actions to the menu

actions_dict = {
    "Frame Jump": (scripts_menu, frame_jump),
    "Surface to Spline": (scripts_menu, set_surface),
    "Randomise Matte Colors": (scripts_menu,random_colors),
    "Shade Mattes By Layer Order": (scripts_menu,shade_mattes),
    "Prepend Selected Layer Names": (scripts_menu,layer_label),
}

for key, value in list(actions_dict.items()):
    action = QAction(key, value[0])
    action.triggered.connect(value[1])
    value[0].addAction(action)
```

If you need to check Python error output after loading an `init.py` script, load the error log from the Help menu, or load mocha via the terminal.

## Rgistering a custom exporter script with `init.py`

If you have a new custom exporter and want it to appear in the Mocha export list, you need to register it inside `init.py`.

For example:

```python:
import export_mistika_tracker_points

mistika_export = export_mistika_tracker_points.MistikaExporter()
mistika_export.register()
```
Be aware that if you register a custom export with the same name as an existing export, you may get a conflict.
