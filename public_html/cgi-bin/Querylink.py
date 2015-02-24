#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
import MySQLdb
sql="SELECT Accession, Description FROM gene_info where Gene_id= %s"
db=MySQLdb.connect(db='jzdunne', user='jzdunne', passwd='PxFPTOvk')
cursor=db.cursor()
cursor.execute(sql,form[''].value)
result=cursor.fetchall()
result

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
print "<html><head><TITLE>Sample Information</TITLE></head>"
print "<body><H1>Sample Information</H1>"
print result
print "<table><tr><th></th><th>Gene_ID</th><th>Gene Symbol</th><th>Gene title</th></tr>"

for k in form.keys():
  

        print "<tr><td>%s</td><td>%s</td></tr>"%(k, form[k].value)

print "<table>"


print "</body></html>"

