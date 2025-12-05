from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Edge()
driver.get("https://www.amazon.in")
driver.maximize_window()

time.sleep(5)
select = driver.find_element(By.LINK_TEXT, "Today's Deals")
select.click()
time.sleep(5)
select_1 = driver.find_element(By.LINK_TEXT, "Electronics")
select_1.click()
time.sleep(5)