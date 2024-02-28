#New York Times API, Write a program to find articles about the moon landing by Apollo 11
import requests

def find_articles():
    url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
    param = {'q':'Apollo 11 moon landing' , 'api-key': 'wycCt4nQoT8VEgC3chPeUUI7MefabaUf'}

    resposne = requests.get(url,params=param)

    if resposne.status_code == 200:
        resposne = resposne.json()
        main = resposne['response']['docs']
        for item in main:
            print(item['headline']['main'])
            print(item['snippet'])
            print(item['pub_date'])
            print(f'--------------')

find_articles()
    
        