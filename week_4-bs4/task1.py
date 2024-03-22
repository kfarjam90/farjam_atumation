import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.worldometers.info/world-population/iran-population/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


tableHead = soup.thead
row_headers = []
for i in tableHead.find_all('tr'):
    for y in tableHead.find_all('th'):
        row_headers.append(y.text)
#print(row_headers)
        
tableBody = soup.tbody
values = []
for tr in tableBody.find_all('tr'):
    td_tags = tr.find_all('td')
    td_val = [td.text for td in td_tags]
    if any(year in td_val for year in ['2020', '2022', '2023', '2024']):
        values.append(td_val)
#print(values)
    
# df = pd.DataFrame(values,columns=row_headers)
# # print(df)
# # df.to_excel(r"C:\Users\parha\Desktop\week_4-bs4\tabledata.xlsx",index=False)

population_data = {}
for row in values:
    year = row[0]
    population = int(row[1].replace(',', ''))
    population_data[year] = population


population_2023_2024 = 0
for year in ['2023', '2024']:
    if year in population_data:
        population_2023_2024 += population_data[year]

print("Sum of population for 2023 and 2024:", population_2023_2024)