#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

number=[]
name=[]
position=[]
age=[]
nation=[]
team=[]
value=[]
    
for i in range(1,3):

    url = f'https://www.transfermarkt.co.uk/spieler-statistik/wertvollstespieler/marktwertetop?ajax=yw1&page={i}'

    r = requests.get(url, headers=headers)
    r.status_code

    soup = BeautifulSoup(r.content, 'html.parser')

    player_info=soup.find_all('tr', class_=['odd','even'])


    for info in player_info:
        player=info.find_all('td')

        number.append(player[0].text)
        name.append(player[3].text)
        position.append(player[4].text)
        age.append(player[5].text)
        nation.append(player[6].img['alt'])
        team.append(player[7].img['alt'])
        value.append(player[8].text.strip())
        
    time.sleep(1)

df=pd.DataFrame(
        {'number':number,
        'name':name,
        'position':position,
        'age':age,
        "nation":nation,
        'team':team,
        'value':value}
    )
df

    #df.to_csv('transfermarket25.csv', index=False)


# In[4]:


df.to_csv('transfermarket50.csv', index=False)


# In[ ]:




