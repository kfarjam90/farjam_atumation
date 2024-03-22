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
#driver.implicitly_wait(5)
driver.get(web)
driver.maximize_window()



driver.find_element(By.XPATH,'(//a[@class="widget-header__cta  "])[3]').click()
sleep(5)

containers = driver.find_elements(By.XPATH,'//span[@class="media-thumbnail__title"]')
containers_src = driver.find_elements(By.XPATH,'//span[@class="media-thumbnail__tag"]')

titles =[]
sorce = []

for item in containers:
    titles.append(item.text)


for item in containers_src:
    sorce.append(item.text)
print(len(titles))
print(len(sorce))


my_duc = {'sorce': sorce, 'titles':titles[3:]}

df = pd.DataFrame(my_duc)
print(df)
#df.to_excel(r"C:\Users\parha\Desktop\class\new.xlsx",index=False)

