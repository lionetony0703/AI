#!/usr/bin/env python
# coding: utf-8

# In[80]:



import requests
from bs4 import BeautifulSoup

url = 'https://www.chinatimes.com/?chdtv'
html = requests.get(url)
html.encoding="utf-8"
#print(html.text)

soup = BeautifulSoup(html.text,'html.parser')
#print(soup.find_all('h4'))

print('熱門新聞：')
hot = soup.find_all('h4',class_="title",limit = 7)
for title in hot:
    print('標題:',title.string)
    print('網址:',title.select_one('h4 a').get("href"),'\n')
    #select()所得到的內容為一list，跟find_all()一樣，所以若確定只有一個內容可以用select_one()。


# In[ ]:





# In[ ]:




