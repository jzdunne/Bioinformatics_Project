import MySQLdb

class DBHandler():
  '''Database connection'''
  connection=None
  dbname='jzdunne'
  dbuser='jzdunne'
  dbpassword='PxFPTOvk'
  def __init___(self):
  '''initialising Database'''
   if DBHandler.connection == None:
       DBHandler.connection = MySQLdb.connect(db=DBHandler.dbname, user=DBHandler.dbuser, passwd=DBHandler.dbpassword)
  def cursor(self):
    return DBHandler.connection.cursor()


class Gene():
  '''A class that describes a gene'''
  accession=''
  description=''
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
    cursor.execute(probessql,(ID_REF))
    for result in cursor.fetchall():
      self.probelist.append(result[0])
  def get_expression(self, ID_REF):
    '''Gets expression value for the Gene'''
    db=DBHandler()
    cursor=db.cursor()
    sql='select Sample_ID, expression_value from expression where ID_REF=%s'
    cursor.execute(sql,(ID_REF))
    for result in cursor.fetchone():
      self.Sample_ID=result[0]
      self.expression_value=result[1]


print("Done!")

  
