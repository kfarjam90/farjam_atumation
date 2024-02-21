from bs4 import BeautifulSoup

with open('movies.html','r') as file:
    html = file.read()

def validation(html_page):
    soup = BeautifulSoup(html_page,'html.parser')
    
    if soup.find('html') and soup.find('body'):
        print('HTML structure is valid')
    else:
        print('HTML structure is not valid')

validation(html)
