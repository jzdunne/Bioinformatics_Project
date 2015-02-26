#creates classes
import MySQLdb

class DBHandler():
  '''Database connection'''
  connection=None
  dbname='jzdunne'
  dbuser='jzdunne'
  dbpassword='PxFPTOvk'

  def __init__(self):
    '''initialising Database'''
    if DBHandler.connection == None:
       DBHandler.connection = MySQLdb.connect(db=DBHandler.dbname, user=DBHandler.dbuser, passwd=DBHandler.dbpassword)

  def cursor(self):
    return DBHandler.connection.cursor()


class Gene():
  '''A class that describes a gene'''
  Accession=''
  Description=''
  Gene_ID=''
  probeslist=[]
  def __init__(self, Gene_ID):
    '''Init method for gene'''
    db=DBHandler()
    self.Gene_ID=Gene_ID
    cursor=db.cursor()
    sql='select Accession, Description from gene_info where Gene_ID=%s'
    cursor.execute(sql,(Gene_ID))
    # this has queried database
    # next step gets result and populates the class fields
    result=cursor.fetchone()
    self.Accession=result[0]
    self.Description=result[1]
    #now fetch the probes..
    probesql='select ID_REF from probes where Gene_ID=%s'
    cursor.execute(probesql,(Gene_ID))
    for result in cursor.fetchall():
      self.probeslist.append(result[0])
  def get_expression(self):
    '''Gets expression value for the Gene'''
    db=DBHandler()
    cursor=db.cursor()
    expsql='select sum(expression_value)/count(expression_value) from expression where ID_REF=%s'
    cursor.execute(expsql,(probeslist[0]))
    result=cursor.fetchall()
    for result in cursor:
      self.expression_value.append(result[0])
   #this final definition does not yet work, requires examining to fix however rest of class works
print("classes.py imported")

  
