import mysql.connector

# Dictionary to map common data types to MySQL data types
datatypes = {
    'string': 'varchar',
    'integer': 'integer',
    'float': 'float',
    'date':'date'
}

# Update the following lines with your MySQL connection details
# You need to provide the appropriate host, user, and password
# host = 'localhost'  # Change this to your MySQL host
# user = 'root'       # Change this to your MySQL username
# password = 'your_password'  # Change this to your MySQL password

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Shubham00@#'
)

# Create a cursor to interact with the database
cursor = db.cursor()

# Main class containing database operations
class Main:
    def __init__(self):
        pass

    def create_database(self, name: str): # creates a database
        try:
            cursor.execute(f'CREATE DATABASE {name}')
            db.commit()
            return True
        except:
            return False

    def create_table(self, database_name: str, table_name: str):  # creates a table in the provided database
        values = {}
        column_num = int(input("Enter Number of Columns:"))

        for i in range(column_num):
            column_name = input(f'Enter Column name:')
            datatype = str(input('Enter datatype:')).lower()
            limit = int(input('Enter Limit:'))
            values[column_name] = [datatypes.get(datatype, 'varchar'), limit]

        try:
            cursor.execute(f'USE {database_name}')
            columns = ', '.join(f"{column} {data[0]}({data[1]})" for column, data in values.items())
            cursor.execute(f'CREATE TABLE {table_name} ({columns})')
            db.commit()
            return True
        
        except Exception as e:
            print("Error:", e)
            return False
    
    def insert_table(self,database_name:str,table_name:str,k:tuple):   # Inserts values into the given table
        try:
            cursor.execute(f'USE {database_name}')
            query = f'INSERT INTO {table_name} VALUES {k}'
            cursor.execute(query)
            db.commit()
            print("Data inserted successfully.")
        
        except Exception as error:
            print(f'Error : {error}')

    def show_table_content(self,database_name:str,table_name:str,column_names = '*'):  # Shows the content present in the table
        cursor.execute(f' USE {database_name}')
        cursor.execute(f'SELECT {column_names} FROM {table_name}')
        rows = cursor.fetchall()
        return rows

    def get_table_header(self,database_name:str,table_name: str):   # Retrieve the column names (header) of a specified table in a given database
        try:
            cursor.execute(f'USE {database_name}')
            cursor.execute(f'SELECT * FROM {table_name} LIMIT 1')

            # Use the description attribute to get the header (column names) of the table
            header = [column[0] for column in cursor.description]
            return header

        except Exception as e:
            print("Error:", e)
            return None
        
    def delete_table_data(self,database_name:str,table_name:str,condition:str = ''): # Deletes the Table data , based on a condition
        try:
            cursor.execute(f'USE {database_name}')
            cursor.execute(f'DELETE FROM {table_name} WHERE {condition}' if condition!='' 
                           else f'DELETE FROM {table_name}')
            db.commit()
            print(f'Deletion of condition "{condition}" is complete')
        except Exception as error:
            print(f'Error:{error}')

    def show_table_names(self,database_name:str): # Shows the names of the tables present in a given database
        try:
            cursor.execute(f'USE {database_name}')
            cursor.execute(f'SHOW TABLES')
            tables = cursor.fetchall()
            table_names = [t[0] for t in tables]
            return table_names
        except Exception as error:
            return f'Error : {error}'
        
    def add_new_column(self,database_name:str,table_name:str):  # Alters the table to add a new column
        try:
            cursor.execute(f'USE{database_name}')
            values = {}
            
            column_name = input(f'Enter Column name:')
            datatype = str(input('Enter datatype:')).lower()
            limit = int(input('Enter Limit:'))
            values[column_name] = [datatypes.get(datatype, 'varchar'), limit]

            cursor.execute(f'ALTER {table_name} ADD {column_name} {values[column_name][0]}({limit})')
            db.commit()
            return True
        
        except Exception as error:
            return f' Error:{error}'




# Usage example
creator = Main()
database_name = "IXII"
table_name = "Employee"

print(creator.get_table_header(database_name,table_name))

# Close the database connection when done
db.close()