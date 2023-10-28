import os
import exifread
import shutil
from datetime import datetime

# Function to get the timestamp from EXIF data
def get_timestamp_from_exif(file_path):
    with open(file_path, 'rb') as f:
        tags = exifread.process_file(f, details=False)
        if 'EXIF DateTimeOriginal' in tags:
            return tags['EXIF DateTimeOriginal'].printable
        else:
            return None

# Prompt the user for the directory path
source_directory = input("Enter the directory path where your picture files are located: ")

# Check if the provided path is a valid directory
if not os.path.isdir(source_directory):
    print("Invalid directory path. Please provide a valid directory path.")
    exit()

# Prompt the user for the increment of files they want to keep
increment = int(input("Enter the increment (e.g., 1 for every file, 2 for every other file): "))

# Create a subdirectory with the current timestamp (with space between day and hour)
timestamp = datetime.now().strftime('%Y%m%d %H%M%S')
subdirectory = os.path.join(source_directory, timestamp)

if not os.path.exists(subdirectory):
    os.mkdir(subdirectory)

# Initialize a counter to keep track of the increment
counter = 0

# Initialize a counter to keep track of copied files
copied_files_count = 0

# Iterate through the files in the directory
for filename in os.listdir(source_directory):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
        file_path = os.path.join(source_directory, filename)

        # Get the timestamp from EXIF data
        timestamp = get_timestamp_from_exif(file_path)

        if timestamp:
            # Format the timestamp with a space between the day and hour
            formatted_timestamp = timestamp.replace(' ', '').replace(':', '').replace('-', '')
            formatted_timestamp = formatted_timestamp[:8] + ' ' + formatted_timestamp[8:]

            # Get the file extension
            _, file_extension = os.path.splitext(filename)

            # Check if the current file should be copied based on the increment
            if counter % increment == 0:
                # Construct the new filename with a space between the day and hour
                new_filename = f"{os.path.splitext(filename)[0]} {formatted_timestamp}{file_extension}"
                
                # Copy the file to the subdirectory and rename it
                new_file_path = os.path.join(subdirectory, new_filename)
                shutil.copy(file_path, new_file_path)

                print(f"Copied '{filename}' to '{new_filename}'")
                copied_files_count += 1

            counter += 1
        else:
            print(f"No EXIF data found for '{filename}'")

print(f"Copied {copied_files_count} files to subdirectory: {subdirectory}")
