# Useful-python-scripts
Python scripts for everyday use, created with a little bit of help from ChatGPT.

Chat GPT explenation for each script:

1. Extract rar files:

This Python script extracts all RAR files in a directory and saves the extracted files in a specified directory. The user is prompted to enter the directory where the RAR files are located, the directory where the extracted files should be saved, and the directory where the extracted RAR files should be moved to after extraction. Default directories can also be defined in the script file. The extracted files are stored in a subfolder named after the RAR file. Once the extraction is complete, the RAR files are moved to the specified directory.

2. leveonlyPNGJPGFiles:

The script prompts the user to enter a directory path from which all files except PNG and JPG files will be deleted. If the user enters an empty path, a default directory is used. The script then walks through the directory and its subdirectories and deletes all files that don't have a PNG or JPG extension. Finally, it prints out the path of each file that was deleted.

3. Indexing Image:

The script imports the "os" module for managing files and directories and defines the "run()" function. The function prompts the user to enter the path of a directory containing image files, iterates through all subdirectories, sorts the list of image files, and renames each file according to a specific naming format. The script checks if the file is being executed as an executable or imported as a module to another script. The default directory path, starting index, and file extension are defined as input variables. The script ensures that the directory provided by the user exists and if not, prints an error message and exits the script.

4. changeFilesDirectory:

The code is a Python script that copies files from subdirectories in a specified folder to a destination folder, avoiding duplicate file names. The script uses the os and shutil modules to manipulate files and directories. It iterates through all the subdirectories in the source folder and for each file found, it checks if the file has already been copied, if not, it creates a new file path in the destination folder and copies the file using shutil.copy(). The script also prints warning messages if a file with the same name already exists in the destination folder.

5. imageToPdf:

This is a Python script that creates a PDF file from a set of PNG and JPG images. The user is prompted to enter the PDF file name, image directory path, start and end prefixes, and output directory path. The script uses the ReportLab library to create a new PDF file and PIL library to read images. Then it loops over each image file, adds it to the PDF file, and saves the PDF file. Finally, it opens the PDF file and the output directory in the Chrome browser, and asks the user to enter a backup output directory path. If the backup output directory is provided, the script creates a backup of the PDF file.
