import time

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_options = Options()

display = Display(visible=0, size=(800, 600))
display.start()

Login = '' # Ваш логин
Password = '' # Ваш пароль

crontab_chrome_path = '/usr/bin/chromedriver'
crontab_chrome = '/home/dragunov/Logs/crontab_chrome_onliner.log' # Путь для лога
service = Service(executable_path=crontab_chrome_path, log_path=crontab_chrome) # Запуск бинарника
driver = webdriver.Chrome(options=chrome_options, service=service)

driver.get("https://profile.onliner.by/")
driver.set_page_load_timeout(7)

input_login = driver.find_element(By.CSS_SELECTOR, "input.auth-input[type='text']") # Внесение данных в поле логин
input_login.send_keys(Login)
time.sleep(5)

input_password = driver.find_element(By.CSS_SELECTOR, "input.auth-input[type='password']")  # Внесение данных в поле пароль
input_password.send_keys(Password)
time.sleep(5)

button_submit = driver.find_element(By.CSS_SELECTOR, "button.auth-button[type='submit']") # Вход на сайт
button_submit.click()
time.sleep(5)

driver.get("https://baraholka.onliner.by/search.php?type=ufleamarket")
driver.set_page_load_timeout(10)

checkbox = driver.find_element(By.ID, 'select-all-my-adverts')
checkbox.click()
time.sleep(5)

up_button = driver.find_element(By.CSS_SELECTOR, "a.btn-up-2-orange")
up_button.click()
driver.close()
