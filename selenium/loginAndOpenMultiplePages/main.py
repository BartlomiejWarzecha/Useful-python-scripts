import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

import time


def load_config():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config


def save_config(config):
    with open('config.json', 'w') as f:
        json.dump(config, f)



def run_configs(config_numbers):
    config = load_config()
    
    # Loop through the chosen configurations and ask the user for new values
    for i in config_numbers:
        print(f"\nExecuting configuration {i}:")
        change_config = input(f"Do you want to change configuration {i}? (y/n)")

        if change_config.lower() == 'y':
            # Ask the user for new values for each configuration element
            config[f'Main_Page_{i}'] = input("Enter the new Main_Page value:")
            config[f'Username_name_{i}'] = input("Enter the new Username_name value:")
            config[f'Password_name_{i}'] = input("Enter the new Password_name value:")
            config[f'Login_Button_{i}'] = input("Enter the new Login_Button value:")
            config[f'Username_{i}'] = input("Enter the new Username value:")
            config[f'Password_{i}'] = input("Enter the new Password value:")
            config[f'Pages_{i}'] = input("Enter the new Pages value (comma separated): ").split(',')
            save_config(config)
        elif change_config.lower() != 'n':
            # If the input is invalid, print an error message and move on to the next configuration
            print("Invalid input. Configuration not changed.")

        while True:
            try:
                    # navigate to the login page
                    driver = create_webdriver()
                    login_page_url = config[f'Main_Page_{i}']
                    driver.get(login_page_url)

                    # Log in
                    username_field_name = config[f'Username_name_{i}']
                    password_field_name = config[f'Password_name_{i}']
                    login_button_name = config[f"Login_Button_{i}"]
                    username = config[f'Username_{i}']
                    password = config[f'Password_{i}']
                    login(username_field_name, password_field_name, login_button_name, username, password, driver)

                    # Open the pages specified in the configuration
                    pages = config[f'Pages_{i}']
                    open_pages(pages, driver)
            except Exception as e:
                print(f"Error occurred: {e} ")
                break
            finally:
                if driver is not None:
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

def open_pages(pages, driver):
    for link in pages:
        new_tab_script = "window.open('" + link + "', '_blank')"
        driver.execute_script(new_tab_script)

def show_config():
    config = load_config()
    print(json.dumps(config, indent=4))

if __name__ == '__main__':
    show_config()
 
    config_choice = input("Which configurations do you want to run? (1-5 comma separated) - you can edit chosen config: ")
    chosen_configs = []
    for choice in config_choice.split(','):
        if choice.strip() in ['1', '2', '3', '4', '5']:
            chosen_configs.append(int(choice.strip()))

if chosen_configs:
    run_configs(chosen_configs)
else:
    print("Invalid input. Please enter a number between 1 and 5")
