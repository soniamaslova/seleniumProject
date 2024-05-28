import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

YES_RADIO_STATUS = ("xpath", "//input[@id='yesRadio']")
YES_RADIO_ACTION = ("xpath", "//label[@for='yesRadio']")

NO_RADIO_STATUS = ("xpath", "//input[@id='noRadio']")
NO_RADIO_ACTION = ("xpath", "//label[@for='noRadio']")

driver.get("https://demoqa.com/radio-button")
print(driver.find_element(*NO_RADIO_STATUS).is_enabled())
time.sleep(2)


