# Finding by clas.
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("https://www.google.com")
driver.maximize_window()

time.sleep(2)

search = driver.find_element(By.CLASS_NAME, 'u4Uk3c')
search.click()
time.sleep(60)
