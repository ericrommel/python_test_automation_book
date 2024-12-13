import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up WebDriver
driver = webdriver.Chrome()  # Replace with Firefox, Edge, etc., as needed

# Open a website
driver.get("https://playwright.dev/")
time.sleep(3)

# Find an element and interact
element = driver.find_element(By.CSS_SELECTOR, ".DocSearch-Button-Placeholder")
# # print(element)
element.click()
time.sleep(7)

# Close the browser
driver.quit()
