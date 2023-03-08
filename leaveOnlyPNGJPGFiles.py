import os


def run():
    # Zmienne wejściowe - ścieżka do folderu, początkowa wartość indeksu i rozszerzenie plik
    default_directory= "default"

    
    # Set the path to the directory containing the files
    directory = input("Enter image directory path from which you want to delete all files besides JPG/PNG(press enter to use default directory): " + "\n"
                    + default_directory + "\n")

    
    if directory == "":
        # If no image directory is provided, use the default directory
        directory = default_directory
        print("Chosen folder path Directory:" + "\n" + folder_path);
    else:
        # Make sure the provided directory exists
        if not os.path.exists(directory):
            print("File  directory does not exist!")
            exit()


    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Get the file extension
            _, extension = os.path.splitext(file)
            # If the file is not a PNG or JPG file, delete it
            if extension not in [".png", ".jpg"]:
                os.remove(os.path.join(root, file))
                print(f"Deleted file {os.path.join(root, file)}")
                
if __name__ == "__main__":
    run()
          
