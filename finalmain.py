#!C:\Python27\python.exe

import sqlite3
import cgi

conn=sqlite3.connect('final.db')
form=cgi.FieldStorage()

valid=0

username=form.getvalue('username')
password=form.getvalue('password')

cursor=conn.execute("SELECT * FROM LOGIN")
for row in cursor:
	if(username==row[0] and password==row[1]):
		valid=1

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<body>"

if(valid==1):
	print "Hello, ",username

	print "<form action='result.py' method='POST'>"
	print "<input type='submit' value='submit'>"
	print "</form>"

elif(valid==0):
	print "Login Unsuccessfull"


print "</body>"
print "</html>"