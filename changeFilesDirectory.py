
import os
import shutil

# ścieżka do folderu, w którym znajdują się podfoldery z plikami
folder_path = ""

# ścieżka do folderu, do którego zostaną wypakowane pliki z podfolderów
output_folder_path = ""

# lista przechowująca nazwy już skopiowanych plików
copied_files = []

# iteracja po wszystkich podfolderach
for subdir, dirs, files in os.walk(folder_path):
    for file in files:
        # utworzenie ścieżki do oryginalnego pliku
        filepath = subdir + os.sep + file
        # sprawdzenie, czy plik został już skopiowany
        if file not in copied_files:
            # utworzenie ścieżki do nowego pliku w folderze wyjściowym
            new_filepath = os.path.join(output_folder_path, file)
            # sprawdzenie, czy plik o takiej samej nazwie już istnieje w folderze wyjściowym
            if os.path.exists(new_filepath):
                print(f"Ostrzeżenie: plik {file} już istnieje w folderze wyjściowym")
            else:
                # skopiowanie pliku do folderu wyjściowego
                shutil.copy(filepath, new_filepath)
                # dodanie nazwy skopiowanego pliku do listy copied_files
                copied_files.append(file)
                print(f"Przekopiowano plik {file}")
        else:
            print(f"Plik {file} już został skopiowany wcześniej")
