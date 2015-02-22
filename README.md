This is the repository for the code that establishes a webpage and a database it communicates with to provide information on the data from a study analysing the rectal epithelia of Cystic Fibrosis sufferers to identify gene expression.
'Cystic Fibrosis: rectal epithelia' is a dataset which was downloaded from GEO. This can be found under 'dataset.soft'.
A parser was written using python to extract the data into 3 files. This code is contained in the file 'my_parser_template.py'.
From the 3 datafiles (genes.txt, probes.txt and expression.txt), a fourth file was created (samples.txt).
These 4 files were put into tables using MySQL and these tables were all linked forming a database. The code for this is in the file 'SQL_table_code'.
The folder public_html contains another; cgi-bin, and it is this that contains the code for the webpage (final_webpage.html) and the CGI forms linking the website to the database.
