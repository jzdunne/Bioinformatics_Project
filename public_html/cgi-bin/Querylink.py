#!/usr/bin/python
import cgi #imports cgi module so HTML form can interact with database
import cgitb
cgitb.enable()

form = cgi.FieldStorage()#stores information submitted to the form
import MySQLdb #imports SQL database so it can be queried
sql="SELECT Accession, Description FROM gene_info where Gene_id= %s" #SQL query
db=MySQLdb.connect(db='jzdunne', user='jzdunne', passwd='PxFPTOvk') #establish SQL connection
cursor=db.cursor() #establish cursor
cursor.execute(sql,form[''].value) #cursor carries out query using form value ('' is the name of the form)
result=cursor.fetchall() #fetches results
result
#second and third query to establish results of experiment
exprsql="SELECT sum(expression_value)/count(expression_value)FROM sample INNER JOIN expression ON sample.Sample_ID=expression.Sample_ID JOIN probes ON expression.ID_REF=probes.ID_REF WHERE Gene_id= %s AND subset=' CF'" 
db=MySQLdb.connect(db='jzdunne', user='jzdunne', passwd='PxFPTOvk') #establish SQL connection
cursor=db.cursor() #establish cursor
cursor.execute(exprsql,form[''].value)
exprresult=cursor.fetchall()
exprresult
NCFsql="SELECT sum(expression_value)/count(expression_value)FROM sample INNER JOIN expression ON sample.Sample_ID=expression.Sample_ID JOIN probes ON expression.ID_REF=probes.ID_REF WHERE Gene_id= %s AND subset=' non-CF'" 
cursor.execute(NCFsql,form[''].value)
NCFresult=cursor.fetchall()
NCFresult

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
print "<html><head><TITLE>Sample Information</TITLE></head>"
print "<body><H1>Sample Information</H1>"
print "<b>Gene ID:      </b>"
#above is HTML creating the page layout
for k in form.keys():
   print "<tr><td>%s</td><td>%s</td></tr>"%(k, form[k].value) #prints value submitted to form

print "<table>"
print "<b>          Gene Symbol, Gene Title:</b>"
print result
print "<p><b>Average Expression Value of Gene Over Cystic Fibrosis Patients</b></p>"
print exprresult
print "<p><b>Average Expression Value of Gene Over non-Cystic Fibrosis Patients</b></p>"
print NCFresult
#all results printed on the page
print "</body></html>"

