from scrape_framework import ScrapeFramework
from bs4 import BeautifulSoup
import requests
import re
import json
from datetime import datetime


class ScrapeMeetup(ScrapeFramework):
    
    def __init__(self) -> None:
        self.club_references = {}
        self.club_name_references = {}
   
    # club name, description, membership cost
    # I think joining clubs are free
    def get_clubs(self, clubs):
        club_data = []
        
        for club in clubs:
            self.club_references.update({club["id"]: club["name"]})
            self.club_references.update({club["urlname"]: club["name"]})
            club_data.append(club["name"], "Unable to retrieve", 0)
            
            
            
   
    
    def process_clubs(self, clubs):
        raise NotImplementedError("Method not imported")
    
    # events free too?
    def get_events(self, events):
        
        # need event_name, club_name, start_date, end_date, price, description
        # price not integrated yet
        event_data = []
        for event in events:
            date = datetime.fromisoformat(event["dateTime"])
            try:
                name = self.club_references.get((event["group"]["__ref"]).split(":")[1])
            except(KeyError):
                try:
                    name = self.club_references.get((event["group"]["urlname"]))
                except(KeyError):
                    print(f"Invalid __ref and urlname for event")
                    name = "INVALID"
            try:
                
                event_data.append([event["title"], name, date, date, event["description"]])
                
            except(KeyError):
                print(f"invalid for {name}")
    
        print(event_data)
    
    def process_events(self, events):
        raise NotImplementedError("Method not imported")
    
    def main(self):
        url = "https://www.meetup.com/en-AU/find/?source=EVENTS&location=au--sydney"
        try:
            website_data = requests.get(url).content    
        except(ConnectionError):
            print("Connection failed to usu website. Check connection")
        
        soup = BeautifulSoup(website_data, "xml")
        extract = soup.find("script", {"id": "__NEXT_DATA__"})
        extract = str(extract)
        # print(extract)
        my_json = re.findall(r"{.*}", extract)[0]
        data = json.loads(my_json)
        data = data["props"]["pageProps"]["__APOLLO_STATE__"]
        
        groups = []
        events = []
        
        for group_key in data:
            if group_key.startswith("Group"):
                groups.append(data[group_key])
                
        
        for event_key in data:
            if event_key.startswith("Event"):
                events.append(data[event_key])
                # print(data[event_key])

        self.get_clubs(groups)
        self.get_events(events)
        
        # formatted = json.dumps(data, indent=2)
        # print(events)
        
if __name__ == "__main__":
    scrape_meetup = ScrapeMeetup()
    scrape_meetup.main()