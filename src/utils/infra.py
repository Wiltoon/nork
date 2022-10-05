import sqlalchemy
from sqlalchemy.orm import Session, declarative_base

from decouple import config

HOST_URL = 'postgresql+psycopg2://postgres:0254@localhost:5433/norktown'
class PostgreSQLInfrastructure:

    connection = None
    session = None

    @classmethod
    def __get_connection(cls):
        if cls.connection is None:
            engine = sqlalchemy.create_engine(HOST_URL)
            cls.connection = engine.connect()
        return cls.connection

    @classmethod
    def get_session(cls):
        if cls.session is None:
            engine = sqlalchemy.create_engine(HOST_URL)
            cls.session = Session(engine)
        return cls.session

    @classmethod
    def script_create_customer_table(cls):

        sql_script = """CREATE TABLE IF NOT EXISTS customer(
                        id INTEGER PRIMARY KEY,
                        idcity VARCHAR(9),
                        name VARCHAR (50),
                        phone VARCHAR (16),
                        sale_opportunity INTEGER)
                   """
        connection = cls.__get_connection()
        connection.execute(sql_script)

    @classmethod
    def script_create_vehicle_table(cls):
        sql_script = """CREATE TABLE IF NOT EXISTS vehicle(
                        id INTEGER PRIMARY KEY,
                        name VARCHAR(15),
                        model VARCHAR (11),
                        color VARCHAR (10),
                        customer_id INTEGER)
                   """
        connection = cls.__get_connection()
        connection.execute(sql_script)