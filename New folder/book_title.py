
import pandas as pd
import requests as rqst
import numpy as np
from bs4 import BeautifulSoup as bs


pages = np.arange(1,5)
book_lists = []
ratings = []
price=[]


for page in pages:
    url = "https://books.toscrape.com/catalogue/page-"+str(page)+".html"
    web = rqst.get(url)
    soup = bs(web.content,"html.parser")

    # Fetch the books title
    for x in soup.find_all('h3'):
        book_lists.append(x.a['title'])

    # Fetch the ratings
    for x in soup.find_all("article"):
        ratings.append(x.p['class'][1])

    # Fetch the prices
    for x in soup.find_all('p',{'class':"price_color"}):
        price.append(x.get_text())

data = {'books_list':book_lists,'ratings':ratings,'prices':price}

book_data = pd.DataFrame(data)
print(book_data)
#book_data.to_excel(r"C:\Users\parha\Documents\ibs\atumation\book_list_all.xlsx",index=False)
