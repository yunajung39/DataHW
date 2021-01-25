#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


# In[3]:


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

url = 'https://www.transfermarkt.co.uk/spieler-statistik/wertvollstespieler/marktwertetop'

r = requests.get(url, headers=headers)
r.status_code


# In[4]:


soup = BeautifulSoup(r.content, 'html.parser')
print(soup)


# In[7]:


player_info=soup.find_all('tr', class_=['odd','even'])


# In[9]:


print(player_info[0])
print(len(player_info))


# In[33]:


number=[]
name=[]
position=[]
age=[]
nation=[]
team=[]
value=[]


# In[34]:


for info in player_info:
    player=info.find_all('td')
    #print(player)
    #print(player[0])
    
    number.append(player[0].text)
    name.append(player[3].text)
    position.append(player[4].text)
    age.append(player[5].text)
    nation.append(player[6].img['alt'])
    team.append(player[7].img['alt'])
    value.append(player[8].text.strip())


# In[35]:


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


# In[36]:


df.to_csv('transfermarket25.csv', index=False)


# In[ ]:





# In[ ]:





# In[ ]:




