from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("https://www.google.com")
driver.maximize_window()

time.sleep(2)

search = driver.find_element(By.NAME, 'q')
search.send_keys("selenium")
time.sleep(1)

search.submit()
time.sleep(35) # To prove I am not a robot.
driver.back()
time.sleep(1)
driver.forward()
