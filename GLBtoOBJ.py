import os
import trimesh
import sys

def glb_to_obj():
    """
    Convert a GLB file to OBJ format using trimesh library.
    Handles multiple meshes within the GLB file and provides error handling.
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

        # Define the output filename
        output_filename = os.path.splitext(input_filename)[0] + '.obj'
        full_output_path = os.path.join(directory, output_filename)

        # Check if output file already exists
        if os.path.exists(full_output_path):
            response = input(f"'{output_filename}' already exists. Do you want to overwrite it? (y/n): ").lower()
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
        print(f"Converting to {output_filename}...")
        combined_mesh.export(full_output_path, file_type='obj')
        
        # Verify the output file was created
        if os.path.exists(full_output_path):
            print(f"Conversion successful! File saved as '{output_filename}'")
            print(f"Output location: {full_output_path}")
        else:
            print("Error: Failed to create output file.")

    except Exception as e:
        print(f"An error occurred during the conversion:")
        print(f"Error details: {str(e)}")
        print("\nPlease make sure you have the required libraries installed:")
        print("pip install trimesh numpy")

if __name__ == "__main__":
    glb_to_obj()
