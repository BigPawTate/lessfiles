import os
import shutil
from datetime import datetime

# Prompt the user for the source directory
source_directory = input("Enter the source directory path: ")

# Check if the entered directory exists
if not os.path.exists(source_directory) or not os.path.isdir(source_directory):
    print("The specified directory does not exist.")
else:
    # Prompt the user for the increment
    try:
        increment = int(input("Enter the increment (e.g., 1 for every file, 2 for every other file): "))
    except ValueError:
        print("Invalid increment. Please enter a positive integer.")
        exit()

    if increment <= 0:
        print("Increment should be a positive integer.")
        exit()

    # Generate a timestamp in the format "20231026 113730"
    timestamp = datetime.now().strftime("%Y%m%d %H%M%S")

    # Get the base directory name from the source directory
    base_directory_name = os.path.basename(os.path.normpath(source_directory))

    # Create the destination subdirectory with original directory name and timestamp
    destination_directory = os.path.join(source_directory, f"{base_directory_name} {timestamp}")
    os.makedirs(destination_directory, exist_ok=True)

    # Get a list of all files in the source directory
    files = [f for f in os.listdir(source_directory) if os.path.isfile(os.path.join(source_directory, f))]

    # Create a list of files to copy based on the specified increment
    files_to_copy = files[::increment]

    # Copy the selected files to the destination subdirectory
    for file_name in files_to_copy:
        source_path = os.path.join(source_directory, file_name)
        destination_path = os.path.join(destination_directory, file_name)
        shutil.copy2(source_path, destination_path)

    print(f"Copied {len(files_to_copy)} files with an increment of {increment} to {destination_directory}")
