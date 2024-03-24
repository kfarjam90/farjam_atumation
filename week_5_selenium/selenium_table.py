import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep
import pandas as pd

web = "https://www.premierleague.com/"
path = '/Users/parha/Documents/chromedriver-win64/chromedriver.exe'


service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)
driver.get(web)
driver.maximize_window()

driver.find_element(By.XPATH, '//a[@class="global-btn global-btn__icn-right league-table-sm__cta"]').click()
sleep(5)

tableHead = driver.find_element(By.TAG_NAME, 'thead')
row_headers = [th.text for th in tableHead.find_elements(By.TAG_NAME, 'th')]
#print(row_headers)

tableBody = driver.find_element(By.TAG_NAME,'tbody')
values = []
for tr in tableBody.find_elements(By.TAG_NAME,'tr'):
    td_tag = tr.find_elements(By.TAG_NAME,'td')
    td_val = [td.text for td in td_tag]
    values.append(td_val)
#print(values)
    
df = pd.DataFrame(values,columns=row_headers)
df.to_excel(r"C:\Users\parha\Desktop\week_5\football.xlsx",index=False)