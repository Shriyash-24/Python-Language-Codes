from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get("https://www.facebook.com")

email_element = driver.find_element(By.XPATH, './/*[@id="email"]')
email_element.send_keys('8668727382')

pass_element = driver.find_element(By.XPATH, './/*[@id="pass"]')
pass_element.send_keys('Lol@2004')

time.sleep(3)

element = driver.find_element(By.NAME, 'login')
element.click()
time.sleep(80)

status_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div[1]')
status_element.click()
time.sleep(5)

status_element.send_keys('Hi there.')
time.sleep(5)

post = driver.find_element(By.CLASS_NAME, 'x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft')
post.click()



