# These prompts are not needed anymore

class PromptGenerator:
    def __init__(self) -> None:
        self.tagging_prompt = f"""
        ### INSTRUCTION ###
        Given the following event title and description, club name and description, output the category of the event.

        ### INFORMATION ###

        Event Title: {event_title}
        Event Description: {event_desc}

        Club Name: {club_name}
        Club Description: {club_description}

        List of potential categories: {event_categories}


        ### EXAMPLES ###
        Few of the events it runs: [
            {
                "name": "",
                "description": ""
            },
            {
                "name": "",
                "description": ""
            }
        ]
        """

        self.price_check_prompt = f"""
        ### INSTRUCTION ###
        Given the event description, output the lowest cost to attend the event.


        ### INFORMATION ###

        Event Description: {event_description}

        ### EXAMPLES ###

        Event Description: <BEGIN DESCRIPTION> Hihi WASABIANS!! 

        WASABI will be heading to our favourite JAZUSHI for our biannual  IZAKAYA NIGHT !! Come along to meet other WASABIANS, enjoy delicious Japanese cuisine and have a fun night with friends before exam season really begins 
        
        EARLY BIRD PRICES
        WASABI Member: $45
        Non-WASABI Member: $50

        GENERAL RELEASE PRICES
        WASABI Member: $50
        Non-WASABI member: $55 <END DESCRIPTION>

        Event Cost: $45


        Event Description: <BEGIN DESCRIPTION> BOARD GAMES NIGHT IS ON MONDAY 3-6pm at ISL!!!

        What is a better way to break the ice than to play board games? Come to BOARD GAMES NIGHT:pepeHa:  to meet new people and make friends while competing, or working with each other to complete the board games:Peepogamer: . Through exhilarating gameplay,  we could spend a great evening with newly made friends! Snacks and drinks are also supplied🍘 🍹, so come along and enjoy your last week before easter🐰 !! HAVE FUN!!!
        <END DESCRIPTION>

        Event Cost: $0
        """

        self.recommendation_prompt = f"""
        ### INSTRUCTION ###
        You are a recommendation engine with a purpose of recommending events to a student based on their interests. Given the following student interests, please recommend an event that would be most suitable for them.

        ### INFORMATION ###
        Interests: {student_interests}

        Events: {event_list}
        """
    
    def fill_recommendation_prompt(self, student_interests, event_list):
        """
        Fills in the recommendation prompt template with provided student interests and event list.

        Args:
        student_interests (str): The interests of the student.
        event_list (str): A list of events.

        Returns:
        str: The formatted prompt for event recommendation.
        """
        return self.recommendation_prompt.format(
            student_interests=student_interests,
            event_list=event_list
        )

    def fill_price_check_prompt(self, event_description):
        """
        Fills in the price check prompt template with the provided event description.

        Args:
        event_description (str): The description of the event.

        Returns:
        str: The formatted prompt for checking the event cost.
        """
        return self.price_check_prompt.format(
            event_description=event_description
        )

    def fill_tagging_prompt(self, event_title, event_desc, club_name, club_desc, event_categories):
        """
        Fills in the tagging prompt template with provided event and club details.

        Args:
        event_title (str): The title of the event.
        event_desc (str): The description of the event.
        club_name (str): The name of the club hosting the event.
        club_desc (str): The description of the club hosting the event.
        event_categories (list): A list of potential categories for the event.

        Returns:
        str: The formatted prompt for event categorization.
        """
        return self.tagging_prompt.format(
            event_title=event_title,
            event_desc=event_desc,
            club_name=club_name,
            club_desc=club_desc,
            event_categories=', '.join(event_categories)
        )





