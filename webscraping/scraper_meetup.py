from scrape_framework import ScrapeFramework
from bs4 import BeautifulSoup
import requests
import re
import json
from datetime import datetime
from tqdm import tqdm


class ScrapeMeetup(ScrapeFramework):
    
    def __init__(self) -> None:
        self.club_references = {}
        self.club_name_references = {}
        
        url = "https://www.meetup.com/en-AU/find/?source=EVENTS&location=au--sydney"
        try:
            website_data = requests.get(url).content    
        except(ConnectionError):
            print("Connection failed to meetup website. Check connection")
        
        soup = BeautifulSoup(website_data, "xml")
        extract = soup.find("script", {"id": "__NEXT_DATA__"})
        extract = str(extract)
        my_json = re.findall(r"{.*}", extract)[0]
        data = json.loads(my_json)
        data = data["props"]["pageProps"]["__APOLLO_STATE__"]
        
        self.clubs = []
        self.events = []
        
        for group_key in data:
            if group_key.startswith("Group"):
                self.clubs.append(data[group_key])
                
        
        for event_key in data:
            if event_key.startswith("Event"):
                self.events.append(data[event_key])
   
    # club name, description, membership cost
    # I think joining clubs are free
    def get_clubs(self):
        
        # need to get meetup description here 
                
        club_data = []
        
        for club in tqdm(self.clubs, desc="updating club dictionary"):
            self.club_references.update({club["id"]: club["name"]})
            self.club_name_references.update({club["urlname"]: club["name"]})
            
            club_data.append((club["name"], self.get_description(club), 0))
            
        return club_data         
   
    def get_description(self, club):
       url = "https://www.meetup.com/" + club["urlname"]
       group_page = requests.get(url).content
       soup = BeautifulSoup(group_page, "html.parser")
       description = soup.find("p", {"class": "mb-4"})
       return description

    # events free too?
    def get_events(self):
        
        # need event_name, club_name, start_date, end_date, price, description
        # price not integrated yet
        event_data = []
        for event in self.events:
            date = datetime.fromisoformat(event["dateTime"])
            try:
                name = self.club_references.get((event["group"]["__ref"]).split(":")[1])
            except(KeyError):
                try:
                    name = self.club_name_references.get((event["group"]["urlname"]))
                except(KeyError):
                    print(f"Invalid __ref and urlname for event")
                    name = "INVALID"
            try:
                
                event_data.append((event["title"], name, date, date, None, event["description"]))
                
            except(KeyError):
                print(f"invalid for {name}")
    
        print(event_data)
        return event_data
    
        
if __name__ == "__main__":
    scrape_meetup = ScrapeMeetup()
    print(scrape_meetup.get_clubs())
    scrape_meetup.get_events()