import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.sql import text


# example data
user_data = {
    'email': 'johndoe@example.com',
    'password': 'password',
    'first_name': 'John',
    'last_name': 'Doe',
    'misc_information': ''
}

user_preferences = ["LAW", "ECONOMICS"]

# ---------------------------------- #

# Always runs

load_dotenv()

username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database_name = os.getenv('DB_NAME')

connection_string = f'postgresql://{username}:{password}@{host}:{port}/{database_name}'

# ---------------------------------- #

def retrieve_users(connection_string):
    engine = create_engine(connection_string)
    connection = engine.connect()

    sql_query = text("SELECT * FROM users")

    result = connection.execute(sql_query)

    for row in result:
        print(row)  # This will print each row as a tuple

    print("---RESULTS PRINTED---")

    connection.close()

def retrieve_events(connection_string):
    engine = create_engine(connection_string)
    connection = engine.connect()

    sql_query = text("SELECT * FROM events")

    result = connection.execute(sql_query)
    my_list = []
    for row in result:
        my_list.append((row[0],row[1],row[2]),)  
        print(row[0],row[1],row[2])  # This will print each row as a tuple

    print("---RESULTS PRINTED---")
    connection.close()
    return my_list    

def create_new_user(connection_string, user_data, user_preferences):
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

def create_new_event(connection_string, event_data):
    row = {
        "event_host": event_data["event_host"],
        "event_name": event_data["event_name"],
        "event_description": event_data["event_description"],
        "event_start_date": event_data["event_start_date"],
        "event_end_date": event_data["event_end_date"],
        "event_location": event_data["event_location"],
        "event_price": event_data["event_price"]
    }

    engine = create_engine(connection_string)
    connection = engine.connect()

    sql_query = text("INSERT INTO events (event_host, event_name, event_description, event_start_date, event_end_date, event_location, event_price) VALUES (:event_host, :event_name, :event_description, :event_start_date, :event_end_date, :event_location, :event_price)")
    connection.execute(sql_query, row)

    sql_query = text("SELECT event_id FROM events WHERE event_name = :event_name")
    result = connection.execute(sql_query, row)

    event_id_row = result.fetchone()
    if not event_id_row:
        print("Error: event not created.")
        connection.close()
        return

    connection.commit()
    connection.close()
    
def retrieve_user_preferences(connection_string, user_id):
    engine = create_engine(connection_string)
    connection = engine.connect()

    sql_query = text("""
    SELECT t.tag
    FROM userPreferences up
    JOIN tags t ON up.tag_id = t.tag_id
    WHERE up.user_id = :user_id
    """)

    result = connection.execute(sql_query, {"user_id": user_id})

    preferences = [row[0] for row in result]
    
    connection.close()
    return preferences

def retrieve_user_additional_info(connection_string, user_id):
    engine = create_engine(connection_string)
    connection = engine.connect()

    sql_query = text("SELECT misc_information FROM users WHERE user_id = :user_id")
    
    result = connection.execute(sql_query, {"user_id": user_id})
    
    # additional_info = result.fetchone()[0] if result.fetchone() else None
    result = result.fetchall()
    connection.close()
    return result
    
def return_connection_string():
    return connection_string

if __name__ == "__main__":
    # createNewUser(connection_string, user_data, user_preferences)
    retrieve_users(connection_string)
    retrieve_events(connection_string)
    print(retrieve_user_preferences(connection_string, 3))


"""
call the webscraping function from Liam which returns events in a tuple -> (event_name, event_description, event_start_date, event_end_date, event_location, event_price)

call the webscraping function from Liam which returns clubs in a tuple -> (club_name, club_description)
"""
