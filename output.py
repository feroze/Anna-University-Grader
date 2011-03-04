#!/usr/bin/env python
"""
Anna University Grader -> Extracts grades from anna univ site

Improvement: Scraping grades to generate GPA, statistics

Feroze Naina
"""

from sqlite3 import *
from BeautifulSoup import BeautifulSoup



def htmlprint(branch):
    f = open('temp.html', 'w')
    
    headers='''<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" lang="en"><head>




    <meta http-equiv="content-type" content="text/html">
    <title>Feroze.in - AUG</title>
    <style type="text/css" media="all">@import "style.css";</style>

    <script type="text/javascript">

    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-21763445-1']);
    _gaq.push(['_setDomainName', '.feroze.in']);
    _gaq.push(['_trackPageview']);
    
    (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();

    </script>

    </head><body>

    <div id="Header"><a href="http://feroze.in/aug/" title="AUG Home">Anna University Grader</a></div>

    <div id="Content">
    <h1> '''+branch+''' </h1>
    <p>
    
    <table>
    <style type="text/css">
    tr.heading { background-color: DarkOrange; }
    
    </style>
    
    <tr class="heading">
    <td align=center>Regno</ td>
    <td align=center>Name</ td>
    <td align=center>English</ td>
    <td align=center>Maths</ td>
    <td align=center>Physics</ td>
    <td align=center>Chem</ td>
    <td align=center>EG</ td>
    <td align=center>FOCP</ td>
    <td align=center>CP Lab</ td>
    <td align=center>EP Lab</ td>
    <td align=center>GPA</ td></ tr>'''
    
    f.write(headers)
    
    conn = connect('marks.db')
    curs = conn.cursor()
    
    curs.execute("select * from "+branch)
    for row in curs:
        f.write('<tr>')
        
        f.write('<td align=center>'+row[0]+'</ td>')
        f.write('<td align=center>'+row[1]+'</ td>')
        f.write('<td align=center>'+row[2]+'</ td>')
        f.write('<td align=center>'+row[3]+'</ td>')
        f.write('<td align=center>'+row[4]+'</ td>')
        f.write('<td align=center>'+row[5]+'</ td>')
        f.write('<td align=center>'+row[6]+'</ td>')
        f.write('<td align=center>'+row[7]+'</ td>')
        f.write('<td align=center>'+row[8]+'</ td>')
        f.write('<td align=center>'+row[9]+'</ td>')
        f.write('<td align=center>'+str(row[18])+'</ td>')
        f.write('</ tr>')
        
        
    
    f.write('''</ tr></ table></p>
    	
    </div>

    <div id="Menu">
    <a href="http://feroze.in/aug/index.html" title="Home">Home</a><br>
    <a href="http://feroze.in/aug/overall.html" title="Overall">Overall Results + Statistics</a><br>
    <a href="http://feroze.in/aug/EIE.html" title="EIE">EIE</a><br>
    <a href="http://feroze.in/aug/ECE.html" title="EIE">ECE</a><br>
    <a href="http://feroze.in/aug/EEE.html" title="EIE">EEE</a><br>
    <a href="http://feroze.in/aug/CSE.html" title="EIE">CSE</a><br>
    <a href="http://feroze.in/aug/IT.html" title="EIE">IT</a><br>
    <a href="http://feroze.in/aug/Mech.html" title="EIE">Mech</a><br>
    <a href="http://feroze.in/aug/Prod.html" title="EIE">Prod</a><br>
    <a href="http://feroze.in/aug/faq.html" title="FAQ">Frequently Asked Questions</a><br>
    <a href="http://feroze.in/aug/notes.html" title="">Notes</a><br>
    <a href="http://feroze.in/" title="Feroze.in">Visit Feroze.in</a><br>
    
    
    </body></html>''')
    f.close()
    
    i = open('temp.html', 'r')
    input=i.read()
    soup = BeautifulSoup(input)
    output=soup.prettify()
    o=open(branch+'.html', 'w')
    o.write(output)
    o.close()
    i.close()
    
htmlprint('EIE')
htmlprint('EEE')
htmlprint('ECE')
htmlprint('Mech')
htmlprint('Prod')
htmlprint('Civil')
htmlprint('CSE')
htmlprint('IT')

