
import os
import shutil

# Define file extensions and corresponding folder names
file_extensions = {
    '.exe': 'Executables',
    '.zip': 'Archives',
    '.jpg': 'Images',
    '.png': 'Images',
    '.mp4': 'Videos',
    '.mp3': 'Audio',
    '.txt': 'Text',
    '.pdf': 'Documents',
}

# Function to organize files into folders based on their types
def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1]
            if file_extension in file_extensions:
                destination_folder = file_extensions[file_extension]
                destination_path = os.path.join(folder_path, destination_folder)
                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)
                shutil.move(file_path, os.path.join(destination_path, filename))
                print(f"Moved {filename} to {destination_folder} folder")

# Function to rename files in bulk
def rename_files(folder_path, new_name_prefix):
    count = 1
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1]
            new_filename = f"{new_name_prefix}_{count}{file_extension}"
            os.rename(file_path, os.path.join(folder_path, new_filename))
            print(f"Renamed {filename} to {new_filename}")
            count += 1

# Function to clean up unused files
def cleanup_unused_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted {filename}")
