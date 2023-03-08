import os
import rarfile
import shutil

def run():
    # Define the directory where the RAR files are located
    rar_dir_default = "default path is empty - change default path in script file"

    # Define the directory where you want to extract the files
    extract_rar_dir_default = "default path is empty - change default path in script file"

    extract_files_dir_default = "default path is empty - change default path in script file"


       # Prompt the user to enter the directory where they want to extract the files
    rar_dir = input("Enter the directory where are rar filest to extract or skip with defined default in script file "  + "\n")

    if rar_dir == "":
            rar_dir = rar_dir_default
 # Prompt the user to enter the directory where they want to extract the files
    extracted_files_dir = input("Enter the directory where you want to extract the file or skip with defined default in script file "  + "\n")

    if extracted_files_dir == "":
            extracted_files_dir = extract_files_dir_default

   # Where do you want to store rar files that have been extracted?
    extract_rar_dir = input("Enter the directory where to store rar files after they have been extracted or skip with defined default in script file "  + "\n")
    

    if extract_rar_dir == "":
            extract_rar_dir = extract_rar_dir_default    
   
        
    if not os.path.exists(extracted_files_dir):
        os.makedirs(extracted_files_dir)
        

    # Loop through all files in the directory
    for filename in os.listdir(rar_dir):
        # Check if the file is a RAR file
        if filename.endswith(".rar"):
            # Create a subfolder for the RAR file in the extract directory
            rar_subfolder = os.path.splitext(filename)[0]
            extracted_files_dir = rar_dir
            if not os.path.exists(extracted_files_dir):
                os.makedirs(extracted_files_dir)

            # Open the RAR file
            rar = rarfile.RarFile(os.path.join(rar_dir, filename))

            # Extract the contents of the RAR file to the extract directory
            rar.extractall(path=extracted_files_dir)

            # Close the RAR file
            rar.close()
            print(filename + " extraction complete.")

            # Move the RAR file to the subfolder
            shutil.move(os.path.join(rar_dir, filename), os.path.join(extract_rar_dir, filename))
            print("Moved " + filename + " to " + extracted_files_dir)

    print("Full Extraction and Move complete.")

if __name__ == "__main__":
    run()
