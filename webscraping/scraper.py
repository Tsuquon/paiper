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
        
    club_processing(clubs)
        
        
# needs club name, description, membership cost
def club_processing(clubs: list):
    url = "https://usu.edu.au/clubs/wasabi-japanese-cultural/"
    pattern = r">.*</"
    
    page_content = requests.get(url).content
    soup = BeautifulSoup(page_content, "html.parser")
    title = soup.find("h1", {"class": "Club-module--title--4dc7e"})
    title = re.search(pattern, str(title)).group()[1:-2]
    membership_fee = soup.find("div", {"class": "Club-module--fee--18235"})
    membership_fee = int(re.search(r"\$\d", str(membership_fee)).group()[1:])
    
    description = soup.find("div", {"class": "Club-module--mainContainer--4e43a"})
    description = description.find_all("p")
    description = re.sub(r"</*p>,*", "\\n", str(description))[1:-1]

    print(title, description, membership_fee)
        
def get_events(events):
    events = [text for text in events if re.match("^https://usu.edu.au/events", text)]
    # print(events)
    
    try:
        events.remove("https://usu.edu.au/events/club-events/")
        events.remove("https://usu.edu.au/events/partner-offers/")
        events.remove("https://usu.edu.au/events/usu-events/")
    
    except(ValueError):
        print("Non-club websites not removed")




def main():
    
    url = "https://usu.edu.au/sitemap/sitemap-0.xml"
    xml_data = requests.get(url).content    
    soup = BeautifulSoup(xml_data, "xml")
    
    web_links = soup.find_all("loc")
    pattern = r"(<loc>)|(</loc>)"
    web_links = [re.sub(pattern, "", str(text)) for text in web_links]
    
    get_clubs(web_links)
    # get_events(web_links)
    

if __name__ == "__main__":
    main()