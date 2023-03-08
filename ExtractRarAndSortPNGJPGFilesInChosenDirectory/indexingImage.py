import os

def run():
    # Zmienne wejściowe - ścieżka do folderu, początkowa wartość indeksu i rozszerzenie pliku
    default_folder_path = "default path is empty - change default path in script file"
    

    folder_path = input("Enter image directory path (press enter to use default directory): " + "\n"
                    + default_folder_path  + "\n")

    if folder_path == "":
        # If no image directory is provided, use the default directory
        folder_path = default_folder_path
        print("Chosen folder path Directory:" + "\n" + folder_path);
    else:
        # Make sure the provided directory exists
        if not os.path.exists(folder_path):
            print("Image directory does not exist!")
            exit()
    start_index = 1
    file_extension = ".png"

    # Przejście przez wszystkie foldery
    for folder_name in os.listdir(folder_path):
        # Utworzenie ścieżki do folderu
        folder = os.path.join(folder_path, folder_name)
        # Sprawdzenie, czy element jest folderem i istnieje
        if os.path.isdir(folder):
            # Pobranie listy plików w folderze
            files = os.listdir(folder)
            # Sortowanie listy plików alfabetycznie
            files.sort()
            # Inicjalizacja zmiennej przechowującej poprzednią nazwę pliku
            prev_file_name = ""
            # Iterowanie przez listę plików
            for i, file_name in enumerate(files):
                # Sprawdzenie, czy plik ma rozszerzenie .png lub .jpg
                if file_name.endswith(".jpg") or file_name.endswith(".png"):
                    # Utworzenie nowej nazwy pliku
                    new_file_name = folder_name + str(i + start_index).zfill(3) + file_extension
                    # Sprawdzenie, czy stara i nowa nazwa są takie same
                    if file_name == new_file_name:
                        print(f"Nie zmieniono nazwy pliku {file_name}, ponieważ nowa nazwa jest taka sama.")
                        continue
                    # Utworzenie ścieżki do starej nazwy pliku
                    old_file_path = os.path.join(folder, file_name)
                    # Utworzenie ścieżki do nowej nazwy pliku
                    new_file_path = os.path.join(folder, new_file_name)
                    # Sprawdzenie, czy poprzednia nazwa pliku jest taka sama jak stara nazwa pliku
                    if prev_file_name == file_name:
                        print(f"Nie zmieniono nazwy pliku {file_name}, ponieważ poprzednia i obecna nazwa pliku są takie same.")
                    else:
                        # Wypisanie starych i nowych nazw plików w konsoli
                        print(f"Stara nazwa pliku: {old_file_path}")
                        print(f"Nowa nazwa pliku: {new_file_path}")
                        # Zmiana nazwy pliku
                        os.rename(old_file_path, new_file_path)
                    # Zapisanie obecnej nazwy pliku do zmiennej prev_file_name
                    prev_file_name = file_name

if __name__ == "__main__":
    run()

