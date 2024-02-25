'''
Connects to a SQL database using pyodbc
'''

import os
import pyodbc
from dotenv import load_dotenv
import logging

load_dotenv()
logging.basicConfig(level=logging.DEBUG, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

def connect_db():
    connectionString = f'DRIVER={{SQL Server}};\
        SERVER={os.getenv("DB_SERVER")};\
        DATABASE={os.getenv("DATABASE")};\
        UID={os.getenv("DB_USERNAME")};\
        PWD={os.getenv("DB_PASSWORD")}'
    conn = pyodbc.connect(connectionString)

def main() -> None:
    connect_db()

if __name__ == "__main__":
    main()
