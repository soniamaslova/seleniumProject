import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": os.path.abspath('../lesson_6/downloads')
}
chrome_options.add_experimental_option("prefs", prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("http://the-internet.herokuapp.com/download")

time.sleep(3)

elements = driver.find_elements("xpath", "//a")

for element in elements[1:]:
    element.click()

time.sleep(3)