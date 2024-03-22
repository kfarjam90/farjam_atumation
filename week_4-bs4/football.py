import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep
import pandas as pd

url = "https://www.premierleague.com/"
path = '/Users/parha/Documents/chromedriver-win64/chromedriver.exe'


service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)
driver.get(url)

tableHead = driver.find_element(By.TAG_NAME, 'thead')
row_headers = [th.text for th in tableHead.find_elements(By.TAG_NAME, 'th')]

tableBody = driver.find_element(By.TAG_NAME, 'tbody')
values = []
for tr in tableBody.find_elements(By.TAG_NAME, 'tr'):
    td_tags = tr.find_elements(By.TAG_NAME, 'td')  # Changed find_element to find_elements
    td_val = [td.text for td in td_tags]
    values.append(td_val)

df = pd.DataFrame(values, columns=row_headers)
df.to_excel(r"C:\Users\parha\Desktop\week_4-bs4\football.xlsx", index=False)  # Corrected file path
driver.quit()