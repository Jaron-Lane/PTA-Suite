import time

from selenium import webdriver

# Open browser
driver = webdriver.Chrome()
time.sleep(3)

# Go to webpage
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(5)