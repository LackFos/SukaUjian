import os
import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv
from Exception import DatabaseConnectionError

# Load enviroment variable dari file .env 
load_dotenv()

class Connect:
    def __init__(self):
        __mydb = None
        __cursor = None

        try:
            # Attempt to Connect Database
            self.__mydb = mysql.connector.connect(
                user=os.getenv("DB_USER"), 
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                database=os.getenv("DB_NAME")    
            )
            self.__cursor = self.__mydb.cursor(dictionary=True)
            print("Database Terkoneksi")

        except mysql.connector.Error as err:
            # Throw Error
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise("Username atau password database salah")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise DatabaseConnectionError(f"Database {os.getenv('DB_NAME')} tidak ada")
            else:
                raise DatabaseConnectionError(err)

    def __execute(self, query, values):
        try:
            self.__cursor.execute(query, values)
            self.__mydb.commit()
        except mysql.connector.Error as err:
            raise DatabaseConnectionError(err)

    def get(self, table, columns=[]):
        # Setting up required data
        columnToSelect = ', '.join(columns) if columns else '*'
        query = f"SELECT {columnToSelect} FROM {table}"

        # Execute mysql script
        self.__cursor.execute(query)
        result = self.__cursor.fetchall()
        return result

    def insert(self, table, data):
        # Setting up required data
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data)) 
        values = list(data.values())
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

        # Execute mysql script
        self.__execute(query, values)
        print("Data berhasil di insert")

    def update(self, table, where, data):
        # Setting up required data
        columns = ', '.join([f"{key} = %s" for key, value in data.items()])
        target = ', '.join([f"{key} = %s" for key, value in where.items()])
        values = list(data.values()) + list(where.values())
        query = f"UPDATE {table} SET {columns} WHERE {target}"

        # Execute mysql script
        self.__execute(query, values)
        print("Data berhasil di update")

    def delete(self, table, where):
        target = ', '.join([f"{key} = %s" for key, value in where.items()])
        values = list(where.values())
        query = f"DELETE FROM {table} WHERE {target}"

        # Execute mysql script
        self.__execute(query, values)
        print("Data berhasil di hapus")

