import db
import random

# required data in df, tuple requirements as (userid, event id, recommendation strenght)

# ----- Sample data ----- #





# ----------------------- #

# ----- Sample dataset ----- #
first_names = ['John',
               'Jane',
               'Bob',
               'Alice',
               'Eve',
               'Mary',
               'Mike',
               'Sue'
               ]

last_names = ['Smith',
              'Bean',
              'Jones',
              'Doe',
              'Brown',
              'Johnson',
              'Williams',
              'Davis'         
              ]

interests = ['LAW',
             'ECONOMICS',
             'TENNIS',
             'COMPUTERS',
             'PARTY',
             'READING']

# ----------------------- #



def populate_users():
    # populate users table
    
    first_name = first_names[random.randrange(0,len(first_names))]
    last_name = last_names[random.randrange(0,len(last_names))]
    
    row = {
    "email": f"{first_name}{last_name}@gmail.com",
    "password": "12345678",
    "first_name": first_name,
    "last_name": last_name,
    "misc_information": "random information"
    }
    
    user_preferences = interests[random.randrange(0, len(user_preferences))]
    db.create_new_user(connection_string, row, user_preferences)
    


def main():
    db.retrieve_users(connection_string)
    db.retrieve_events(connection_string)
    
    for _ in range(16):
        try:
            populate_users()
        except(Exception) as e:
            print(e)

    
    

if __name__ == "__main__":
    connection_string = db.return_connection_string()

    main()