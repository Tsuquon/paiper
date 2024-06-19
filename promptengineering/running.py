import chatgpt


tagging_prompt = """HERE ARE A LIST OF RECOGNISED CATEGORIES: ARTS & CRAFTS, POLITICS, LAW, MEDICINE, ENGINEERING

given the following event title and description, please tag the event with the most appropriate category

Description: this workshop

Club Name and Description: 
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


price_doublecheck_prompt = """Given the following event description, please parse the price to participate in the event:

+ few shot examples

Description: this event is very good i like it very much costs $5 to attend
Price: $5.00

Description: fun ball and gala very good $25.5
Price: $25.50

Description: {description}
"""


recommendation_prompt = """You are a recommendation engine with a purpose of recommending events to a student based on their interests. Given the following student interests, please recommend an event that would be most suitable for them.

Interests: {tags they selected during onboarding, and any tags added thereafter when they click like/dislike button in their recommendations}

Events: [
    {
        "name": "",
        "description": ""
        ...
    },
    {
        "name": "",
        "description": ""
    }
]

Recommended Events: []
"""
