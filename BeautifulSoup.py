#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

url = 'https://www.transfermarkt.co.uk/'

r = requests.get(url, headers=headers)
r.status_code


# In[5]:


html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


# In[7]:


from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')


# In[8]:


soup.p


# In[9]:


soup.find('p')


# In[11]:


soup.find('a')['href']
soup.a['href']


# In[10]:


soup.find('a').text
soup.find('a').get_text()


# In[12]:


soup.find_all('a')


# In[13]:


soup.find_all('a')[1]


# In[15]:


a_list=soup.find_all('a')
for i in a_list:
    print(i['href'])


# In[16]:


a_list=soup.find_all('a')
for i in a_list:
    print(i.text)


# In[24]:


soup.find_all('a', class_='sister')
soup.find_all('a', {'class':'sister'})


# In[18]:


soup.find_all('a', id='link3')


# In[19]:


soup.find_all('a',{'id':'link3'})

