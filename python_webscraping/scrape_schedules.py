from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

""" 8 seasons 
21-22: Oct - June
20-21: Dec - July
19-20: Oct - Oct
18-19: Oct - June
17-18: Oct - June
16-17: Oct - June
15-16: Oct - June
14:15: Oct - June
"""

season = ["october", "november", "december", "january", "february", "march", "april", "may", "june"]
season21 = ["december", "january", "february", "march", "april", "may", "june", "july"]
season20 = ["october", "november", "december", "january", "february", "march", "july", "august", "september", "october"]


urls_to_browse = []
schedule_base = "https://www.basketball-reference.com/leagues/NBA_"

for year in range (2015, 2023):

    to_loop = season
    if (year == 2020):
        to_loop = season20
    elif (year == 2021):
        to_loop = season21
    
    flag = False

    for month in to_loop:
        temp_url = schedule_base+str(year)+"_games-"+month
        if (year == 2020 and month == "october" and not flag):
            temp_url += "-2019"
            flag = True
        elif (year == 2020 and month == "october" and flag):
            temp_url += "-2020"

        temp_url += ".html"
        urls_to_browse.append (temp_url)

# print (urls_to_browse)


abbrev = pd.read_csv ("team_abbrev.csv")

teams = abbrev["Team"]
abbrevs = abbrev['Abbrev']

dict = {}

for i in range (len(abbrev)):
    dict [teams[i]] = abbrevs [i]

dict_month = {}

dict_month ['Jan'] = "01"
dict_month ['Feb'] = "02"
dict_month ['Mar'] = "03"
dict_month ['Apr'] = "04"
dict_month ['May'] = "05"
dict_month ['Jun'] = "06"
dict_month ['Jul'] = "07"
dict_month ['Aug'] = "08"
dict_month ['Sep'] = "09"
dict_month ['Oct'] = "10"
dict_month ['Nov'] = "11"
dict_month ['Dec'] = "12"


base = "https://www.basketball-reference.com/boxscores/pbp/"
dates = []
start = []
visitor = []
pts_visitor = []
home = []
pts_home = []
ot = []
attendance = []
arena = []
game_id = []
game_urls = []
count = 0

for url in urls_to_browse:

    print (url)
    count += 1


    content=requests.get(url).text
    soup=BeautifulSoup(content, "lxml")

    pbp_table = soup.find("table", attrs={"id": "schedule"})
    pbp_rows=pbp_table.find_all("tr")

    for i in range (1, len (pbp_rows)):
        temp = pbp_rows[i].find_all("th")+pbp_rows[i].find_all("td")
        if (len(temp)<11):
            continue
        dates.append (temp[0].text)
        start.append (temp[1].text)
        visitor.append (temp[2].text)
        pts_visitor.append (temp[3].text)
        home.append (temp[4].text)
        pts_home.append (temp[5].text)
        ot.append (temp[7].text)
        attendance.append (temp[8].text)
        arena.append (temp[9].text)

        home_abbrev = dict [temp[4].text]
        date = temp[0].text.split (",")
        if (len(date[1].split(" ")[2])<2):
            date = date[2] + dict_month[date[1].split(" ")[1]] + "0" + date[1].split(" ")[2] +"0" + home_abbrev
        else:
            date = date[2] + dict_month[date[1].split(" ")[1]] + date[1].split(" ")[2] +"0" + home_abbrev
        date = date.strip ()
        game_id.append (date)
        game_url = base+date+".html"
        game_urls.append (game_url)

data = {'dates': dates, 'start': start, 'visitor': visitor, 'pts_visitor': pts_visitor, 
        'home': home, 'pts_home': pts_home, 'ot': ot, 'attendance': attendance, 'arena':arena, 
        'urls': game_urls, 'id': game_id}

df = pd.DataFrame(data)

df.to_csv ("game_schedule.csv", index = False)