from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("https://www.amazon.in")

driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys('iphones')
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
time.sleep(5)


