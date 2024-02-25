import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://www.amazon.in/'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

search_box = driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')
search_box.send_keys('dell laptops')

driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]').click()

driver.find_element(By.XPATH,'//span[text()="Dell"]').click()

laptops = driver.find_elements(By.XPATH,'//div[@data-component-type="s-search-result"]')

laptop_name = []
laptop_price = []
no_reviews = []
final_list = []

for laptop in laptops: 
  
    names =laptop.find_elements(By.XPATH,".//span[@class='a-size-medium a-color-base a-text-normal']")
    for name in names:
        laptop_name.append(name.text)
        
    try:
        if len(laptop.find_elements(By.XPATH,".//span[@class='a-price-whole']"))>0:
            prices= laptop.find_elements(By.XPATH,".//span[@class='a-price-whole']")
            for price in prices:
                laptop_price.append(price.text)
        else:
            laptop_price.append("0")
    except:
        pass
    
    try:
        if len(laptop.find_elements(By.XPATH,".//span[@class='a-size-base s-underline-text']"))>0:
            reviews = laptop.find_elements(By.XPATH,".//span[@class='a-size-base s-underline-text']")
            for review in reviews:
                no_reviews.append(review.text)
        else:
            no_reviews.append("0")
    except:
        pass
        
print('no of laptops==>',len(laptop_name))
print('no of prices==>',len(laptop_price))
print('no of reviews==>',len(no_reviews))



df = pd.DataFrame(zip(laptop_name,laptop_price,no_reviews),columns=['laptop_name','laptop_price','no_reviews'])

df.to_excel(r"C:\Users\parha\Desktop\n\laptops.xlsx",index=False)

driver.quit()

