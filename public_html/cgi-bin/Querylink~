import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
print "<html><head><TITLE>Sample Information</TITLE></head>"
print "<body><H1>Sample Information</H1>"
print "<table><tr><th>Gene ID</th><th>Gene Symbol</th><th>Gene title</th></tr>"

for k in form.keys():
        print "<tr><td>%s</td><td>%s</td></tr>"%(k, form[k].value)

print "<table>"

print "</body></html>"
