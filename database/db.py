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

def createNewUser(connection_string, user_data, user_preferences):
    row = {
        "email": user_data["email"],
        "password": user_data["password"],
        "first_name": user_data["first_name"],
        "last_name": user_data["last_name"],
        "misc_information": user_data["misc_information"]
    }

    engine = create_engine(connection_string)
    connection = engine.connect()

    sql_query = text("INSERT INTO users (email, password, first_name, last_name, misc_information) VALUES (:email, :password, :first_name, :last_name, :misc_information)")
    connection.execute(sql_query, row)

    sql_query = text("SELECT user_id FROM users WHERE email = :email")
    result = connection.execute(sql_query, row)

    user_id_row = result.fetchone()
    if not user_id_row:
        print("Error: user not created.")
        connection.close()
        return
        
    created_user_id = user_id_row[0]
        
    tag_ids = []
    for user_preference in user_preferences:
        sql_query = text("SELECT tag_id FROM tags WHERE tag = :tag")
        result = connection.execute(sql_query, {"tag": user_preference})

        tag_id_row = result.fetchone()
        if tag_id_row:
            tag_ids.append(tag_id_row[0])

    for tag_id in tag_ids:
        sql_query = text("INSERT INTO userPreferences (user_id, tag_id) VALUES (:user_id, :tag_id)")
        connection.execute(sql_query, {"user_id": created_user_id, "tag_id": tag_id})

    connection.commit()
    connection.close()

user_data = {
    'email': 'johndoe@example.com',
    'password': 'password',
    'first_name': 'John',
    'last_name': 'Doe',
    'misc_information': ''
}

user_preferences = ["LAW", "ECONOMICS"]

createNewUser(connection_string, user_data, user_preferences)


"""
call the webscraping function from Liam which returns events in a tuple -> (event_name, event_description, event_start_date, event_end_date, event_location, event_price)

call the webscraping function from Liam which returns clubs in a tuple -> (club_name, club_description)
"""
