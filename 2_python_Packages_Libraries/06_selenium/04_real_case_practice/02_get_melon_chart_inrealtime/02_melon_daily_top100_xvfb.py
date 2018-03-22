from pyvirtualdisplay import Display
from selenium import webdriver
import pandas as pd
import datetime


display = Display(visible=0, size=(800, 600))
display.start()

url_1 = "https://www.melon.com/chart/day/index.htm"
url_2 = "https://www.melon.com/chart/day/index.htm#params%5Bidx%5D=51"

def melon_daily_100():
    
    melon_day = pd.DataFrame(columns = ["Ranking", "Song", "Artist", "Album"])
    
    driver = webdriver.Chrome()
    
    driver.get(url_1) 
    table_50 = driver.find_elements_by_css_selector("#tb_list tbody #lst50")
    
    for table in table_50:

        rank = table.find_element_by_css_selector(".rank").text
        song = table.find_element_by_css_selector(".wrap_song_info .ellipsis.rank01 a").text
        artist = table.find_element_by_css_selector(".wrap_song_info .ellipsis.rank02 a").text
        album = table.find_element_by_css_selector(".wrap_song_info .ellipsis.rank03 a").text

        data = {"Ranking" : rank, 
                "Song" : song, 
                "Artist" : artist, 
                "Album" : album, }

        melon_day.loc[len(melon_day)] = data
    
    
    
    driver.get(url_2)
    table_100 = driver.find_elements_by_css_selector("#tb_list tbody .lst100")
    
    for table in table_100:

        rank = table.find_element_by_css_selector(".rank").text
        song = table.find_element_by_css_selector(".wrap_song_info .ellipsis.rank01 a").text
        artist = table.find_element_by_css_selector(".wrap_song_info .ellipsis.rank02 a").text
        album = table.find_element_by_css_selector(".wrap_song_info .ellipsis.rank03 a").text

        data = {"Ranking" : rank, 
                "Song" : song, 
                "Artist" : artist, 
                "Album" : album, }

        melon_day.loc[len(melon_day)] = data
    
    
    melon_day = melon_day.set_index('Ranking')
    
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d")

    melon_day.to_csv('melon_daily_100_(' + str(current_time) + ').csv', encoding='utf-8' )
    
    driver.close()
    
    
melon_daily_100()

