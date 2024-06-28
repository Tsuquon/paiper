import requests
from bs4 import BeautifulSoup
import re
import gzip
import json
import os
from tqdm import tqdm

class MeetupEvents:
    
    
    def __init__(self):
        
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(self.script_dir, "cache/meetup_groups.txt")

        source_link = "https://www.meetup.com/groups-index-sitemap.xml"
        
        self.link_dict = {}
        
        try:
            xml_data = requests.get(source_link).content    
        except(ConnectionError):
            print("Connection failed to meetup website. Check connection")
        
        soup = BeautifulSoup(xml_data, "xml")
        web_links = soup.find_all("loc")
        pattern = r"(<loc>)|(</loc>)"
        self.web_links = [re.sub(pattern, "", str(text)) for text in web_links]
        print(self.web_links)
        
    def get_groups(self):
        
        if os.path.exists(self.file_path):
            user_answer = input("File already exists: Are you sure you want to refresh? (Y/N) ")
            if user_answer == "N":
                return
        
        for link in tqdm(self.web_links, desc="processing links"):
            try:
                xml_data = requests.get(link).content
            except(ConnectionError):
                print("Failed to obtain individual link")

            my_gzip = gzip.decompress(xml_data)
            soup = BeautifulSoup(my_gzip, "xml")

            group_links = soup.find_all("loc")
            pattern = r"(<loc>)|(</loc>)"
            group_links = [re.sub(pattern, "", str(text)).split('/')[-2] for text in group_links]
            
            for group_link in group_links:
                if group_link not in self.link_dict:
                    self.link_dict.update({group_link: 1})
                    
                else:
                    self.link_dict[group_link] += 1
        
    def write_groups(self):
        
        if len(self.link_dict) == 0:
            return

        with open(self.file_path, "w") as f:
            f.write(json.dumps(self.link_dict))
    
    
if __name__ == "__main__":
    meetup = MeetupEvents()
    meetup.get_groups()
    meetup.write_groups()
    