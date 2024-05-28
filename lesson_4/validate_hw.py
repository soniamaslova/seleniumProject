import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://vk.com/")

title_vk = driver.title
print("Текущий заголовок: ", title_vk)

driver.get("https://ya.ru/")

title_ya = driver.title
print("Текущий заголовок: ", title_ya)

driver.back()

url = driver.current_url
assert url == "https://vk.com/", "Ошибка в URL, открыта не та страница"

driver.refresh()

current_url = driver.current_url
print("Текущий URL: " ,current_url)

driver.forward()

url = driver.current_url
assert url == "https://ya.ru/", "Ошибка в URL, открыта не та страница"
