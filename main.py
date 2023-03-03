from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime
from time import sleep
import pyautogui

email = "analistas1@gimipogliano.com.br"
senha = "cuDGibs6!uvfC4D"

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

browser.get("https://app.omie.com.br/login/")

browser.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
browser.find_element(By.XPATH, '//*[@id="btn-continue"]').click()
sleep(1)
browser.find_element(By.XPATH, '//*[@id="current-password"]').send_keys(senha)
browser.find_element(By.XPATH, '//*[@id="btn-login"]').click()

sleep(3)

browser.find_element(By.XPATH, '//*[@id="service-box-gimi-0wbr4mtt"]/div/div/div[5]/div/div/a').click()

sleep(10)
pyautogui.click(x=797, y=599)
sleep(5)
pyautogui.click(x=342, y=360)
sleep(15)

inicio = datetime.now()

pyautogui.click(x=1098, y=323)
sleep(1)
pyautogui.click(x=1136, y=449)
sleep(1)
pyautogui.click(x=1200, y=286)
sleep(3)
pyautogui.click(x=1200, y=286)
sleep(3)

for i in range(1000):
    pyautogui.doubleClick(x=342, y=360)
    sleep(5)
    pyautogui.click(x=1120, y=262)
    sleep(1)
    pyautogui.click(x=430, y=671)
    sleep(15)
    pyautogui.click(x=1052, y=829)
    sleep(3)
    pyautogui.click(x=131, y=276)
    sleep(5)
    pyautogui.click(x=61, y=199)
    sleep(5)

fim = datetime.now() 

print(f"{(fim - inicio).total_seconds()} segundos")
