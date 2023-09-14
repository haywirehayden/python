import pyodbc  

def sql_query(sqlvar):
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor() 
    result = cur.execute(sqlvar).fetchall()
    cur.close()
    return result


# Between example

sqlqueryvar = 'SELECT sales_target FROM dept WHERE sales_target BETWEEN 4.9999 AND 25.0001'

# Like Example

sqlqueryvar = "SELECT job_title, notes FROM contact WHERE job_title LIKE '%Acc'"

# Greater than example

sqlqueryvar = 'SELECT salary FROM salesperson WHERE salary > 13.0000'

# IN example

sqlqueryvar = "SELECT * FROM salesperson WHERE post_code IN ('NULL')"

# Equal example

sqlqueryvar = "SELECT * FROM salesperson WHERE post_code = 'NULL'"

resultvar = sql_query(sqlqueryvar)

for row in resultvar:
   print(row)