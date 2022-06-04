import psycopg2
from psycopg2 import Error
import db_secrets

def postgres_info(connection):
    try:
        # Connection to an existing database 
        cursor = connection.cursor()
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        cursor.execute("SELECT version();")
        # Fetch result
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")  

connection = psycopg2.connect(
            user = db_secrets.user,
            password = db_secrets.password,
            host = db_secrets.host,
            port = db_secrets.port,
            database = db_secrets.database
        )


'''
Create table
'''        

def create_table(connection):
    try:    
        cursor = connection.cursor()
        # SQL query to create a new table
        create_table_query = '''CREATE TABLE mobile
            (ID INT PRIMARY KEY     NOT NULL,
            MODEL           TEXT    NOT NULL,
            PRICE         REAL); '''
        # Execute a command: this creates a new table
        cursor.execute(create_table_query)
        connection.commit()
        print("Table created successfully in PostgreSQL ")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

'''
CRUID OPERATION WITH PYTHON
'''

def crud(connection):
    try:
        cursor = connection.cursor()
        # Executing a SQL query to insert data into  table
        insert_query = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (1, 'Iphone12', 1100)"""
        cursor.execute(insert_query)
        connection.commit()
        print("1 Record inserted successfully")
        # Fetch result
        cursor.execute("SELECT * from mobile")
        record = cursor.fetchall()
        print("Result ", record)
        
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")



def main():
    #postgres_info(connection) 
    #create_table(connection)
    crud(connection)



if __name__ == '__main__':
    main()
   


