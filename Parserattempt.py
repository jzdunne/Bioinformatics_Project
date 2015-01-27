#!/usr/bin/python
#This is first parser attempt

infile = 'dataset.soft'
fh = open(infile)
line= fh.readline()
while line[:20] != '!datatset_table_begin':
    line=fh.readline().strip()

colnames={}

index=0
for title in header.split('\t'):
    colnames[title]=index
    print '%s\t%s'%(title,index)
    index=index+1



#opens output files, one per table
genefile=open('genes.txt', 'w')
expressionfile=open('expression.txt', 'w')
probefile=open('probes.txt', 'w')

genefileds=['Gene ID', 'Gene symbol', 'Gene title']
samples=header.split('\t')[2:int(colnames['Gene title'])]
probefields=['ID_REF','Gene ID']

def buildrow(row, fields):
	'''This function creates a row in a table'''
    newrow=[]
    for f in fields:
	newrow.append(row[int(colnames[f])])
    return "\t".join(newrow)+"\n"





