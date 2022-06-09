
import psycopg2
from pprint import pprint
import time
import json 
from pathlib import Path

'''
import psycopg2
'''

'''
We are using a Psycopg2 to connect to rds postgres database.
Intension.: 
          Perform CRUD OPERATION. 
          LIKE CREATE TABLES. 
          READ TABLES 
          UPDATE TABLES 
          DELETE TABLES

Requirement to connect to postgres database using python. 
user: 
database name: 
password: 
database posrt: 
database host name(endpoint): 
'''

# connection 
# SQL 
'''
connection = psycopg2.connect(
        user = "python",
        password = "admin",
        host = "localhost",
        port = "5432",
        database = "kojitechs"
    )
'''
# Connection info
'''
with psycopg2.connect(user = "python", password = "admin",host = "localhost",port = "5432", database = "kojitechs") as connection:
    cursor = connection.cursor()
    print("Print postgres server infomation")
    print(connection.get_dsn_parameters(), "\n")
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")
'''

# Create a database table using python. 

'''
create table (SQL){
    TABLE_NAME = "kojitechs"
    CREATE TABLE kojitechs
    (ID, INT PRIMARY KEY NOT NULL
    FIRST_NAME TEXT NOT NULL 
    LAST_NAME TEXT NOT NULL 
    PRICE REAL);
}
'''

'''
with psycopg2.connect(user = "python", password = "admin",host = "localhost",port = "5432", database = "kojitechs") as connection:
    cursor = connection.cursor()
    print("Creating table in my database")
    time.sleep(4)
    create_table =  CREATE TABLE kojitechs
        (ID INT PRIMARY KEY    NOT NULL,
        FIRST_NAME  TEXT NOT NULL ,
        LAST_NAME   TEXT NOT NULL,
        PRICE   REAL);
    cursor.execute(create_table)
    connection.commit()
    print("Table create succufully in PostgreSQL.")

'''

# creating table
"""
with psycopg2.connect(user = "python", password = "admin",host = "localhost",port = "5432", database = "kojitechs") as connection:
    cursor = connection.cursor()
    print("Creating table in my database")
    time.sleep(4)
    student_table = '''CREATE TABLE students
        (ID INT PRIMARY KEY    NOT NULL,
        STUT_NAME  TEXT NOT NULL ,
        Email   TEXT NOT NULL,
        Phone_Number   TEXT NOT NULL,
        STUT_ADD TEXT NOT NULL,
        STUT_APP TEXT NOT NULL,
        zip INT NOT NULL,
        Amount_paid REAL NOT NULL,
        PaidFull bool NULL); '''
    cursor.execute(student_table)
    connection.commit()
    print("Table create succufully in PostgreSQL.")
"""

students = json.loads(Path("stundentinfo.json").read_text())

# Insert in a table
"""
with psycopg2.connect(user = "python", password = "admin",host = "localhost",port = "5432", database = "kojitechs") as connection:
    cursor = connection.cursor()
    print("Inserting data to postgres database")
    time.sleep(4)
    command = "INSERT INTO students VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    for student in students:
        cursor.execute(command, tuple(student.values()))
    connection.commit()
    print("Insert succuful in PostgreSQL.")
"""


# READING A DATABASE TABLE
"""
with psycopg2.connect(user = "python", password = "admin",host = "localhost",port = "5432", database = "second_project=#") as connection:
    cursor = connection.cursor()
    time.sleep(4)
    command = "SELECT * FROM students"
    cursor.execute(command)
    datas= cursor.fetchall()
    for data in datas:
        print(data)
"""

with psycopg2.connect(user = "python", password = "admin",host = "localhost",port = "5432", database = "second_project") as connection:
    cursor = connection.cursor()
    print("reading table")
    time.sleep(4)  
    command = "SELECT * FROM students_studentinfo"
    cursor.execute(command)
    datas= cursor.fetchall()
    for data in datas:
        print(data)
    

