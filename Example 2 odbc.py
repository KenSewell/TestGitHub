
from pyodbc import *

cnxn = connect('DSN=McK_v3')
cursor = cnxn.cursor()
cursor.execute("select * from dbo.OKProperty_view")
# fetchall() returns a list of row objects
# but keeps all the rows in memory
rows = cursor.fetchall()
for row in rows:
    print row.PropCode, row.PropName
    
cursor.close()
cnxn.close()
