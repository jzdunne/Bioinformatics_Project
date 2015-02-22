#!/usr/local/bin/python
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
print "<html><head><TITLE>CGI script output</TITLE></head>"
print "<body><H1>Form values</H1>"
print "<table><tr><th>Key</th><th>Value</th></tr>"

if 'name' in form:
        print "<tr><td>name</td><td>%s</td></tr>"% form['name'].value
else:
	print "name not found"
print "<table>"

print "</body></html>"
