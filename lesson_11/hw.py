import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")

CHANGE_BUTTON = ("xpath", "//button[@id='populate-text']")
CHANGE_TEXT = ("xpath", "//h2[@class='target-text']")

driver.find_element(*CHANGE_BUTTON).click()
wait.until(EC.text_to_be_present_in_element(CHANGE_TEXT, "Selenium Webdriver"))

print("test 1 is passed")

DISPLAY_BUTTON = ("xpath", "//button[@id='display-other-button']")
ENABLED_BUTTON = ("xpath", "//button[text()='Enabled']")

driver.find_element(*DISPLAY_BUTTON).click()
wait.until(EC.element_to_be_clickable(ENABLED_BUTTON))

print("test 2 is passed")

ENABLE_BUTTON = ("xpath", "//button[@id='enable-button']")
CLICKABLE_BUTTON = ("xpath", "//button[@id='disable']")

driver.find_element(*ENABLE_BUTTON).click()
wait.until(EC.element_to_be_clickable(CLICKABLE_BUTTON))

print("test 3 is passed")

ALERT_BUTTON = ("xpath", "//button[@id='alert']")

driver.find_element(*ALERT_BUTTON).click()
wait.until(EC.alert_is_present())

print("test 4 is passed")