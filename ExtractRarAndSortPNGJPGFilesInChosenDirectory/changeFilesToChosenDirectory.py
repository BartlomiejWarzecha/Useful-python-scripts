import os
import shutil

def run():

    default_output_path = "default path is empty - change default path in script file"

    default_folder_path = "default path is empty - change default path in script file"
    
    # ścieżka do folderu, w którym znajdują się podfoldery z plikami
    folder_path = input("Podaj ścieżkę do folderu z którego chcesz przenieść pliki, albo pozostaw podstawowy" + "\n"
                        + default_folder_path  + "\n")
    
    if(folder_path == ""):
        folder_path = default_folder_path

    # pobranie ścieżki do folderu, do którego zostaną wypakowane pliki z podfolderów
    output_folder_path = input("Podaj ścieżkę do folderu wyjściowego:  albo pozostaw podstawowy" + "\n"
                        + default_output_path  + "\n")

    if(output_folder_path  == ""):
        output_folder_path = default_output_path

    # Create the extracted directory if it doesn't exist
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    # lista przechowująca nazwy już skopiowanych plików
    copied_files = []

    # iteracja po wszystkich podfolderach
    for subdir, dirs, files in os.walk(folder_path):
        for file in files:
            # utworzenie ścieżki do oryginalnego pliku
            filepath = os.path.join(subdir, file)
            # sprawdzenie, czy plik został już skopiowany
            if file not in copied_files:
                # utworzenie ścieżki do nowego pliku w folderze wyjściowym
                new_filepath = os.path.join(output_folder_path, file)
                # sprawdzenie, czy plik o takiej samej nazwie już istnieje w folderze wyjściowym
                if os.path.exists(new_filepath):
                    print(f"Ostrzeżenie: plik {file} już istnieje w folderze wyjściowym")
                else:
                    # sprawdzenie, czy plik ma żądane rozszerzenie .png lub .jpg
                    file_ext = os.path.splitext(file)[-1]
                    if file_ext == ".png" or file_ext == ".jpg":
                        # skopiowanie pliku do folderu wyjściowego
                        shutil.copy(filepath, new_filepath)
                        # dodanie nazwy skopiowanego pliku do listy copied_files
                        copied_files.append(file)
                        print(f"Przekopiowano plik {file}")
                    else:
                        print(f"Plik {file} ma nieobsługiwane rozszerzenie")
            else:
                print(f"Plik {file} już został skopiowany wcześniej")

if __name__ == "__main__":
    run()
