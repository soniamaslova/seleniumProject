import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/selectable")

GRID_BUTTON = driver.find_element("xpath", "//a[@id='demo-tab-grid']")
GRID_BUTTON.click()

BUTTON_1 = driver.find_element("xpath", "//li[text()='One']")
BUTTON_1.click()

BUTTON_2 = driver.find_element("xpath", "//li[text()='Two']")
BUTTON_2.click()
BUTTON_2.click()

assert "active" in BUTTON_2.get_attribute("class"), "Чек-бокс не выбран"

time.sleep(3)
