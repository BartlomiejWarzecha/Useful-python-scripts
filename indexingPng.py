import os

# Zmienne wejściowe - ścieżka do folderu, początkowa wartość indeksu i rozszerzenie pliku
folder_path = ""
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
        # Iterowanie przez listę plików
        for i, file_name in enumerate(files):
            # Utworzenie nowej nazwy pliku
            new_file_name = folder_name + str(i + start_index).zfill(3) + file_extension
            # Utworzenie ścieżki do starej nazwy pliku
            old_file_path = os.path.join(folder, file_name)
            # Utworzenie ścieżki do nowej nazwy pliku
            new_file_path = os.path.join(folder, new_file_name)
            # Wypisanie starych i nowych nazw plików w konsoli
            print(f"Stara nazwa pliku: {old_file_path}")
            print(f"Nowa nazwa pliku: {new_file_path}")
            # Zmiana nazwy pliku
            os.rename(old_file_path, new_file_path)
 
