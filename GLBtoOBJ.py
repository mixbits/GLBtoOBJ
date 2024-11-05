import os
import trimesh
from PIL import Image
import sys

def glb_to_obj():
    """
    Convert a GLB file to OBJ format using trimesh library.
    Handles multiple meshes within the GLB file and provides error handling.
    Also exports textures as PNG images if embedded in materials of the GLB file.
    """
    try:
        # Get the directory where the script is running
        directory = os.getcwd()

        # Ask the user for the filename of the .glb file
        input_filename = input("Enter the filename of the .glb file (include '.glb'): ").strip()
        
        # Validate file extension
        if not input_filename.lower().endswith('.glb'):
            print("Error: File must have .glb extension")
            return

        full_input_path = os.path.join(directory, input_filename)

        # Check if the file exists
        if not os.path.isfile(full_input_path):
            print(f"Error: File '{input_filename}' does not exist in the current directory.")
            return

        # Define default output filenames
        obj_output_filename = os.path.splitext(input_filename)[0] + '.obj'
        texture_dir = os.path.join(directory, 'textures')
        
        # Create a textures directory if it doesn't exist
        if not os.path.exists(texture_dir):
            os.makedirs(texture_dir)

        # Ask the user for output filename if not provided
        response = input(f"Enter the filename for OBJ file (default is '{obj_output_filename}'): ").strip()
        obj_output_filename = response if response else obj_output_filename

        full_obj_output_path = os.path.join(directory, obj_output_filename)

        # Check if output file already exists
        if os.path.exists(full_obj_output_path):
            response = input(f"'{obj_output_filename}' already exists. Do you want to overwrite it? (y/n): ").lower()
            if response != 'y':
                print("Conversion cancelled.")
                return

        # Load the .glb file
        print(f"Loading {input_filename}...")
        scene = trimesh.load(full_input_path, force='scene')

        # Handle both single mesh and scene with multiple meshes
        if isinstance(scene, trimesh.Scene):
            # Combine all meshes in the scene
            meshes = []
            for geometry in scene.geometry.values():
                if isinstance(geometry, trimesh.Trimesh):
                    meshes.append(geometry)
            if not meshes:
                print("Error: No valid meshes found in the GLB file.")
                return
            combined_mesh = trimesh.util.concatenate(meshes)
        else:
            combined_mesh = scene

        # Export to OBJ format
        print(f"Converting to {obj_output_filename}...")
        combined_mesh.export(full_obj_output_path, file_type='obj')
        
        # Verify the output file was created
        if os.path.exists(full_obj_output_path):
            print(f"Conversion successful! OBJ file saved as '{obj_output_filename}'")
            print(f"Output location: {full_obj_output_path}")

            # Export textures from materials
            texture_index = 0
            for mesh in scene.geometry.values():
                if hasattr(mesh, 'visual') and hasattr(mesh.visual, 'material'):
                    material = mesh.visual.material
                    if material is not None and hasattr(material, 'image'):
                        image = material.image
                        if image is not None:
                            texture_filename = f"texture_{texture_index}.png"
                            full_texture_path = os.path.join(texture_dir, texture_filename)
                            image.save(full_texture_path)
                            print(f"Texture from material {material} exported as '{texture_filename}'")
                            texture_index += 1
        else:
            print("Error: Failed to create output file.")

    except Exception as e:
        print(f"An error occurred during the conversion:")
        print(f"Error details: {str(e)}")
        print("\nPlease make sure you have the required libraries installed:")
        print("pip install trimesh numpy pillow")

if __name__ == "__main__":
    glb_to_obj()
