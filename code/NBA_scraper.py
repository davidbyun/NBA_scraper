# -*- coding: utf-8 -*-
"""
Created on Dec 1 2019

@author: David Byun

NBA.com Scraper

I wanted to write a web scraper for NBA.com to use the data to help with my fantasy 
basketball team. My friends and I all have our own strategies and I am interested 
in developing a tool that can help us and save time. I am also interested in being 
able to compare our draft results with actual basketball performances to see 
how well we drafted (maybe bring in a Yahoo API for this?).

nba.com/robots.txt has not forbidden scraping of the player's data sections

Sections to Scrape:
A. Players - General - Traditional [https://stats.nba.com/players/traditional/?sort=PTS&dir=-1]
    1. Season, Season Type, Per Mode, Season Segment
    *. webpage uses JavaScript - using Selenium to navigate to the next page


"""

import os
import re
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


# target webpage
target_url = "https://stats.nba.com/players/traditional/?sort=PTS&dir=-1"

# initiate chromedriver
driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe")
# navigate to webpage
driver.get(target_url)
# sleep
time.sleep(5)
# pull html of target_url
html = driver.page_source
# beautify html using BS4
soup = BeautifulSoup(html, "html5lib")

# player stats
player_stat_cols = ["rank","player_name","team","age","gp","w","l","min","pts","fgm","fga","fg%","threepm",
                "threepa","threep%","ftm","fta","ft%","oreb","dreb","reb","ast",
                "tov","stl","blk","pf","fp","dd2","td3","plusminus"]
# I want iterate through "td"s and save data
player_data_df = pd.DataFrame(columns = player_stat_cols) 


## loop for every page - save all player stats
while True:
    # save html
    html = driver.page_source
    # beautify html using BS4
    soup = BeautifulSoup(html, "html5lib")
    
    # find all td's
    td = soup.find_all("td")
    
    # turn bs4 ResultSet into a list
    td_list = list(td)
    # strip the text from each object and save to a lsit
    clean_td_list = [n.text.strip() for n in td_list]
    
    # check if on last page
    # every page other than the last has exactly 1600 td elements
    if len(clean_td_list) < 1600:
        # calculate the number of players on the last page of the table
        # floor (len(clean_td_list) / 30) = number of players?
        # floor (224 / 30 ) = 7, which works for this table - test on others
        num_of_players = len(clean_td_list) // 30
        
        # subset the clean_td_list for player information
        players_td_list = clean_td_list[0:num_of_players*30]
    else:
        # player data (for 50 players) exists in the first 1500 objects
        players_td_list = clean_td_list[0:1500]
    
    # parse clean_td_list into individual metric lists
    rank_list = players_td_list[0::30]
    player_name_list = players_td_list[1::30]
    team_list = players_td_list[2::30]
    age_list = players_td_list[3::30]
    gp_list = players_td_list[4::30]
    w_list = players_td_list[5::30]
    l_list = players_td_list[6::30]
    min_list = players_td_list[7::30]
    pts_list = players_td_list[8::30]
    fgm_list = players_td_list[9::30]
    fga_list = players_td_list[10::30]
    fgperc_list = players_td_list[11::30]
    threepm_list = players_td_list[12::30]
    threepa_list = players_td_list[13::30]
    threepperc_list = players_td_list[14::30]
    ftm_list = players_td_list[15::30]
    fta_list = players_td_list[16::30]
    ftperc_list = players_td_list[17::30]
    oreb_list = players_td_list[18::30]
    dreb_list = players_td_list[19::30]
    reb_list = players_td_list[20::30]
    ast_list = players_td_list[21::30]
    tov_list = players_td_list[22::30]
    stl_list = players_td_list[23::30]
    blk_list = players_td_list[24::30]
    pf_list = players_td_list[25::30]
    fp_list = players_td_list[26::30]
    dd2_list = players_td_list[27::30]
    td3_list = players_td_list[28::30]
    plusminus_list = players_td_list[29::30]
    
    # create a dictionary of lists for dataframe construction
    col_dict = {'rank': rank_list, 'player_name': player_name_list, 'team': team_list,
                'age': age_list, 'gp': gp_list, 'w': w_list, 'l': l_list, 'min': min_list,
                'pts': pts_list, 'fgm': fgm_list, 'fga': fga_list, 'fg%': fgperc_list,
                'threepm': threepm_list, 'threepa': threepa_list, 'threep%': threepperc_list,
                'ftm': ftm_list, 'fta': fta_list, 'ft%': ftperc_list, 'oreb': oreb_list,
                'dreb': dreb_list, 'reb': reb_list, 'ast': ast_list, 'tov': tov_list,
                'stl': stl_list, 'blk': blk_list, 'pf': pf_list, 'fp': fp_list,
                'dd2': dd2_list, 'td3': td3_list, 'plusminus': plusminus_list}  
    # build player data dataframe using column dictionary
    part_player_data_df = pd.DataFrame(col_dict)
    # add these players to the player_data_df
    player_data_df = player_data_df.append(part_player_data_df)
    
    #DJB- think about removing rank - will differ depending on the statistic that is being focused
    
    # click next page button
    # two "next page" elements found; both work
    elements = driver.find_elements_by_class_name("stats-table-pagination__next")
    elements[0].click()
    # sleep
    time.sleep(3)
    
    # break operation if on last page
    if len(clean_td_list) < 1600:
        break


# reset index
player_data_df.reset_index(drop=True, inplace=True)

# quit chromedriver
driver.quit()









