import os
import shutil

# Define the source directory where your images are located
source_directory = r"C:\Users\arjun\Desktop\dataset"

# Define the destination directory where you want to store the collected images
destination_directory = r"C:\path\to\destination\directory"

# Create the destination directory if it doesn't exist
os.makedirs(destination_directory, exist_ok=True)

# List all files in the source directory
files = os.listdir(source_directory)

# Specify the file extensions you want to collect (e.g., '.jpg', '.png')
allowed_extensions = [".jpg", ".jpeg", ".png"]

# Iterate through the files in the source directory
for file in files:
    # Check if the file has an allowed extension
    if any(file.endswith(ext) for ext in allowed_extensions):
        # Construct the source and destination file paths
        source_path = os.path.join(source_directory, file)
        destination_path = os.path.join(destination_directory, file)

        # Copy the file from the source to the destination directory
        shutil.copy(source_path, destination_path)
        print(f"Collected: {file}")

print("Data collection completed.")
