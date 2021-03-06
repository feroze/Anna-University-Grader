#!/usr/bin/env python
"""
Anna University Grader -> Extracts grades from anna univ site

TODO:   Better branch wise statistics
        Other college data
        Implement on Django-non-rel on GAE to handle traffic

Feroze Naina
"""

from decimal import *
import urllib3
from BeautifulSoup import BeautifulSoup
import sqlite3
import base64
import os

mydb_path = 'test.db'




#Grade -> Mark Converter
def marker(grade):
    if grade == 'S':
        return 10
    elif grade == 'A':
        return 9
    elif grade == 'B':
        return 8
    elif grade == 'C':
        return 7
    elif grade == 'D':
        return 6
    elif grade == 'E':
        return 5
    else:
        return 0
    

    
def scraper(first,last,table_name):
    #Check if db exists
    #print "Enter table name"
    #table_name=str(raw_input())
    create_table='''create table ''' +table_name+ ''' (roll text, name text,
    g186101 text, g181101 text, g182101 text, g183101 text,
    g185101 text, g186102 text,g186151 text, g186152 text,
    m186101 integer, m181101 integer, m182101 integer, m183101 integer,
    m185101 integer, m186102 integer,m186151 integer,
    m186152 integer, GPA integer)'''
   
    if not os.path.exists(mydb_path):
        #create new DB, create table
        conn = sqlite3.connect(mydb_path)
        conn.execute(create_table)
    else:
        #use existing DB
        conn = sqlite3.connect(mydb_path)
        #conn.execute(create_table)
    
    for i in range (first,last+1):
        regno= str(i)
        URL="http://www1.annatech.ac.in/result/index.php?regno="+ base64.encodestring(str(regno))
        http_pool = urllib3.connection_from_url(URL)
        page=http_pool.post_url(URL)
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
        
        grades=[]
        for arr in range(0,8):
            grades.append(results[arr+2].renderContents())
        
        
        """ This is seriously FAIL method
        g186101=results[2].renderContents()
        g181101=results[3].renderContents()
        g182101=results[4].renderContents()
        g183101=results[5].renderContents()
        g185101=results[6].renderContents()
        g185102=results[7].renderContents()
        g185151=results[8].renderContents()
        g185152=results[9].renderContents()"""
        
        
        print roll ," - ", name
        print branch
        """for sub in grades:
            print sub"""
     
       
        """ This is seriously FAIL method
        print g186101
        print g181101
        print g182101
        print g183101
        print g185101
        print g185102
        print g185151
        print g185152"""
        
        #Convert grades to marks
        credits=26
        marks=[]
        
        for arr in grades:
            marks.append(marker(arr))
        
        """for arr in marks:
            print arr"""
            
        #Reduces Total Credit for arrears
        if marks[0]==0:
            credits=credits-4
        if marks[1]==0:
            credits=credits-4
        if marks[2]==0:
            credits=credits-3
        if marks[3]==0:
            credits=credits-3
        if marks[4]==0:
            credits=credits-5
        if marks[5]==0:
            credits=credits-3
        if marks[6]==0:
            credits=credits-2
        if marks[7]==0:
            credits=credits-2
            
        
        total=(marks[0]*4)+(marks[1]*4)+(marks[2]*3)+(marks[3]*3)+(marks[4]*5)+(marks[5]*3)+(marks[6]*2)+(marks[7]*2)
        getcontext().prec=3 #For precision :|
        #if credits==0:
        #    pass
        _gpa=Decimal(total)/Decimal(credits)
        gpa=_gpa
        
        
        #Sqlite insert
        t=[roll,name] #list
        for arr in grades:
            t.append(arr)
            
        for arr in marks:
            t.append(arr)
            
        t.append(float(gpa))
        #print t
        tuple(t)
        
        conn.execute('insert into '+table_name+' values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',t)
        conn.commit()
        


#scraper(1027694,1027695,'EIE') #Arrear test

scraper(1027171,1027286,'Civil') #Civil
scraper(1027287,1027402,'Mech') #Mech
scraper(1027403,1027462,'Prod') #Prod
scraper(1027463,1027580,'EEE') #EEE
scraper(1027581,1027698,'EIE')#EIE
scraper(1027699,1027817,'IT') #IT
scraper(1027818,1027933,'CSE') #CSE
scraper(1027934,1028000,'ECE') #ECE -> 1028001 is absent for all . Left college.
scraper(1028002,1028049,'ECE') #ECE

