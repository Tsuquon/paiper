from bs4 import BeautifulSoup
import requests
import re

    # filter clubs
def get_clubs(clubs):
    clubs = [text for text in clubs if re.match("^https://usu.edu.au/clubs", text)]
    try:
        clubs.remove("https://usu.edu.au/clubs/complaints/")
        clubs.remove("https://usu.edu.au/clubs/")
    
    except(ValueError):
        print("Non-club websites not removed")
        
def get_events(events):
    events = [text for text in events if re.match("^https://usu.edu.au/events", text)]
    print(events)
    
    try:
        events.remove("https://usu.edu.au/events/club-events/")
        events.remove("https://usu.edu.au/events/partner-offers/")
        events.remove("https://usu.edu.au/events/usu-events/")
    
    except(ValueError):
        print("Non-club websites not removed")

def source_information(scraped_links):
    pass


def main():
    
    url = "https://usu.edu.au/sitemap/sitemap-0.xml"
    xml_data = requests.get(url).content    
    soup = BeautifulSoup(xml_data, "xml")
    
    web_links = soup.find_all("loc")
    pattern = r"(<loc>)|(</loc>)"
    web_links = [re.sub(pattern, "", str(text)) for text in web_links]
    
    # get_clubs(web_links)
    get_events(web_links)
    

if __name__ == "__main__":
    main()