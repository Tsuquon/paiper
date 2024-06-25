from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime
from scrape_framework import ScrapeFramework

class ScrapeUSU(ScrapeFramework):
    # filter clubs
    def get_clubs(self, clubs):
        clubs = [text for text in clubs if re.match("^https://usu.edu.au/clubs", text)]
        try:
            clubs.remove("https://usu.edu.au/clubs/complaints/")
            clubs.remove("https://usu.edu.au/clubs/")
        
        except(ValueError):
            print("Non-club websites not removed")
        
        else:
            self.club_processing(clubs)
            
            
    # needs club name, description, membership cost
    def club_processing(self, clubs: list):
        club_data = []
        cancel_num = 0
        
        for url in clubs:
            if cancel_num == 10:
                break
            # url = "https://usu.edu.au/clubs/wasabi-japanese-cultural/"
            pattern = r">.*</"
            
            try:
                page_content = requests.get(url).content
            
            except(ConnectionError):
                print(f"Error connecting to {url}")   
            
            else:
                
                try:
                    soup = BeautifulSoup(page_content, "html.parser")
                    title = soup.find("h1", {"class": "Club-module--title--4dc7e"})
                    title = re.search(pattern, str(title)).group()[1:-2]
                    membership_fee = soup.find("div", {"class": "Club-module--fee--18235"})
                    membership_fee = re.search(r"(\$\d)|(Free)", str(membership_fee)).group()
                    membership_fee = 0 if membership_fee == "Free" else int(membership_fee[1:])
                    description = soup.find("div", {"class": "Club-module--mainContainer--4e43a"})
                    description = description.find_all("p")
                    description = re.sub(r"(</*p>,*)|(<strong>Want to join the fun\?.*</strong>)", "", str(description))[1:-1]

                    # print(title, description, membership_fee)
                    # print(membership_fee)
                    club_data.append([title, description, membership_fee])
                    
                except:
                    print(f"problem obtaining information from {url}")
                    
            cancel_num += 1
                    
        print(club_data)
            
    def get_events(self, events):
        events = [text for text in events if re.match("^https://usu.edu.au/events", text)]
        # print(events)
        
        try:
            events.remove("https://usu.edu.au/events/club-events/")
            events.remove("https://usu.edu.au/events/partner-offers/")
            events.remove("https://usu.edu.au/events/usu-events/")
        
        except(ValueError):
            print("Non-club websites not removed")
        
        else:
            self.event_processing(events)

    def event_processing(self, events):
        event_data = []
        cancel_num = 0
        
        for url in events:
            
            if cancel_num == 10:
                break
        
            try:
                page_content = requests.get(url).content
            
            except(ConnectionError):
                print(f"Error connecting to {url}")   
                
            else:
                
                # need event_name, club_name, start_date, end_date, price, description
                # I've noticed events that say free aren't really free - will have to deal with this later, via AIing the desc
                try:
                    soup = BeautifulSoup(page_content, "html.parser")
                    title = soup.find("div", {"class": "Events-module--title--5f77b"})
                    title = re.search("h1>.*</h1", str(title)).group()[3:-4]
                    club_name = soup.find("a", {"class": "club"})
                    club_name = re.search(">.*<", str(club_name)).group()[1:-1]
                    date = soup.find("div", {"class": "date-list"})
                    date = re.search(">.*<!", str(date)).group()[1:-2]
                    date = "0" + date if int(date.split(" ")[0]) < 10 else date
                    start_date = ' '.join(date.split(" ")[:4]) + f" {datetime.today().year}"
                    end_date = ' '.join(date.split(" ")[:2] + date.split(" ")[5:]) + f" {datetime.today().year}"
                    date_format = "%d %b %I:%M %p %Y"
                    start_date = datetime.strptime(start_date, date_format)
                    end_date = datetime.strptime(end_date, date_format)
                    description = soup.find("div", {"class": "main"})
                    description = str(description.find_all("p"))
                    description = re.sub(r"(</*p>,*)|(<strong>Want to join the fun\?.*</strong>)", "", str(description))[1:-1]
                
                
                except Exception as e:
                    print(e)
                    print(f"Problem obtaining information from {url}")   
                    
                else:
                    event_data.append([club_name, title, start_date, end_date, description])
                    
            cancel_num += 1
                
        print(event_data)
        print(len(event_data))


    def main(self):
        
        url = "https://usu.edu.au/sitemap/sitemap-0.xml"
        try:
            xml_data = requests.get(url).content    
        except(ConnectionError):
            print("Connection failed to usu website. Check connection")
        
        soup = BeautifulSoup(xml_data, "xml")
        
        web_links = soup.find_all("loc")
        pattern = r"(<loc>)|(</loc>)"
        web_links = [re.sub(pattern, "", str(text)) for text in web_links]
        
        # self.get_clubs(web_links)
        self.get_events(web_links)
        

if __name__ == "__main__":
    USU_scraper = ScrapeUSU()
    USU_scraper.main()