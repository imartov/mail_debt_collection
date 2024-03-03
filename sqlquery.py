'''
Connects to a SQL database using pyodbc
'''

import os
from dotenv import load_dotenv
import logging
from datetime import datetime
import sqlalchemy as db
from sqlalchemy import ForeignKey
from sqlalchemy import select
from sqlalchemy import Table
from sqlalchemy import MetaData
from sqlalchemy import Column

load_dotenv()
logging.basicConfig(level=logging.DEBUG, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

engine = db.create_engine(f"mssql+pymssql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_SERVER')}:{os.getenv('DB_PORT')}/{os.getenv('DATABASE')}")
metadata_obj = MetaData()

service_run = Table(
    "service_run",
    metadata_obj,
    Column("id", db.Integer, primary_key=True, autoincrement=True),
    Column("created_date", db.DateTime, default=datetime.now()),
    Column("result", db.Boolean, default=None)
)

clients = Table(
    "clients",
    metadata_obj,
    Column("unp", db.Integer, primary_key=True),
    Column("monolit_code", db.Integer),
    Column("client_name", db.String(collation="Cyrillic_General_CI_AS")),
    Column("email", db.String(200))
)

delivering = Table(
    "delivering",
    metadata_obj,
    Column("id", db.Integer, primary_key=True, autoincrement=True),
    Column("created_date", db.DateTime, default=datetime.now()),
    Column("service_run_id", ForeignKey("service_run.id"))
)

sent_messages = Table(
    "sent_messages",
    metadata_obj,
    Column("id", db.Integer, primary_key=True, autoincrement=True),
    Column("unp", ForeignKey("clients.unp")),
    Column("payment_date", db.Date),
    Column("debt_amount", db.Float),
    Column("sent_data", db.Date, nullable=False, default=datetime.now().date()),
    Column("delivering_id", ForeignKey("delivering.id"))
)

stop_list = Table(
    "stop_list",
    metadata_obj,
    Column("id", db.Integer, primary_key=True),
    Column("unp", ForeignKey("clients.unp")),
    Column("reason", db.String(collation="Cyrillic_General_CI_AS"))
)

metadata_obj.create_all(engine)

class TransformData:

    def __init__(self, input_data: list) -> None:
        self.input_data = input_data

    def clients(self) -> list:
        output_list = []
        for item in self.input_data:
            output_list.append(
                {
                    "unp": int(item["unp"]),
                    "monolit_code": int(item["monolit_code"]),
                    "client_name": str(item["client_name"]),
                    "email": str(item["email"]),
                }
            )
        return output_list

def select_data(table_name: Table, *args) -> list:
    with engine.connect() as connection:
        stmt = select(table_name.c[*args])
        result = list(connection.execute(stmt))
    return result

def insert_data(table_name: Table, insert_data: dict) -> None:
    with engine.connect() as connection:
        connection.execute(table_name.insert(), insert_data)
        connection.commit()


def main() -> None:
    pass

if __name__ == "__main__":
    main()
