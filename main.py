#!/usr/bin/env python

import urllib3
from BeautifulSoup import BeautifulSoup
import sqlite3


    

regno= 1027606

URL="http://www1.annatech.ac.in/result/index.php?regno=MTAyNzYwNg=="
http_pool = urllib3.connection_from_url(URL)
fields = {'regnum':regno,'Submit':'Submit'}
page=http_pool.post_url(URL,fields)
print page.data




