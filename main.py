#!/usr/bin/env python

import urllib3
from BeautifulSoup import BeautifulSoup
import sqlite3


    

regno= 1027606

URL="http://www1.annatech.ac.in/result/index.php?regno=MTAyNzYwNg=="
http_pool = urllib3.connection_from_url(URL)
fields = {'regnum':regno,'Submit':'Submit'}
page=http_pool.post_url(URL,fields)
#print page.data

soup=BeautifulSoup(page.data)
results = soup.findAll('span', attrs={'style' : "font-weight:bold;color:#003366;"})

roll=results[0].renderContents()
name=results[1].renderContents()
print roll ," - ", name




