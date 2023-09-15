import pyodbc
import csv

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

#createtablequery = "CREATE TABLE Student ( StudentID int PRIMARY KEY, FirstName varchar(40) NOT NULL, Surname varchar(30), Course varchar(30), City varchar(15) )"

#sql_query(createtablequery)

#with open('Student.csv') as student_file:
#    csv_reader = csv.reader(student_file)
#    for row in csv_reader:


#        insertrows = ["INSERT INTO Student (StudentID, FirstName, Surname ,Course, City) VALUES ('1','Noah','Smith','Chemical Engineering','Nottingham')",
#                     "INSERT INTO Student (StudentID, FirstName, Surname, Course, City) VALUES ('2','Olivia','Jones','Architecture','Cambridge')",
#                     "INSERT INTO Student (StudentID, FirstName, Surname, Course, City) VALUES ('3','Arthur','Taylor','Archaeology','Birmingham')",
#                     "INSERT INTO Student (StudentID, FirstName, Surname, Course, City) VALUES ('4',Ivy','Jackson','Civil Engineering','Coventry')",
#                     "INSERT INTO Student (StudentID, FirstName, Surname, Course, City) VALUES ('5','Muhammad','Wilson','Financial accounting','Oxford')"]
#for i in insertrows:
#    sql_query(i)



# work in progress

student_list = []

with open('Student.csv') as student_file:
    student_data = student_file.readlines()
    student_file.close()
    print(student_data)

    for line in student_data:
        students = line.split(",")
        print(students)
        student_list.append(students)

    for students in student_list:
        sqlquery = "INSERT INTO Student (StudentID, FirstName, Surname ,Course, City) VALUES ("+,student_list[0][0]"+, ",student_list[0][1]",",student_list[0][2]",",student_list[0][3]",",student_list[0][4]", ")
        print(sqlquery)


updaterows = "UPDATE Student SET Course = 'Computer Science' WHERE StudentID = 5"

sql_query(updaterows)


