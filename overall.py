#!/usr/bin/env python
"""
Anna University Grader -> Extracts grades from anna univ site

Improvement: Scraping grades to generate GPA, statistics

Feroze Naina
"""

from sqlite3 import *
from BeautifulSoup import BeautifulSoup

f = open('temp.html', 'w')

headers='''
<h1> Overall Results + Statistics </h1>
<p>'''

f.write(headers)

def branchwise(branch):
    conn = connect('marks.db')
    curs = conn.cursor()
        
    #branch
    f.write('''<table>
    <style type="text/css">
    tr.heading { background-color: DarkOrange; }
    </style><b>'''+
    branch+ '''</b><br /><br />  <i>Toppers</i><tr class="heading">
    <td align=center>Regno</ td>
    <td align=center>Name</ td>
    <td align=center>GPA</ td></ tr>''')

    

    curs.execute("SELECT roll,name,GPA FROM "+branch+" ORDER BY GPA DESC LIMIT 0,5")
    for row in curs:
        f.write('<tr>')        
        f.write('<td align=center>'+row[0]+'</ td>')
        f.write('<td align=center>'+row[1]+'</ td>')
        f.write('<td align=center>'+str(row[2])+'</ td>')
        f.write('</ tr>')
    
    
    #GPA Stats
    f.write('''<table>
    <style type="text/css">
    tr.heading { background-color: DarkOrange; }
    </style><b></b><br /><br />  <i>GPA Stats</i>
    <tr class="heading">
    <td align=center>Highest</ td>
    <td align=center>Average</ td>
    <td align=center>Lowest</ td></ tr><tr>''')
    
    #max
    curs.execute("SELECT MAX(GPA) FROM "+branch)
    for max in curs:
        f.write('<td align=center>'+str(max[0])+'</ td>')
    
    #avg
    curs.execute("SELECT AVG(GPA) FROM "+branch)
    for avg in curs:
        f.write('<td align=center>'+str(avg[0])+'</ td>')
    
    #min
    curs.execute("SELECT MIN(GPA) FROM "+branch)
    for min in curs:
        f.write('<td align=center>'+str(min[0])+'</ td>')
    
    f.write('</ tr></table><br /><br /><br />')
    conn.close()
    
def overall():
    conn = connect('marks.db')
    curs = conn.cursor()
    
    #coll toppers
    #Top 10 nerds
    f.write('''<table>
    <style type="text/css">
    tr.heading { background-color: DarkOrange; }
    </style><b>College Overall </b><br /><br />  <i>TOP 10 NERDS</i>
    <tr class="heading">
    <td align=center>Regno</ td>
    <td align=center>Name</ td>
    <td align=center>GPA</ td></ tr>''')
    
    curs.execute("SELECT roll,name,GPA FROM overall ORDER BY GPA DESC LIMIT 0,10")
    for row in curs:
        f.write('<tr>')        
        f.write('<td align=center>'+row[0]+'</ td>')
        f.write('<td align=center>'+row[1]+'</ td>')
        f.write('<td align=center>'+str(row[2])+'</ td>')
    
    #GPA Stats
    f.write('''<table>
    <style type="text/css">
    tr.heading { background-color: DarkOrange; }
    </style><b></b><br /><br />  <i>GPA Stats</i>
    <tr class="heading">
    <td align=center>Highest</ td>
    <td align=center>Average</ td>
    <td align=center>Lowest</ td></ tr><tr>''')
    
    
    #max
    curs.execute("SELECT MAX(GPA) FROM overall")
    for max in curs:
        f.write('<td align=center>'+ str(max[0])+'</ td>')
    #avg
    curs.execute("SELECT AVG(GPA) FROM overall")
    for avg in curs:
        f.write('<td align=center>'+ str(avg[0])+'</ td>')
    #min
    curs.execute("SELECT MIN(GPA) FROM overall")
    for min in curs:
        f.write('<td align=center>'+ str(min[0])+'</ td>')
        
    f.write('</ tr></table><br /><br /><br />')
    conn.close()

overall()
    
branchwise('EIE')
branchwise('ECE')
branchwise('EEE')
branchwise('CSE')
branchwise('IT')
branchwise('Civil')
branchwise('Mech')
branchwise('Prod')



f.close()
    
i = open('temp.html', 'r')
input=i.read()
soup = BeautifulSoup(input)
output=soup.prettify()
o=open('overalltemp.html', 'w')
o.write(output)
o.close()
i.close()
