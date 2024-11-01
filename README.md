# GLBtoOBJ
A simple Python script that converts GLB (Binary glTF) files to OBJ files using the trimesh library.

Table of Contents


Installation
To use this script, you'll need to install the required libraries:

trimesh: A Python 3 library for working with three-dimensional meshes. You can install it via pip: pip install trimesh
Here's a step-by-step guide to installing and setting up the environment:

## Install trimesh using pip
```
pip install trimesh
```

## Clone this repository (if you haven't already)
```
git clone https://github.com/your-username/glb-to-obj-converter.git
```
## Navigate into the cloned directory
```
cd glb-to-obj-converter
```

## Run the script
python glb_to_obj.py
Usage
Running the Script
To run the script, execute the following command in your terminal or command prompt:

python glb_to_obj.py
The script will guide you through the conversion process.

##   Conversion Process
Enter filename: Enter the name of the .glb file (including the extension) that you want to convert.

File check: The script checks if the provided file exists in the current directory. If it doesn't, an error message will be displayed.

Conversion: The script loads the GLB file using trimesh.load() and exports it as an OBJ file using mesh.export(). If any errors occur during this process, they will be printed to the console.

Example Output:
Enter the filename of the .glb file (include '.glb'): my_model.glb
Converted my_model.glb to my_model.obj successfully.
