
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
