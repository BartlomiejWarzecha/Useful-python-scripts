import os
import rarfile

# Define the directory where the RAR files are located
rar_dir = ""

# Define the directory where you want to extract the files
extract_dir = ""

# Loop through all files in the directory
for filename in os.listdir(rar_dir):
    # Check if the file is a RAR file
    if filename.endswith(".rar"):
        # Open the RAR file
        rar = rarfile.RarFile(os.path.join(rar_dir, filename))

        # Extract the contents of the RAR file to the extract directory
        rar.extractall(path=extract_dir)

        # Close the RAR file
        rar.close()
        print(filename + "extraction complete.")


print("Full Extraction complete.")
