import os
import trimesh

def glb_to_obj():
# Get the directory where the script is running
directory = os.getcwd()

# Ask the user for the filename of the .glb file
input_filename = input("Enter the filename of the .glb file (include '.glb'): ")
full_input_path = os.path.join(directory, input_filename)

# Check if the file exists
if not os.path.isfile(full_input_path):
    print("File does not exist. Please check the filename and try again.")
    return

# Define the output filename
output_filename = input_filename.replace('.glb', '.obj')
full_output_path = os.path.join(directory, output_filename)

# Load the .glb file and convert it
try:
    mesh = trimesh.load(full_input_path)
    mesh.export(full_output_path, file_type='obj')
    print(f"Converted {input_filename} to {output_filename} successfully.")
except Exception as e:
    print(f"An error occurred during the conversion: {e}")

# Run the function
glb_to_obj()
