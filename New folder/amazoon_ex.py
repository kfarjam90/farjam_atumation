import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://www.goodreads.com/book/show/2657.To_Kill_a_Mockingbird'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

driver.find_element(By.XPATH,"//span[contains(text(),'Classics')]").click()

classic = driver.find_element(By.XPATH,'//span[@id="freeTextContainer12233491553839452903"]')
print(classic.text)