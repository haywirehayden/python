import pyodbc  

def sql_query(sqlvar):
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor() 
    result = cur.execute(sqlvar).fetchall()
    cur.close()
    return result


# Between example

betweenvar = 'SELECT sales_target FROM dept WHERE sales_target BETWEEN 4.9999 AND 25.0001'

resultvar = sql_query(betweenvar)

for row in resultvar:
    print(row)

# Like Example

likevar = "SELECT job_title, notes FROM contact WHERE job_title LIKE '%Acc'"

resultvar = sql_query(likevar)

for row in resultvar:
    print(row)

# Greater than example

greatervar = 'SELECT salary FROM salesperson WHERE salary > 13.0000'

resultvar = sql_query(greatervar)

for row in resultvar:
    print(row)

# IN example

invar = "SELECT * FROM salesperson WHERE post_code IN ('NULL')"

resultvar = sql_query(invar)

for row in resultvar:
   print(row)

# Equal example

equalvar = "SELECT * FROM salesperson WHERE post_code IN ('NULL')"

resultvar = sql_query(equalvar)

for row in resultvar:
   print(row)