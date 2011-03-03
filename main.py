#!/usr/bin/env python
"""
Anna University Grader -> Extracts grades from anna univ site

Improvement: Scraping grades to generate GPA, statistics

Feroze Naina
"""


import urllib3, urllib2, urllib
from BeautifulSoup import BeautifulSoup
import sqlite3
import base64


    

regno= 1027655


URL="http://www1.annatech.ac.in/result/index.php?regno="+ base64.encodestring(str(regno))
http_pool = urllib3.connection_from_url(URL)
fields = {'regnum':'1027655','Submit':'Submit'}
page=http_pool.post_url(URL,fields)
#print page.data

#Beautiful Soup Start
soup=BeautifulSoup(page.data)

#Extract roll, name, branch
bio = soup.findAll('span', attrs={'style' : "font-weight:bold;color:#003366;"})
roll=bio[0].renderContents()
name=bio[1].renderContents()

degree = soup.findAll('strong')
branch=degree[3].renderContents()

#Extract grades
results=soup.findAll('div', attrs={'align':"center"})


g186101=results[2].renderContents()
g181101=results[3].renderContents()
g182101=results[4].renderContents()
g183101=results[5].renderContents()
g185101=results[6].renderContents()
g185102=results[7].renderContents()
g185151=results[8].renderContents()
g185152=results[9].renderContents()


print roll ," - ", name
print branch
print g186101
print g181101
print g182101
print g183101
print g185101
print g185102
print g185151
print g185152