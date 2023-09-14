import pyodbc

def sql_query(sqlvar):
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()
    try:
       result = cur.execute(sqlvar)
    except Exception as e:
        print(e)
        result = None
    conn.commit()
    cur.close()
    return result



sqlqueryvar = "INSERT INTO salesperson (emp_no,first_name,last_name,dept_no,salary,sales_target,county,post_code,tel,notes) VALUES (70, 'Sarah','Hayden',2,40000,12000,'Kent','CT20 3SE','01234567890','Winging it!')"
insertresult = sql_query(sqlqueryvar)
print(insertresult)

