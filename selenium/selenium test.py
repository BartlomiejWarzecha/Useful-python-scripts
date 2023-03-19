from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create an instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the login page
driver.get("https://suszi.wszib.edu.pl/suszi-web/login")

# Find the username and password fields by name and enter the login credentials
username_field = driver.find_element_by_name("login")
password_field = driver.find_element_by_name("password")

username_field.send_keys("your_username")
password_field.send_keys("your_password")

# Submit the login form by pressing enter in the password field
password_field.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(50)

# Close the browser window
driver.quit()
