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

titles = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")

print(str(len(titles)) + 'products found.')
for i in titles:
    print(i.text)