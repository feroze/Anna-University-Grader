#!/usr/bin/env python
"""
Anna University Grader -> Extracts grades from anna univ site

Improvement: Scraping grades to generate GPA, statistics

Feroze Naina
"""

from sqlite3 import *

f = open('table.html', 'w')
f.write('<html><table><style type="text/css">tr.heading { background-color: DarkOrange; }</style>')
f.write('<tr class="heading">')
f.write('<td>Regno</td>')
f.write('<td>Name</td>')
f.write('<td>English</td>')
f.write('<td>Maths</td>')
f.write('<td>Physics</td>')
f.write('<td>Chemistry</td>')
f.write('<td>EG</td>')
f.write('<td>FOCP</td>')
f.write('<td>CP Lab</td>')
f.write('<td>Engg Practice Lab</td>')
f.write('<td>GPA</td></tr>')

conn = connect('test.db')
curs = conn.cursor()

curs.execute("select * from eie")
for row in curs:
    f.write('<tr>')
    
    f.write('<td>'+row[0]+'</td>')
    f.write('<td>'+row[1]+'</td>')
    f.write('<td>'+row[2]+'</td>')
    f.write('<td>'+row[3]+'</td>')
    f.write('<td>'+row[4]+'</td>')
    f.write('<td>'+row[5]+'</td>')
    f.write('<td>'+row[6]+'</td>')
    f.write('<td>'+row[7]+'</td>')
    f.write('<td>'+row[8]+'</td>')
    f.write('<td>'+row[9]+'</td>')
    f.write('<td>'+str(row[18])+'</td>')
    
f.write('</tr></table></html>')

