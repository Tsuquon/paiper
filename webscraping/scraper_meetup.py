from scrape_framework import ScrapeFramework
from bs4 import BeautifulSoup
import requests
import re
import json
from datetime import datetime


class ScrapeMeetup(ScrapeFramework):
   
    def get_clubs(self, clubs):
        raise NotImplementedError("Method not imported")
   
    
    def process_clubs(self, clubs):
        raise NotImplementedError("Method not imported")
    
    
    def get_events(self, events):
        raise NotImplementedError("Method not imported")
    
    
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
        
        events = []
        
        for event_key in data:
            if event_key.startswith("Event"):
                events.append(data[event_key])
                print(data[event_key])

        # self.get_clubs()
        self.get_events()
        
        formatted = json.dumps(data, indent=2)
        print(events)
        
if __name__ == "__main__":
    scrape_meetup = ScrapeMeetup()
    scrape_meetup.main()