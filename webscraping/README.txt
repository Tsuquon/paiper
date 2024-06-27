# How to get values:

1. Instantiate class that manages website
2. Call either clubs or events - whichever one is needed

# Example

if __name__ == "__main__":
    USU_scraper = ScrapeUSU()
    USU_scraper.get_clubs()
    USU_scraper.get_events()