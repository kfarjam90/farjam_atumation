import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep


web = "https://rahulshettyacademy.com/angularpractice/"
path = '/Users/parha/Documents/chromedriver-win64/chromedriver.exe'


service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)
driver.get(web)

driver.find_element(By.XPATH,'/html/body/app-root/app-navbar/div/nav/ul/li[2]/a').click()
products = driver.find_elements(By.XPATH,'//div[@class="card h-100"]')
names = []
for product in products:
    name = product.find_element(By.XPATH,'div/h4/a').text
    if name == 'Blackberry':
        product.find_element(By.XPATH,'div/button').click()

driver.find_element(By.XPATH,'//a[@class="nav-link btn btn-primary"]').click()
driver.find_element(By.XPATH,'/html/body/app-root/app-shop/div/div/div/table/tbody/tr[3]/td[5]/button').click()
driver.find_element(By.ID,'country').send_keys('Hun')
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,'Hungary')))
driver.find_element(By.LINK_TEXT,'Hungary').click()
driver.find_element(By.XPATH,'//div[@class="checkbox checkbox-primary"]').click()
driver.find_element(By.XPATH,'//input[@value="Purchase"]').click()
final = driver.find_element(By.XPATH,'//div[@class="alert alert-success alert-dismissible"]').text
print(final)
sleep(3)

    

