from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import time

# Przykładowe linki do stron, z których chcemy pobierać pliki
strony = ["https://chomikuj.pl/pati94blackangel/One+Piece+manga+PL/One+Piece+586+-+City+of+Stench"]

# Przykładowy wzór strony do otwarcia
wzor_strony = "One+Piece+586+-+City+of+Stench"

# Tworzenie instancji przeglądarki Chrome

driver = webdriver.Chrome()

# Przetwarzanie każdej strony
for strona in strony:
    # Otwieranie nowej karty z podanym adresem strony
    driver.execute_script("window.open('{}', '_blank')".format(strona))
    # Zmiana do nowo otwartej karty
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)
    
    # Wyszukiwanie linku do wzoru strony i klikanie w niego
    link = driver.find_element_by_xpath("//a[contains(@href, '{}')]".format(wzor_strony))
    link.click()
    time.sleep(2)
    
    # Pobieranie linku do pliku i pobieranie pliku
    pliki = driver.find_elements_by_xpath("//a[contains(@href, 'archived')]")
    for plik in pliki:
        link_do_pliku = plik.get_attribute("href")
        urllib.request.urlretrieve(link_do_pliku, "nazwa_pliku")
    
    # Zamykanie karty
    driver.close()
    # Zmiana do karty z poprzedniej pętli
    driver.switch_to.window(driver.window_handles[0])
    
# Zamykanie przeglądarki
driver.quit()




