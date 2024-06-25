import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.sql import text

load_dotenv()

username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database_name = os.getenv('DB_NAME')

connection_string = f'postgresql://{username}:{password}@{host}:{port}/{database_name}'

def retrieveUsers(connection_string):
    engine = create_engine(connection_string)
    connection = engine.connect()

    sql_query = text("SELECT * FROM users")

    result = connection.execute(sql_query)

    for row in result:
        print(row)  # This will print each row as a tuple

    print("---RESULTS PRINTED---")

    connection.close()

retrieveUsers(connection_string)

"""
call the webscraping function from Liam which returns events in a tuple -> (event_name, event_description, event_start_date, event_end_date, event_location, event_price)

call the webscraping function from Liam which returns clubs in a tuple -> (club_name, club_description)
"""
