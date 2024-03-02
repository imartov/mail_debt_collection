'''
Connects to a SQL database using pyodbc
'''

import os
import pyodbc
from dotenv import load_dotenv
import logging
from datetime import datetime
import pyodbc
import sqlalchemy as db
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import insert
from sqlalchemy import URL
from sqlalchemy.sql import func
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import select
from sqlalchemy import Table
from sqlalchemy import MetaData
from sqlalchemy import Column

load_dotenv()
logging.basicConfig(level=logging.DEBUG, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

engine = db.create_engine("mssql+pymssql://sa:12345-Suka@127.0.0.1:1433/db_emaildebtcollection", echo=True)
metadata_obj = MetaData()

service_run = Table(
    "service_run",
    metadata_obj,
    Column("id", db.Integer, primary_key=True, autoincrement=True, nullable=False),
    Column("created_date", db.DateTime, default=datetime.now(), nullable=False),
    Column("result", db.Boolean, default=None)
)

clients = Table(
    "clients",
    metadata_obj,
    Column("unp", db.Integer, primary_key=True),
    Column("monolit_code", db.Integer, unique=True, index=True, nullable=False),
    Column("client_name", db.String(200), index=True, unique=True, nullable=False),
    Column("email", db.String)
)

delivering = Table(
    "delivering",
    metadata_obj,
    Column("id", db.Integer, primary_key=True, autoincrement=True, nullable=False),
    Column("created_date", db.DateTime, default=datetime.now(), nullable=False),
    Column("service_run_id", ForeignKey("service_run.id"))
)

sent_messages = Table(
    "sent_messages",
    metadata_obj,
    Column("id", db.Integer, primary_key=True, autoincrement=True, nullable=False),
    Column("unp", ForeignKey("clients.unp")),
    Column("payment_date", db.Date, nullable=False),
    Column("debt_amount", db.Float, nullable=False),
    Column("sent_data", db.Date, nullable=False, default=datetime.now().date()),
    Column("delivering_id", ForeignKey("delivering.id"), nullable=False)
)

stop_list = Table(
    "stop_list",
    metadata_obj,
    Column("id", db.Integer, primary_key=True),
    Column("unp", ForeignKey("clients.unp")),
    Column("reason", db.Text)
)

metadata_obj.create_all(engine)

def insert_data(table_name: Table, insert_data: dict) -> None:
    with engine.connect() as connection:
        connection.execute(table_name.insert(), insert_data)
        connection.commit()


def main() -> None:
    pass

if __name__ == "__main__":
    main()
