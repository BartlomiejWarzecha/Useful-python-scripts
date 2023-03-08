import extractRarFiles
import leaveOnlyPNGJPGFiles
import indexingImage
import changeFilesToChosenDirectory
import imageToPDF

extractRarFiles.run()
leaveOnlyPNGJPGFiles.run()
indexingImage.run()
changeFilesToChosenDirectory.run()

print("Posortowane pliki PNG/JPG znajdują się w wybranym folderze")

choicePDF = input("Czy chcesz utworzyć  plik pdf dla wybranych plików? (tak/nie): ")
if choicePDF.lower() == "tak":
    imageToPDF.run()
    while True:
        choicePDF = input("Czy chcesz utworzyć kolejny plik pdf dla wybranych plików? (tak/nie): ")
        if choicePDF.lower() == "tak":
            imageToPDF.run()
        elif choicePDF.lower() == "nie":
            print("Koniec działania programu!")
            exit()
        else:
            print("Niepoprawna odpowiedź, wprowadź 'tak' lub 'nie'")
else:
    print("Koniec działania programu!")
    exit()
    


