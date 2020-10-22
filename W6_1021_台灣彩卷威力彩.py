#!/usr/bin/env python
# coding: utf-8

# In[21]:


# Lottery number
# 大樂透頭獎號碼擷取

import requests
from bs4 import BeautifulSoup

url = 'http://www.taiwanlottery.com.tw/'
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')
#print(sp.prettify())
data1 = sp.select("#rightdown")
#print(data1)

data2 = data1[0].find_all('div', {'class':'contents_box02'})
#print(data2)

data3 = data2[2].find_all('div', {'class':'ball_tx ball_yellow'})
#print(data3)

print("開出順序：",end="")
for n in range(0,6):
    print(data3[n].text,end="  ") 

print("\n大小順序：",end="")    
for n in range(6,len(data3)):
    print(data3[n].text,end="  ")
     
## 第二區
red = data2[2].find('div', {'class':'ball_red'})        
print("\n第二區：{}".format(red.text)) 


# In[ ]:





# In[ ]:




