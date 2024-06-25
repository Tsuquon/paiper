
- categories
  - we use LLMs to categorise initial list of events scraped from USU website, use those categories as base list of categories
  - initial PoC of website would be simply a flat screen with list of such categories, users can tap/click category to enable/disable
  - improvement or expansion after completion of PoC could include suggestion further categories based on what the user clicked first (screen is dynamic and categories available change as user makes more selections - like Apple Music sign up screen)

- lack of events on USU website right now
  - due to semester break;
  - for now use meetup.com to scrape data and create list of categories

- recommendation email to be sent out
  - create standard HTML template for emails with 5 slots of events to be recommended, parsed output from recommendation engine prompt to be slotted into each event slot in the email
  - email template should also include slot for student's name as a greeting for personalisation
  - email template should have like/dislike button for every event slot
    - each like/dislike button should point to a URL to action each like/dislike

- prompt engineering
  - prompt engineering should work off the schema
    - any few-shot examples should use the structure of the SQL schema

By Sunday, 30th June:

- Kerui: write SQL query to extract each event and club from SQL database, insert event and club attributes from table into prompt templates as variables, parse output from prompt (which would be the tags and prices) and insert that back into the database

- Liam: create functions for Bernard to call to dump scraped data into the database
  - events function returns tuple -> (event_name, event_description, event_start_date, event_end_date, event_location, event_price)
  - clubs function returns tuple -> (club_name, club_description)

- Bernard: 
  - create a PostgreSQL server, create all the tables from schema.sql, and share the database credentials (hostname, username, password, database name)
  - write Python code to interact with PostgreSQL database (using SQLAlchemy)
  - create Python function for the creation of a new user (their name, email, password, preferences - tags they like)

After Sunday, 30th June:

- Kerui and Liam: work on recommendation algorithm to recommend events to users based on tags (match user preference tags to event tags / club tags)
  - can use LLM to recommend or can use mathematical algorithms to recommend
- Bernard: work on frontend for user enrolment and newsletter email template
