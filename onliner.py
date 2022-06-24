import time
from datetime import datetime
from config import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

# set date and time in dd/mm/YY H/M/S
now = datetime.now()
date_cron = now.strftime("%d/%m/%Y %H:%M:%S")
#

# chrome options
driver_options = webdriver.ChromeOptions()
driver_options.add_argument("no-sandbox")
driver_options.add_argument("--headless")
driver_options.add_argument("--disable-gpu")
driver_options.add_argument("--window-size=1920,1080")
driver_options.add_argument("--disable-extensions")
driver_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36")
#

# login and password from config.py
Login = input_login_hh
Password = input_password
#

# setting path for web driver path and log path
chrome_service = Service(executable_path=crontab_chromedriver_path)
driver = webdriver.Chrome(service=chrome_service, service_log_path=crontab_chromedriver_log, options=driver_options)
#

url = ["https://profile.onliner.by/", "https://baraholka.onliner.by/search.php?type=ufleamarket"]

try:
    driver.get(url[0])
    driver.set_page_load_timeout(7)
except TimeoutException:
    print(date_cron, "Can't go on", url[0])
    driver.quit()

try:
    input_login = driver.find_element(By.CSS_SELECTOR, "input.auth-input[type='text']")  # Внесение данных в поле логин
    input_login.send_keys(Login)
    time.sleep(5)
except NoSuchElementException:
    print(date_cron, "Can't see login input")
    driver.quit()

try:
    input_password = driver.find_element(By.CSS_SELECTOR, "input.auth-input[type='password']")  # Внесение данных в поле пароль
    input_password.send_keys(Password)
    time.sleep(5)
except NoSuchElementException:
    print(date_cron, "Can't see password input")
    driver.quit()

try:
    button_submit = driver.find_element(By.CSS_SELECTOR, "button.auth-button[type='submit']")  # Вход на сайт
    button_submit.click()
    time.sleep(5)
except NoSuchElementException:
    print(date_cron, "Can't click on submit button")
    driver.quit()

try:
    driver.get(url[1])
    driver.set_page_load_timeout(10)
except TimeoutException:
    print(date_cron, "Can't go on", url[1])
    driver.quit()

try:
    checkbox = driver.find_element(By.ID, "select-all-my-adverts")
    checkbox.click()
    time.sleep(5)
except NoSuchElementException:
    print(date_cron, "Can't click on select all button")
    driver.quit()

try:
    up_button = driver.find_element(By.CSS_SELECTOR, "a.btn-up-2-orange")
    up_button.click()
except NoSuchElementException:
    print(date_cron, "Can't click on up button")
    driver.quit()
    
