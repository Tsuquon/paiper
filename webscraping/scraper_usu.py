from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime
from scrape_framework import ScrapeFramework

class ScrapeUSU(ScrapeFramework):
    # filter clubs
    def __init__(self) -> None:
        url = "https://usu.edu.au/sitemap/sitemap-0.xml"
        try:
            xml_data = requests.get(url).content    
        except(ConnectionError):
            print("Connection failed to usu website. Check connection")
        
        soup = BeautifulSoup(xml_data, "xml")
        
        web_links = soup.find_all("loc")
        pattern = r"(<loc>)|(</loc>)"
        self.web_links = [re.sub(pattern, "", str(text)) for text in web_links]
    
    def get_clubs(self):
        clubs = [text for text in self.web_links if re.match("^https://usu.edu.au/clubs", text)]
        try:
            clubs.remove("https://usu.edu.au/clubs/complaints/")
            clubs.remove("https://usu.edu.au/clubs/")
        
        except(ValueError):
            print("Non-club websites not removed")
        
        else:
            return self.club_processing(clubs)
            
            
    # needs club name, description, membership cost
    def club_processing(self, clubs: list[str]):
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
                    club_data.append((title, description, membership_fee))
                    
                except:
                    print(f"problem obtaining information from {url}")
                    
            cancel_num += 1
                    
        print(club_data)
        return club_data
            
    def get_events(self):
        events = [text for text in self.web_links if re.match("^https://usu.edu.au/events", text)]
        # print(events)
        
        try:
            events.remove("https://usu.edu.au/events/club-events/")
            events.remove("https://usu.edu.au/events/partner-offers/")
            events.remove("https://usu.edu.au/events/usu-events/")
        
        except(ValueError):
            print("Non-club websites not removed")
        
        else:
            return self.event_processing(events)
        
    def convert_date_time_range(self, date_time_range):
        # Split the date and time range into parts
        dates, times = date_time_range[:len(date_time_range)//2 - 1], date_time_range[len(date_time_range)//2 - 1:]
        start_date_str, end_date_str = dates.split(' - ')
        start_time_str, end_time_str = times.split(' to ')

        # Assuming the year is 2024
        year = 2024

        # Combine dates and times with year
        start_datetime_str = f"{start_date_str} {start_time_str} {year}"
        print(start_datetime_str)
        end_datetime_str = f"{end_date_str} {end_time_str} {year}"
        print(end_datetime_str)

        # Convert to datetime objects
        date_format = "%d %b %I:%M %p %Y"
        try:
            start_datetime = datetime.strptime(start_datetime_str, date_format)
        except Exception:
            date_format = "%I %M %p %Y"
            start_datetime = datetime.strptime(start_datetime_str, date_format)
        date_format = "%d %b %I:%M %p %Y"
        end_datetime = datetime.strptime(end_datetime_str, date_format)


        return start_datetime, end_datetime

    def event_processing(self, events):
        

        
        event_data = []
        cancel_num = 0
        
        for url in events:
            
            if cancel_num == 30:
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
                    if '-' not in date:
                        print("DATE IS",date)
                        start_date = ' '.join(date.split(" ")[:4]) + f" {datetime.today().year}"
                        print("START IS", start_date)
                        end_date = ' '.join(date.split(" ")[:2] + date.split(" ")[5:]) + f" {datetime.today().year}"
                        print("END IS", end_date)
                        date_format = "%d %b %I:%M %p %Y"
                        start_date = datetime.strptime(start_date, date_format)
                        end_date = datetime.strptime(end_date, date_format)
            

                    else:
                        start_date, end_date = self.convert_date_time_range(date)
                    

                    description = soup.find("div", {"class": "main"})
                    description = str(description.find_all("p"))
                    description = re.sub(r"(</*p>,*)|(<strong>Want to join the fun\?.*</strong>)", "", str(description))[1:-1]
                
                
                except Exception as e:
                    print(e)
                    print(f"Problem obtaining information from {url}")   
                    
                else:
                    event_data.append((club_name, title, start_date, end_date, None, description))
                    
            cancel_num += 1
                
        print(event_data)
        # print(len(event_data))
        return event_data


if __name__ == "__main__":
    USU_scraper = ScrapeUSU()
    USU_scraper.get_clubs()
    USU_scraper.get_events()