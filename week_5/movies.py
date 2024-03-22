import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd


web = "https://www.rottentomatoes.com/"
path = '/Users/parha/Documents/chromedriver-win64/chromedriver.exe'

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
#driver.implicitly_wait(5)
driver.get(web)
driver.maximize_window()

driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]').click()

movies_list = ["'War Sailor'","'War Machine'","'Warhorse One'"]
movie_names = []
audience_counts = []
audience_scores = []
tomatometers = []
movie_infos = []

for subject in movies_list:
    search_path = "//a[contains(text()," +subject+ ")]"


    search_box = driver.find_element(By.XPATH,"//input[@slot='search-input']")
    search_box.send_keys(subject)
    search_box.send_keys(Keys.ENTER)
    sleep(1)

    movie_tab = driver.find_element(By.XPATH, '//*[@id="search-results"]/nav/ul/li[2]/span').click()
    sleep(1)

    my_movie = driver.find_element(By.XPATH, search_path)
    movie_name = my_movie.text
    movie_names.append(movie_name)
    my_movie.click()
    sleep(1)
    
    audience_count = driver.find_element(By.XPATH,'//a[@slot="audience-count"]').text
    audience_counts.append(audience_count)

    audience_score = driver.find_element(By.XPATH, '//score-board-deprecated').get_attribute('audiencescore')
    audience_scores.append(audience_score)

    tomatometerscore_score = driver.find_element(By.XPATH, '//score-board-deprecated').get_attribute('tomatometerscore')
    tomatometers.append(tomatometerscore_score)

    info = driver.find_element(By.XPATH, '//p[@data-qa="movie-info-synopsis"]').text
    movie_infos.append(info)

df = pd.DataFrame(zip(movie_names,audience_counts,audience_scores,tomatometers,movie_infos)
                  ,columns=['movie_names','audience_counts','audience_scores','tomatometers','movie_infos'])

df.to_excel(r"C:\Users\parha\Desktop\class\movie2.xlsx",index=False)