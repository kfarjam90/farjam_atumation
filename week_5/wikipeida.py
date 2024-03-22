import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep
import pandas as pd

web = "https://www.wikipedia.org/"
path = '/Users/parha/Documents/chromedriver-win64/chromedriver.exe'

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
#driver.implicitly_wait(5)
driver.get(web)
driver.maximize_window()


# Exercise 3 - Wikipedia Scraper
# Open the Wikipedia main page.
# Select a random topic link from the main page.
# Click on the chosen topic link.
# Extract and print the titles of all sections in the table of contents.




driver.find_element(By.XPATH, '//*[@id="js-link-box-en"]').click()
sleep(5)

driver.find_element(By.XPATH, '//*[@id="mp-tfa"]/p/b[1]/a').click()
sleep(5)

topics = driver.find_elements(By.XPATH, "//li[@class='vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded']")

for item in topics:
    print(item.text)