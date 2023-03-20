import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

import time

def load_config():
    with open('config.json', 'r') as f:
        config = json.load(f)
        # add the new field with a default value of None
        config.setdefault('Consent_Element_name', None)
    return config

def save_config(config):
    with open('config.json', 'w') as f:
        json.dump(config, f)

def run_config():
    config = load_config()
    print("Executing configuration:")
    change_config = input("Do you want to change the configuration? (y/n)")

    if change_config.lower() == 'y':
        # Ask the user for new values for each configuration element
        config['Main_Page'] = input("Enter the new Main_Page value:")
        config['Username_name'] = input("Enter the new Username_name value:")
        config['Password_name'] = input("Enter the new Password_name value:")
        config['Login_Button_name'] = input("Enter the new Login_Button value:")
        config['Username'] = input("Enter the new Username value:")
        config['Password'] = input("Enter the new Password value:")
        config['Consent_Element_name'] = input("Enter the new Consent_Element_name value (or leave blank for None):")
        save_config(config)
    elif change_config.lower() != 'n':
        # If the input is invalid, print an error message and move on to the next configuration
        print("Invalid input. Configuration not changed.")

    while True:
        try:
            # Navigate to the login page
            driver = create_webdriver()
            login_page_url = config['Main_Page']
            driver.get(login_page_url)

            # Check if a consent confirmation element is provided in the configuration
            consent_element_name = config['Consent_Element_name']
            if consent_element_name is not None:
                # Click on the consent confirmation element
                consent_element = driver.find_element("class name", consent_element_name)
                consent_element.click()


            # Log in
            username_field_name = config['Username_name']
            password_field_name = config['Password_name']
            login_button_name = config['Login_Button_name']
            username = config['Username']
            password = config['Password']

            login(username_field_name, password_field_name, login_button_name, username, password, driver)

            # Open the pages specified in the configuration
            pages = config['Pages']
            open_pages(pages, driver)
            time.sleep(100000)
        except Exception as e:
            print(f"Error occurred: {e} ")
            break
        finally:
            if driver is not None:
                driver.quit()
                break

def create_webdriver():
    path_to_chromedriver = 'C:\\Users\\Justyna\\Downloads\\chromedriver\\chromedriver.exe'
    service = Service(path_to_chromedriver)
    driver = webdriver.Chrome(service=service)
    return driver

def login(username_field_name, password_field_name, login_button_name, username, password, driver):
    username_field = driver.find_element("name", username_field_name)
    password_field = driver.find_element("name", password_field_name)
    login_button = driver.find_element("name", login_button_name)
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

import time
from selenium import webdriver

def open_pages(pages, driver):

    for page in pages:
        driver.get(page)
        input("Please click on the links you want to open and then press Enter to continue...")
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            url = driver.current_url
            print(f"Downloading file from {url}...")
            download_button = driver.find_element("xpath", "//a[text()='Pobierz folder']").click()
            time.sleep(20)
            driver.close()
            print(f"Closed tab with URL: {url}")
        driver.switch_to.window(driver.window_handles[0])


def show_config():
    config = load_config()
    print(json.dumps(config, indent=4))

if __name__ == '__main__':
    show_config()
    run_config()
