import sqlalchemy
from sqlalchemy.orm import Session

from decouple import config

class SqliteInfrastructure:

    connection = None
    session = None

    @classmethod
    def __get_connection(cls):
        if cls.connection is None:
            engine = sqlalchemy.create_engine(config("HOST_URL"))
            
            cls.connection = engine.connect()
        return cls.connection

    @classmethod
    def get_session(cls):
        if cls.session is None:
            engine = sqlalchemy.create_engine(config("HOST_URL"))
            cls.session = Session(engine)
        return cls.session

    @classmethod
    def script_create_customer_table(cls):

        sql_script = """CREATE TABLE IF NOT EXISTS customer(
                        id INTEGER PRIMARY KEY,
                        id_city VARCHAR(9),
                        name VARCHAR (50),
                        phone VARCHAR (16),
                        sale_opportunity INT)
                   """
        connection = cls.__get_connection()
        connection.execute(sql_script)

    @classmethod
    def script_create_vehicle_table(cls):
        sql_script = """CREATE TABLE IF NOT EXISTS VEHICLE(
                        ID INTEGER PRIMARY KEY,
                        NAME VARCHAR(15),
                        MODEL VARCHAR (11),
                        COLOR VARCHAR (10),
                        CLIENT_ID INTEGER)
                   """
        connection = cls.__get_connection()
        connection.execute(sql_script)