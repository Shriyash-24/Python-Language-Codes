from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.maximize_window()

driver.get("https://www.facebook.com")
time.sleep(3)

email_element = driver.find_element(By.XPATH, './/*[@id="email"]')
email_element.send_keys('8668727382')

time.sleep(1)

pass_element = driver.find_element(By.XPATH, './/*[@id="pass"]')
pass_element.send_keys('Shriyash@2004')

time.sleep(3)

element = driver.find_element(By.NAME, 'login')
element.click()
time.sleep(30)

composer = driver.find_element(By.XPATH, ".//span[contains(text(), \"What's on your mind\")]")
composer.click()
time.sleep(3)

text_area = driver.find_element(By.XPATH, './/div[@data-lexical-editor = "true"]')
text_area.send_keys('Automated Post')

time.sleep(3)

post = driver.find_element(By.XPATH, './/div[@aria-label="Post"]')
post.click()

time.sleep(10)
driver.quit()

