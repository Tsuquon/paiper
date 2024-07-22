import chatgpt
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../database")
import db

connection_string = db.connection_string

"""
- user's selected preference tags
- user's additional information field
- user's events that they clicked like on in the past
- user's events that they clicked dislike on in the past
- all possible events to be recommended

"""

def get_preferences(user_id):
    preferences = db.retrieve_user_preferences(connection_string, user_id)
    random_info = db.retrieve_user_additional_info(connection_string, user_id)
    events_in_db = db.retrieve_events(connection_string)
    
    question = (f"given that the user's preferences are {preferences} and given other additional information is {random_info} and the events are {events_in_db} "
    f"recommend five events that the user would be interested in")
    # print(question)
    return chatgpt.gpt4(question)
    
if __name__ == "__main__":
    answer = get_preferences(6)
    print(answer)