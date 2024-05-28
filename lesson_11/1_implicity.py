from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

driver.get("https://demoqa.com/dynamic-properties")

visible_after_button = ("xpath", "//button[@id='visibleAfter']")

driver.find_element(*visible_after_button).click()