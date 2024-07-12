import db
import random
import datetime

events = [
    ('Film Society', 'Semester 2 Opening Night Screening', datetime.datetime(2024, 7, 31, 16, 30), datetime.datetime(2024, 7, 31, 21, 0), None, "The University of Sydney's Film Society (FilmSoc) is holding their opening night screening for Semester 2 at Old Geology Lecture Theatre on the 31st of July 2024! We will be screening <em>Om Shanti Om</em> (2007), a Bollywood film from director Farah Khan. The event is open to all FilmSoc members for free and there will also be free pizza!"), 
    ('Movement and Dance Society', 'Ramneek’s Museum Rehearsal', datetime.datetime(2024, 7, 19, 15, 0), datetime.datetime(2024, 7, 19, 17, 0), None, ''), 
    ('Power to Change', 'Pizza Party!', datetime.datetime(2024, 8, 1, 13, 0), datetime.datetime(2024, 8, 1, 15, 0), None, 'Power to Change will be having a pizza party – come along for free pizza! 🍕'), 
    ('Puzzle Society', 'USYD Puzzlesoc Movie Night', datetime.datetime(2024, 10, 24, 18, 0), datetime.datetime(2024, 10, 24, 20, 30), None, 'We\'ll be holding a <strong>Movie Night</strong><img decoding="async" src="https://discord.com/assets/5fb359217c0d94718ec2.svg"/> at the end of the semester! The movie will be decided on by popular vote and be revealed closer towards showtime.  Keep your eyes peeled on Discord or our other socials for updates!   WHEN: Thursday October 24th 6pm-8:30pm WHERE: ABS Case Study Lecture Theatre 1050 '), 
    ('Puzzle Society', 'Usyd Puzzlesoc Switch Night', datetime.datetime(2024, 8, 6, 18, 0), datetime.datetime(2024, 8, 6, 20, 0), None, 'We’re planning on holding a <img decoding="async" src="https://discord.com/assets/3104468867fe05a3fa2e.svg"/> <strong>SWITCH TOURNAMENT</strong> <img decoding="async" src="https://discord.com/assets/3104468867fe05a3fa2e.svg"/> on Tuesday of Week 2 (that’s the 6th of August) in place of our regular Games Night! <img decoding="async" src="https://discord.com/assets/c8b379e5a3bda6d08a71.svg"/> Anyone can compete in one of the Switch games on offer – battle it out with others for the crown! <img decoding="async" src="https://discord.com/assets/652ec4bf8bb976cd272a.svg"/>   Otherwise the vibes will be pretty much our ordinary Games Night. Not interested in competitive gaming? Not to worry! We’ll also have casual fun games and mods for you to play 🙂  WHEN: 6th of August 6pm-8pm WHERE: <img decoding="async" src="https://discord.com/assets/9592f506a368ffa64deb.svg"/>ABS Learning Studio 3080 <img decoding="async" src="https://discord.com/assets/4bc9e31b96f92a347ae9.svg"/>')
]

event_data_dicts = []

for event in events:
    event_data = {}
    event_data["event_name"] = event[1]
    event_data["event_start_date"] = event[2]
    event_data["event_end_date"] = event[3]
    event_data["event_description"] = event[5]
    event_data["event_location"] = ""   # add scrape location code later
    event_data["event_price"] = 0.0     # change to LLM price detection later
    event_data_dicts.append(event_data)

def populate_events(event_data):
    # populate events table
    
    db.create_new_event(connection_string, event_data)

def main():
    db.retrieve_users(connection_string)
    db.retrieve_events(connection_string)
    
    for event_data in event_data_dicts:
        try:
            populate_events(event_data)
        except(Exception) as e:
            print(e)

    
    

if __name__ == "__main__":
    connection_string = db.return_connection_string()

    main()