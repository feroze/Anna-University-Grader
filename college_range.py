from decimal import *
import urllib3
from BeautifulSoup import BeautifulSoup
import sqlite3
import base64
import os
  
 
num=1027100
   
flag=0
while(not flag):
    regno= str(num)
    URL="http://www1.annatech.ac.in/result/index.php?regno="+ base64.encodestring(str(regno))
    http_pool = urllib3.connection_from_url(URL)
    page=http_pool.post_url(URL)
    #print page.data
    
    #Beautiful Soup Start
    soup=BeautifulSoup(page.data)
    
    #Extract roll, name, branch
    bio = soup.findAll('strong')
    try:
        x=bio[2].renderContents()
        
    except IndexError:
        print "GOtcha"
        flag=1

    print num
    num=num+50
    
if (flag):
    print "No is"
    print num
    