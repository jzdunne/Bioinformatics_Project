import MySQLdb
class DBHandler():
  '''Database connection'''
  connection=None
  dbname='jzdunne'
  dbuser='jzdunne'
  dbpassword='PxFPTOvk'
  def __init___(self):
   if DBHandler.connection == None:
    DBHandler.connection = MySQLdb.connect(db=DBHandler.dbname, user=DBHandler.dbuser, passwd=DBHandler.dbpassword)
  def cursor(self):
    return DBHandler.connection.cursor()


class Gene():
  '''A class that describes a gene'''
  accession=''
  description=''
  gene_id=''
  probeslist=[]
  def __init__(self, geneid):
    '''Init method for gene'''
    self.Gene_ID=geneid
    db=DBHandler()
    cursor=db.cursor()
    sql='select Accession, Description from gene_info where Gene_ID=%s'
    cursor.execute(sql,(geneid))
    # this has queried database
    # next step gets result and populates the class fields
    result=cursor.fetchone()
    self.gene_title=result[0]
    self.gene_symbol=result[1]
    #now fetch the probes..
    probesql='select ID_REF from probes where geneid=%s'
    cursor.execute(probessql, (result))
    for result in cursor.fetchall():
      self.probelist.append(result[0])
  
