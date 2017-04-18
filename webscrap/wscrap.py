
# coding: utf-8

# In[54]:

import requests
from requests.auth import HTTPProxyAuth
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
from random import randint
import pandas as pd


# In[131]:

# auth = HTTPProxyAuth("username", "password")


# In[41]:

user_agent_list = ['Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
                   'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36',
                   'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 7.0; InfoPath.3; .NET CLR 3.1.40767; Trident/6.0; en-IN)',
                   'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0'
                  ]
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


# In[42]:

for i in range(1,10):
  rand_user_agent = randint(0,len(user_agent_list)-1)
  headers['User-Agent'] = user_agent_list[rand_user_agent]
  print(headers['User-Agent'])


# In[68]:

url = 'http://www.whoishostingthis.com/tools/user-agent/'
response = requests.get(url, headers=headers,auth=auth)
data = response.text
soup = BeautifulSoup(data,"lxml")
useragent = soup.find(attrs={"class":"info-box user-agent"})
ip = soup.find(attrs={"class":"info-box ip"})
print(useragent.text)
print(headers["User-Agent"])
print(ip.span.text)


# In[148]:

### Example Code for using Sessions
# s = requests.Session()
# s.get(url,headers=headers)
# print(s.cookies)
# r = s.post(url, data=payload,auth=auth,headers=headers,cookies=cookie)


# In[146]:

# Go to Chrome Developer Tools > Inspect > Network > Select Page > View Headers
# Get cookie info from  chrome://settings/cookies


cookie = {'session_name':'session','cookie_1': 'cookie_session_1'}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
           'header_2':'header_value_2'
          }


payload = {'input1':'value1',
           'input2': 'value2',
          }

r = requests.post(url, data=payload,auth=auth,headers=headers,cookies=cookie)

data = r.text
soup = BeautifulSoup(data,"lxml")
#Debug
r.request.headers
r.headers


# In[147]:

file = open("output.html","w") 
file.write(soup.prettify()) 
file.close() 
# soup


# In[2]:

url = "https://en.wikipedia.org/wiki/List_of_airports_by_IATA_code:_A"

# html = urlopen(search_url)
# bsObj = BeautifulSoup(html.read(),"lxml")
# page = bsObj.findAll("a",{"class":"page_no"})
# max = 0 
# for i in page:
#     page_no = int(i.get_text())
#     if (page_no > max):
#         max = page_no
# print(max)
# page.findAll("div")

page = urlopen(url).read()
soup = BeautifulSoup(page)

for tr in soup.find_all('tr')[2:]:
    tds = tr.find_all('td')
    print(tds[0].text, tds[2].text, tds[3].text)






