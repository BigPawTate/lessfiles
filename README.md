#  Too Many Files! 
- Make some more!
- doing photogrammetry and sometimes I have more images than the application can handle
- using this script to pare down the number of files and update the filenames to include the image's timestamp to avoid naming conflicts when combining multiple sessions
  



# Photo File Renaming and Copying Script

This Python script is designed to rename and copy picture files based on their EXIF data. It extracts the timestamp from the EXIF data and appends it to the original filename, while retaining the file extension. The script also allows you to specify an increment to choose which files to copy.

## Dependencies

Before using this script, ensure you have the following dependencies installed:

- Python 3.x
- The `exifread` library for reading EXIF data. You can install it using pip:  ```pip install exifread```


## Usage

1. Run the script by executing it using a Python 3 interpreter.

2. You will be prompted to provide the directory path where your picture files are located.

3. You will also be asked to specify an increment. For example, you can enter `1` to copy every file or `2` to copy every other file.

4. You can optionally provide an output directory. If you do not provide one, the script will create a subdirectory in the source directory with a timestamp (format: YYYYMMDD HHMMSS), where copied files will be stored.

5. If you provide an output directory, the renamed files will be placed directly in that directory. If you do not provide one, the default timestamp directory will be created as before.

6. The script will iterate through the picture files in the source directory, extract the timestamp from their EXIF data, and append it to the filename.

7. Only the files selected based on the increment will be copied to the subdirectory with the modified names.

8. The script will display the total number of files that were copied to the subdirectory.

## Example

Suppose you have a directory with picture files, and you run the script with an increment of `2`. The script will copy every other picture file and append the timestamp from their EXIF data to the filenames. If you provide an output directory, the renamed files will be placed directly in that directory.
