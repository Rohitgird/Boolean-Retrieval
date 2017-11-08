#!C:\Python27

import sqlite3
import cgi

conn=sqlite3.connect('final.db')
form=cgi.FieldStorage()


print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<body>"
print "<form action='result.py' method='POST'>"
print "<select name='sel'>"
print "<option value='Jio'>Jio</option>"
print "<option value='Airtel'>Airtel</option>"
print "<option value='Reliance'>Reliance</option>"
print "</select>"
print "<input type='submit' value='submit'>"
print "</form>"

if(form.getvalue('sel')=="Airtel"):
	cursor=conn.execute("SELECT COUNT(PLAN) FROM DATA WHERE PLAN='AIRTEL'")

if(form.getvalue('sel')=="Reliance"):
	cursor=conn.execute("SELECT COUNT(PLAN) FROM DATA WHERE PLAN='RELIANCE'")

if(form.getvalue('sel')=="Jio"):
	cursor=conn.execute("SELECT COUNT(PLAN) FROM DATA WHERE PLAN='JIO'")

for row in cursor:
	print row[0], ' ', row[1]


print "</body>"
print "</html>"