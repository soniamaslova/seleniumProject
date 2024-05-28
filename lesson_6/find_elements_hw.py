import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(3)

driver.find_elements("id", "Wikipedia1_wikipedia-search-input")

driver.find_elements("class name", "wikipedia-icon")

time.sleep(3)