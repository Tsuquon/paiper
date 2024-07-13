import db
import random
import datetime

usu_events = [
    ('Film Society', 'Semester 2 Opening Night Screening', datetime.datetime(2024, 7, 31, 16, 30), datetime.datetime(2024, 7, 31, 21, 0), None, "The University of Sydney's Film Society (FilmSoc) is holding their opening night screening for Semester 2 at Old Geology Lecture Theatre on the 31st of July 2024! We will be screening <em>Om Shanti Om</em> (2007), a Bollywood film from director Farah Khan. The event is open to all FilmSoc members for free and there will also be free pizza!"), 
    ('Movement and Dance Society', 'Ramneek’s Museum Rehearsal', datetime.datetime(2024, 7, 19, 15, 0), datetime.datetime(2024, 7, 19, 17, 0), None, ''), 
    ('Power to Change', 'Pizza Party!', datetime.datetime(2024, 8, 1, 13, 0), datetime.datetime(2024, 8, 1, 15, 0), None, 'Power to Change will be having a pizza party – come along for free pizza! 🍕'), 
    ('Puzzle Society', 'USYD Puzzlesoc Movie Night', datetime.datetime(2024, 10, 24, 18, 0), datetime.datetime(2024, 10, 24, 20, 30), None, 'We\'ll be holding a <strong>Movie Night</strong><img decoding="async" src="https://discord.com/assets/5fb359217c0d94718ec2.svg"/> at the end of the semester! The movie will be decided on by popular vote and be revealed closer towards showtime.  Keep your eyes peeled on Discord or our other socials for updates!   WHEN: Thursday October 24th 6pm-8:30pm WHERE: ABS Case Study Lecture Theatre 1050 '), 
    ('Puzzle Society', 'Usyd Puzzlesoc Switch Night', datetime.datetime(2024, 8, 6, 18, 0), datetime.datetime(2024, 8, 6, 20, 0), None, 'We’re planning on holding a <img decoding="async" src="https://discord.com/assets/3104468867fe05a3fa2e.svg"/> <strong>SWITCH TOURNAMENT</strong> <img decoding="async" src="https://discord.com/assets/3104468867fe05a3fa2e.svg"/> on Tuesday of Week 2 (that’s the 6th of August) in place of our regular Games Night! <img decoding="async" src="https://discord.com/assets/c8b379e5a3bda6d08a71.svg"/> Anyone can compete in one of the Switch games on offer – battle it out with others for the crown! <img decoding="async" src="https://discord.com/assets/652ec4bf8bb976cd272a.svg"/>   Otherwise the vibes will be pretty much our ordinary Games Night. Not interested in competitive gaming? Not to worry! We’ll also have casual fun games and mods for you to play 🙂  WHEN: 6th of August 6pm-8pm WHERE: <img decoding="async" src="https://discord.com/assets/9592f506a368ffa64deb.svg"/>ABS Learning Studio 3080 <img decoding="async" src="https://discord.com/assets/4bc9e31b96f92a347ae9.svg"/>')
]

meetup_events = [('One Week Online Yoga Sessions  (FREE)', 'Sydney Online Yoga and Energy Healing Meetup Group', datetime.datetime(2024, 7, 15, 11, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), datetime.datetime(2024, 7, 15, 11, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), None, "✨Make your mornings powerful with Yoga\n\n**WHAT'S INCLUDED:**\n1\\. 30 minutes of Yoga Asana Practice for both strength and flexibility\n2\\. Guided Meditation sessions to help still the mind\n3\\. Breathing exercises\n4\\. Tools to help with better sensory engagement to help fully indulge in the moment\n\n**DETAILS:**\nFee : Pay what you like\nTime : 11:00 am to 12:00 pm\nDuration : 1 hour\nWhen : 15th July to 21st July 2024\nWhere: Online\n\n**TO SIGN UP:**\nKindly fill in this [form](https://forms.gle/yEDxnBmVFwYzKKRo8) ( https://forms.gle/yEDxnBmVFwYzKKRo8 )\n\n**GET IN TOUCH:**\nWhatsApp**📱:** [+91 9521642306](https://wa.me/9521642306) ( https://wa.me/9521642306 )\nInstagram **📷:** [@atravyaah](https://www.instagram.com/atravyaah) ( https://www.instagram.com/atravyaah )\n\nFeel free to message me with any questions or queries 💫\n\nSee you on the mat!🧘\u200d♀️"), ('AI And GitHub: Sydney GitHub User Group', 'Sydney GitHub User Group', datetime.datetime(2024, 7, 25, 17, 30, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), datetime.datetime(2024, 7, 25, 17, 30, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), None, "CodeGen and Co-pair programmers are all the rage right now.\n\nWe have a few exciting talks coming soon to a meetup near you.\n\n**Our First Speaker:**\n\n**Andre Kolodochka - Solutions Engineer @ GitHub**\n\n**Title:**\n*What GitHub Copilot is and how it works*\n\n**Description:**\nGitHub Copilot is the world’s most widely adopted AI developer tool for organisations that innovate ahead of the curve through software that disrupts the status quo. Backed by the leaders in AI, Copilot provides contextualised coding assistance for developers, and our research shows that developers are able to code up to 55% faster when they use the tool. This is why over 27,000 businesses worldwide are already taking advantage of the game-changing solution. Join us in this session where we’ll be diving into GitHub Copilot, addressing frequently asked questions around everything from feature functionality to data privacy and security, and providing resources so you can get started today.\n\nNetwork with like-minded individuals, share your knowledge, and stay up to date with the latest trends in software engineering. Don't miss this opportunity to boost your skills and grow your network within the Sydney GitHub User Group community."), ('Landing Your Dream Job: Practical Advice and Tips from HR', 'Sydney Cybersecurity Meetup Group', datetime.datetime(2024, 7, 28, 15, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), datetime.datetime(2024, 7, 28, 15, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), None, "**Agenda**\n1\\. Karen's self\\-introduction\n2\\. The underlying logic of job referrals\n3\\. How HR screens resumes for technical positions\n4\\. The impact of visas on job searching \\(PR\\, 482\\, 485\\, others\\)\n5\\. What qualities ensure success in interviews and quick job offers?\n6\\. Q&A"), ('Digital Transformation in Aged and Social Care', 'Digital Transformation in Aged and Social Care Sydney', datetime.datetime(2024, 7, 26, 8, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), datetime.datetime(2024, 7, 26, 8, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), None, "**Registration required here:** https://bfrank.live/events/aged-social-care-providers-event-2024/\n\nPlease join us for an Amazon Web Services (AWS)-hosted breakfast on exploring the role of digital innovation in transforming aged and social care sectors in Australia.\n\nThis event will bring together thought leaders, industry experts, and providers to discuss the latest trends, technologies, and best practices for enhancing the quality of life for Australians who utilise care services, using digital technology.\n\n**Agenda:**\n8am Registration and Networking Breakfast\n8:30am Welcome and Opening Remarks\n8:40am Transforming Data into Insights to Improve Health and Wellbeing Outcomes\n9am Connected Care - Personalised, Quality Healthcare; Accessible Through Technology\n9:20am Data Driven Insights to Improve Customer & Stakeholder Satisfaction\n9:40am Closing Remarks and Networking\n\n**Speakers:**\n\nBobbie Couhbor, Senior Digital Innovation Solution Architect\nBobbie Couhbor is a Senior Solutions Architect at AWS working within the Digital Innovation team where he is tasked with working closely with enterprise and public sector organisations on exploring and solving unique challenges that often require innovative thinking and the application of emerging technologies, with a focus on IoT, Robotics, and Machine Learning. During his 5 years at AWS, he’s had the opportunity to help customers build cloud enabled robotic applications, design and open source IoT operational technology for industry, and speak at national and international conferences with some of the world’s most innovative thinkers, such as NASA JPL. Prior to his time at AWS, Bobbie consulted for various multi-national and industry leading organisations. Bobbie earned a bachelor of Software Engineering from the University of Canberra.\n\nDouglas Park, Senior Solution Architect\nDouglas is a seasoned Customer Experience specialist with a passion for transforming businesses through data-driven personalization and exceptional customer engagement. Over his 25-year career, Douglas has helped hundreds of organizations across APAC (including federal agencies, charities, utilities, telcos, and 'big 4' banks) leverage data and analytics to measurably improve customer satisfaction, loyalty, and revenue growth. Douglas is a sought-after speaker and thought leader in the Customer Experience domain, having delivered presentations and workshops at leading industry events. Thinking about, talking about and designing great customer experiences is what gets Douglas up in the morning and excites him throughout the day.\n\nSenior Solution Architect - Healthcare and Life Sciences\nShiddy Mwinyi is a Senior Solutions Architect at AWS, specializing in the Healthcare, Life Sciences, and Aged Care sectors. In her four years at AWS, she has played a pivotal role in helping healthcare and aged care organisations harness cloud and data technologies. Her focus includes modernising data platforms, deriving actionable insights from data, and advancing AI adoption in healthcare. Leveraging AWS cloud solutions, Shiddy empowers healthcare and aged care providers to utilise advanced analytics and machine learning, enabling personalised patient experiences and improving overall care outcomes. Prior to joining AWS, Shiddy accumulated valuable experience with top consulting firms, where she supported clients across both commercial and public sector. Her expertise positions her as a trusted partner for organisations striving to innovate and optimise healthcare and aged care delivery through technology.\n\nStrategic Advisor, Public Sector Strategic Development\nAmity is a Strategic Adviser in the Strategic Development team in AWS’ Public Sector business. Amity develops strategic relationships and collaborative initiatives with public sector customers to demonstrate how digital innovation can drive improved economic, social and environmental outcomes for citizens and communities. Before joining AWS Amity was an experienced public sector leader holding senior executive roles across the New South Wales and Victorian governments. Most recently she held the position of Deputy Secretary, Strategy and Planning in the Victorian Department of Health and Human Services, where she led cross-portfolio strategic policy and service reform, analytics and evidence, Aboriginal policy and reform and corporate planning and performance. Amity has also led strategic policy and innovation teams across the health and human services portfolios in the NSW Department of Premier and Cabinet. Amity holds an Executive Masters in Public Administration, Diploma in Law, an Honours degree in Social Sciences and Policy and is a graduate of the Australian Institute of Company Directors."), ('Women in SEO & Digital Marketing Meetup & Drinks - July 2024', 'Women in SEO & Digital Marketing', datetime.datetime(2024, 7, 18, 18, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), datetime.datetime(2024, 7, 18, 18, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), None, 'Our first Women in SEO & Digital Marketing Meetup will happen on Thursday July 18th! Join us for a casual, supportive space to connect, chat and learn from women in the SEO & digital marketing space over food and drinks (not catered for, for now!). Every month we will visit a different and relaxed venue at a convenient location in Sydney CBD.'), ('Sydney MongoDB User Group - July 2024', 'Sydney MongoDB User Group', datetime.datetime(2024, 7, 18, 17, 45, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), datetime.datetime(2024, 7, 18, 17, 45, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), None, "Hi MongoDB Users,\n\nJoin us for the Sydney MongoDB User Group event as we explore best practices and use cases of app development with MongoDB. Whether you're a software developer, tech enthusiast, or simply curious about new technology, this event is for you.\n\nWe're excited to announce an in-person meetup session scheduled for Thursday 18th July 2024. This is a FREE event.\n\nThe agenda for the evening are TBC\n\n* 6:00pm - Announcements\n* 6:10pm - Andy McMenemy - Software Engineer MongoDB\n* 6:40pm - [Luke Thompson Chief Architect at Clarifruit](https://www.linkedin.com/in/lukethompson9/)\n* 7:20pm - Networking / Refreshments\n* 8:00pm - Wrap Up\n\n**Talk 1: Atlas Stream Processing**\nA talk that introduces Atlas' new Stream Processing capabilities. Leverage the document model on Kafka topics, Atlas Change streams, and host it all on MongoDB.\n\n**Talk 2: Atlas Search Development with Java**\nBuilding a Java based Atlas Search service, developing locally against the Atlas Local docker container and unit testing with Test Containers.\n\nPlease **RSVP** if you plan to attend so we can plan for appropriate food & beverage supplies.\n\nYou could also [RSVP on MongoDB Community Forums](https://www.mongodb.com/community/forums/t/sydney-mongodb-user-group-july-2024/283702), if you have an account there.\n\nIf you'd like to present a talk or demo tech related to MongoDB (or suggest topics of interest) please contact the organisers."), ('Sydney Strategy Board Games evening', 'Sydney Strategy Board Games Meetup Group', datetime.datetime(2024, 7, 17, 18, 30, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), datetime.datetime(2024, 7, 17, 18, 30, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), None, "Join us for a fun and engaging evening of strategy board games with like-minded individuals at the Sydney Strategy Board Games Meetup Group. Whether you're a seasoned board gamer or just looking to dip your toes into the world of strategic gameplay, this event is perfect for all levels of experience. Bring your favorite board game or try one of ours as we gather to socialise, strategise, and have a great time together.\n\nMeet fellow board game enthusiasts, make new friends, and enjoy a relaxed atmosphere where you can challenge your cognitive skills and strategic thinking.\n\nWhether you prefer classics like Settlers of Catan or newer titles like Ticket to Ride, there will be something for everyone to enjoy. Don't miss this opportunity to connect with the vibrant board game community in Sydney and experience the thrill of strategy board gaming at its finest!\n\nPlease note the dress code:\nhttps://www.raca.com.au/about-the-club/dress-code\n\nExcited that for those coming along . Just a few things to point out\n\n**Food** \\- the Club will be providing a special menu for us\\, please see details below\n$12 each\n\\- Stir\\-fried Noodles with chicken & Prawn chips\\.\n\\- Fish & chips with lemon & tartare sauce\n\\- Peking duck spring rolls with dipping sauce\n\\- Vegetarian Nasi goreng with fried egg\n\n**On Arrival** \\- please check your name off with the front desk concierge\\. You will need to reply Yes on RSVP to have your name on the list\n\n**Dress Code** \\- very important\\, the Club has a smart casual dress code\\, this means:\n\\- no shorts or t\\-shirts\n\\- yes jeans\\, though they can't be ripped\n\\- a collar shirt or jacket must be worn at all times\n\\- no flip flops or runners\\, closed shoes only\nFurther details here https://www.raca.com.au/about-the-club/dress-code\n\n**Drinks** \\- there will be a full bar\n\n**Games** \\- we will have a few games to join in and play\\, though feel free to bring along any you would also like to play\\.\n\n**Questions?** Please just ask"), ('Social Drinks #9', 'UX After Dark', datetime.datetime(2024, 7, 19, 18, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), datetime.datetime(2024, 7, 19, 18, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), None, "Hey everyone!\n\nMy name is Josh and I am the founder & host of this event. I am currently the Senior UX Designer at The Black Dog Institute in Sydney.\n\nHere is our ninth event!\n\nAs usual there is no agenda, no official talks or design challenges. The aim of this meetup is to network with UX professionals who all share a passion or interest in UX.\n\nTo keep it simple i have kept this at the same venue as last time.\n\nOn arrival please head up the stairs and look for the meetup sign.\n\nCheers,\nJosh\n\nPS: Since the UI of the Meetup app is pretty disappointing, please join this WhatsApp community i have created for this group :D\n\nhttps://tinyurl.com/uxad2024\n\nIf you'd like a chat or have any feedback on my group, you can find me on LinkedIn:\n\nhttps://www.linkedin.com/in/joshualeung/"), ('Automation User Group Summit - Practical Discussion on GenAI in Business', 'Sydney Robotic Process Automation Meetup', datetime.datetime(2024, 7, 25, 18, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), datetime.datetime(2024, 7, 25, 18, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), None, 'We have a pleasure of inviting you to our next Automation User Group Summit hosted at BlueFin. It will start at 5.45pm on 25th July 2024.\n\nThe central topic of this meetup will be a current state of GenAI initiatives in the companies. More and more companies involved in GenAI initiatives with different degrees of success. Our goal during this 2 hours will be to talk to practitioners in the space and discuss what it looks like using it in the trenches.\n\nOur finalised agenda:\n\n17.45 - Open doors and Networking\n18.15 - Presentation - Practical use of RAG in Enterprise\n18.45 - Presentation - Real-life use cases of using GenAI in FinTech\n19.15 - Panel Discussion - Multimodal chatbots - the good, the bad and the ugly\n\nToday we invited following practitioners to take a lead in our event:\n\nJoseph Pham, CEO of Descretion\nErle Pereira, Founder of RRADD Strategy Model\nVasyl Boroviak - CTO at Flash Payments\nBora Wiemann - Co-organiser, Meetup\nLuke Kelly - Co-organiser, Meetup\nPavel Gimelberg - Co-organiser, Meetup\n\nWe are looking forward meeting you at the event'), ('AWS Sydney Well Architected User Group - July 2024 Meetup!', 'AWS Sydney Well-Architected User Group', datetime.datetime(2024, 7, 18, 17, 30, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), datetime.datetime(2024, 7, 18, 17, 30, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), None, 'Welcome to our next [AWS Sydney Well Architected User Group](https://www.meetup.com/aws-sydney-well-architected-user-group/) Meetup for 2024, including some exceptional speakers and topics! :-D\n\nAt each meeting we cover off various pillars in detail, best-practices and insights from industry leaders that specialise in the Well-Architected Framework.\n\nAnd giving away drones, of course. Lots of drones.\n\nWe\'re excited to announce the speakers for this month will be:\n\n* Jason Umiker, Senior Sales Engineer, Sysdig\n\nWe welcome Jason back to cover off the Cost Optimisation Pillar and do a fascinating deep-dive into what tools work best when specifically catering for EKS/Kubernetes environments.\n\n* Luke Fogerty, Technical Director APL, LogicMonitor\n\nThis month, Luke will be revealing how deep and accurate observability is essential to becoming Well-Architected in AWS, including some customer examples.\n\n* Mystery Speaker: AWS Well-Architected changes as announced in June (also known as "Why oh why didn\'t I take the BLUE pill...?")\n\nThis month\'s menu will include:\n\n* Pizzas\n* Beer: Nastro Azzuro\n* Wine: Big and red 🤤\n\nNB: Please enter via Kent St (just to keep you on your toes) and note that this month\'s Meetup will be held at Amazon Web Services Australia P/L offices **Level 9**, 2 Market Street Sydney, NSW 2000.\n\nSo come join us at 5:30 for a 6pm start, followed by beer, wine, pizza and networking after our talks :-)'), ('Is Agile Transformation the ideal approach?', 'Women in Agile Sydney', datetime.datetime(2024, 7, 24, 17, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), datetime.datetime(2024, 7, 24, 17, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), None, "Women in Agile Winter Edition 2024!\n\nIt's been a while in between sessions; life has been busy. But we are looking forward to hosting our next session later this month.\n\nIn this session, facilitator Afra Dianati will lead you through a group activity on how to determine the most effective Agile approach for your new initiative or organisation.\n\n**By the end of this workshop, participants have:**\n\n1. Shared challenges/concerns encountered during Agile transformation in their teams, projects, and companies\n2. Experienced applying decision-making models to real-world experiences with the support of the facilitators\n3. Enhanced their understanding of how these models can help Agile transformation strategies in different organizational contexts.\n4. Last but not least, established connections with other women in the industry and cultivated a stronger support network.\n\n**\\*\\* Everyone is welcome! This is a free event, however, space is limited due to venue capacity :)**\n\n**More about Women in Agile**\nWomen in Agile is an opportunity for locals in the Agile industry to network and learn from each other over drinks and nibbles. The aim of this community and meetup is to spark diverse connections and create stronger networks.\n\nThe Women in Agile Sydney event is hosted and sponsored by [Easy Agile](https://www.easyagile.com/), [Scaled Agile](https://scaledagile.com/) and [Atlassian](https://www.atlassian.com/)."), ('Casual Catch-up', 'Girls Who Boss - Sydney', datetime.datetime(2024, 7, 27, 12, 30, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), datetime.datetime(2024, 7, 27, 12, 30, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), None, 'Join us for our next in-person catchup in Sydney! (Venue TBC but will be around CBD area close to public transport.)\n\nA space for young, female entrepreneurs, businesswomen, creatives, and early careers to meet, no matter your industry or interests! Grab a drink and hang out with some super cool, like-minded ladies. These events are super casual and are a great way to ease yourself into networking and meet some other Girlbosses.\n\nLooking forward to seeing everyone! Feel free to shoot me a message if you have any questions beforehand.\n\n\\*Please note that those who register for an event and do not show up may be removed from the group as per the group etiquette. If you cannot attend please let us know so we can give your spot to someone else. Thanks for your understanding!'), ('Future Author Fun Circles', 'Future Author Fun Circles', datetime.datetime(2024, 7, 23, 11, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), datetime.datetime(2024, 7, 23, 11, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), None, 'In this networking meeting, we will meet other business owners writing their own books.'), ('AllThingsData, Building a Resilient Technology Ecosystem in Uncertain Times', 'all things data. Sydney', datetime.datetime(2024, 7, 24, 17, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), datetime.datetime(2024, 7, 24, 17, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), None, '**Join Us at the July "All Things Data" Meetup in Sydney**\n\n📅 **Date:** Wednesday, 24th July 2024\n🕔 **Time:** 5pm onwards\n📍 **Location:** Microsoft Reactor Sydney, Lv 10/11 York St, Sydney NSW\n\n**Thanks to our Sponsors - Myndful and Confluent!**\n\n**Agenda:**\n\n* **5:00 PM:** Networking, pre-drinks, and food\n* **6:00 PM (Sharp):** Panel Discussion and Q&A\n* **7:00 PM:** Networking\n\n**Speakers:**\n\n* **Aaron Blishen**, CEO/Founder, Myndful.com.au\n* **Glen MacLarty**, Head of Data Platform, HUB24 Group\n* **James Gollan**, Solutions Engineering Manager, Confluent\n* **Rebecca Monfries**, Partner, Terem\n\n**Transforming Business through Data Integration**\nJoin us to explore how businesses can leverage real-time data integration and analytics to drive decision-making, improve efficiencies, and enhance customer experiences. Through compelling case studies, we\'ll demonstrate how effective data integration leads to transformative outcomes.\n\n**Special Topic: Building a Resilient Technology Ecosystem in Uncertain Times**\nOur panel will also discuss strategies for creating robust technology infrastructures capable of withstanding economic fluctuations and cyber threats, highlighting the importance of agility and resilience in technology planning.\n\n**Why Attend?**\n\n* **Engage with Industry Leaders:** Network with CTOs, CDOs, Data Leads, and other senior professionals at the forefront of data innovation.\n* **Explore Advanced Topics:** Delve into real-time data analytics, cybersecurity, and resilient tech ecosystems.\n* **Network and Collaborate:** Enjoy networking opportunities with pre-drinks and food, and engage in meaningful discussions during and after the panel.\n\nThis in-person event is a fantastic opportunity to learn, share insights, and connect with like-minded professionals.\n\n**RSVP and join the conversation here:** All Things Data Meetup - Sydney\nLet’s explore the world of data together!\n\n**Meet Our Confirmed Panel Speakers:**\n**Aaron Blishen**\n**Founder @ Myndful \\| Customer\\-Centric Approach to Data \\| Change Catalyst**\nAaron Blishen is a seasoned leader in digital transformation and data integration with over two decades in the tech industry. At Myndful, Aaron empowers businesses to navigate technological changes and foster an innovation-driven culture. His expertise in software engineering, IT strategy, and product innovation has driven growth and enhanced customer experiences for numerous organisations.\n\n**James Gollan**\n**Solutions Engineering Manager ANZ @ Confluent \\| Data in Motion Advocate**\nJames Gollan helps businesses set their data in motion as the Solutions Engineering Manager at Confluent. With a background in web design, HTML, and Drupal, James drives innovative solutions in data streaming and real-time analytics. He guides organisations through data integration complexities, ensuring they harness their data infrastructure for strategic decision-making.\n\n**Rebecca Monfries**\n**Partner\\, Digital for Enterprise & Government @ Terem \\| Digital Delivery and Product Enthusiast**\nRebecca Monfries leads Terem’s Digital business unit, specialising in building complex functionality into user-facing apps and modernising legacy systems. Experienced in program and project delivery, Rebecca excels in digital product development strategies that deliver measurable outcomes. Her passion for business process improvement and agile project management has positioned her as a key player in digital transformation.\n\n**Glen MacLarty**\n**Head of Data Platform, HUB24 Group**\nGlen MacLarty is an accomplished Solution Architect, Development Team Leader, and Technology Advisor with extensive experience across various industries. At HUB24, Glen leads the development of advanced data capabilities on a modern tech stack incorporating Databricks, dbt, and Google Cloud Platform. He built Qantas\' first chatbot for lounge access queries and led the migration of legacy CRM systems to cloud solutions.\n\n**We\'d love to hear from you if you want to participate in our panel discussion.**\nEven if you can\'t make it this time, let us know if you\'d like to speak at future sessions or have topics you’re passionate about discussing.\nFeel free to reach out if you have any questions or need further information.\n\nWe look forward to seeing you at the event!'), ('Sydney Music Jam - Meetup - Jam July 20, 2024', 'Sydney Music Jam - Meetup', datetime.datetime(2024, 7, 20, 15, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), datetime.datetime(2024, 7, 20, 15, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), None, "Join the Sydney Music Jam Meetup group for a great afternoon of jamming. Bring your instruments to play great music or come to enjoy the melodious tunes of fellow musicians. All skill levels are welcome, from beginners to advanced and professional musicians. Our jam sessions are a great opportunity to connect with other music enthusiasts, exchange tips, learn and simply have a great time. Whatever kind of music you're into, this is the perfect platform to express your musical love and have a blast. Let's make some noise and great music together!\nIdeally 6 people maximum attending to fit comfortably in the rehearsal studio but of course we will accommodate more if more people turn up.\nIf 6 people attend, the cost will be $17.50 per person to cover the cost of the room hire but this will be adjusted if more than 6 people turn up.\nDrummers - if you wish to hire drums (cymbals included) cost is $30 extra on top of the $17.50 per person.\nGuitarists- if you wish to hire an amplifier cost is $25 extra on top of the $17.50 per person.\nCost will be worked out on the day depending on how many people turn up and payable at the studio reception or you can pay me and I will pass on your payment to reception. Cash only please to make it easier.\nFor songlist and further details please see the group's homepage.\n\nIf you RSVP for the jam but you get a message saying that you are waitlisted or you are on a waitlist, just ignore that message and turn up to the jam. I look forward to seeing you all there and let's make some great music!!"), ('Crafting Your Perfect One-Liner: A Hands-On Workshop', 'Sydney Business Growth Accelerator', datetime.datetime(2024, 7, 19, 17, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), datetime.datetime(2024, 7, 19, 17, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), None, "The Sydney Business Growth Accelerator supports the policies and principles of Meetup. We make no guarantees and we do not offer financial services or assurances. All our workshops are FREE to attend.\n\nJoin Dr Edward Klinger of EdwardKlinger Coaching for an engaging and interactive 1-hour workshop designed to help you **master the art of the one-liner**.\n\nIn today's fast-paced world, having a clear and compelling one-liner is crucial for **making a memorable first impression**, whether you're networking, pitching, or simply introducing yourself.\n\nThis workshop will address the common problem of not having a clear one-liner, break down the essential ingredients of a good one-liner, and provide real-world examples to inspire you. Participants will then have the opportunity to craft their own one-liners and receive personalized feedback from Edward and fellow attendees.\n\nDon't miss this chance to refine your message and boost your confidence!"), ('Sydney Women First Skate Meet Up', 'Sydney Women Skateboarding & Cruising Group', datetime.datetime(2024, 7, 14, 15, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), datetime.datetime(2024, 7, 14, 15, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), None, "Join us for our first women's skateboarding meet! We're excited to connect our community of female skateboarders for the very first time.\n\nHere, we're not focused on landing tricks or qualifying for the Olympic team —we're about creating a supportive, inclusive and safe space for women where mental health, connection and community are at the forefront.\n\nPlease come down for a casual, fun but empowering afternoon with your new female skate crew.\n\nLooking forward to meeting you!\nSam"), ('Pie & AI: Sydney - Unpacking Reponsible AI, Ethics, Laws and Regulations', 'Sydney DeepLearning.AI Pie & AI Community', datetime.datetime(2024, 7, 31, 18, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), datetime.datetime(2024, 7, 31, 18, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), None, "Join us for the inaugural Pie & AI DeepLearning.AI Sydney community event were we dive into the world of responsible AI, AI ethics and AI regulations.\n\n**Theme:** Understand current ethical issues working with AI as well as regulations in Australia and rest of the world.\n\nWith the every growing demand for AI's good there is also a challenge to keep up with and understand the various ethical, compliance, governance and risk issues. Hear from hands on practitioners that are working with ethical issues as well responsible AI and legal frameworks in Australia and beyond. Understand how ethics and regulation will play a part in how you shape your AI systems and projects in a very real and practical manner.\n\n**Agenda**\n\n* 6:00pm-6:30pm Networking\n* 6:30pm-7:15pm Talk 1\n* 7:15pm-8:00pm Talk 2\n* 8:00pm Close\n* *Drinks at Cafe 80 next door for those that want to stay back to talk*\n\n**Talks & Speakers**\n\n**AI Regulation Landscape: Navigating the AI Regulations**\n[Raymond Sun](https://www.linkedin.com/in/raymond-sun-64576a122/) (Technology Lawyer, Herbert Smith Freehills) - Raymon is a practicing technology lawyer and developer with a focus on emerging technology law that has developed an AI regulation tracker and global tech law news hub.\n\n* Raymon will walk us through current issues and how to navigate AI law in Australia as anyone working with AI products from procurement to privacy policies. Raymon will also give us a view of emerging global AI regulation in EU and US for those with global customers.\n\n**Responsible AI Engineering: Bridging the Gap between Policy and Practice.**\n[Dr Qinghua Lu](https://people.csiro.au/L/Q/Qinghua-Lu) (Responsible AI Science Team Lead at CSIRO's Data61) - Dr Qinghua Lu is a principal research scientist and leads the Responsible AI science team at CSIRO's Data61. She is the winner of the 2023 APAC Women in AI Trailblazer Award and is part of the OECD.AI’s trustworthy AI metrics project team. She has published 150+ papers in premier international journals and conferences.\n\n* The rapid advancements in AI, particularly with the emergence of large language models (LLMs) and their diverse applications, have attracted huge global interest and raised significant concerns on responsible AI and AI safety. While LLMs are impressive examples of AI models, it is the compound AI systems, which integrate these models with other key components for functionality and quality/risk control, that are ultimately deployed and have real-world impact.\n\n* These AI systems, especially autonomous LLM agents and those involving multi-agent interacting, require system-level engineering to ensure responsible AI and AI safety. In this talk, Dr Lu will introduce a responsible AI engineering approach to address system-level responsible AI challenges. This includes engineering/governance methods, practices, tools, and platforms to ensure responsible AI and AI safety.\n\nThanks\nVincent Koc\nDeepLearning.AI Ambassador"), ('Buying Businesses - Week 2 - Business Acquisition Strategies', 'Australian Business Buyers Community', datetime.datetime(2024, 7, 15, 19, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), datetime.datetime(2024, 7, 15, 19, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))), None, "Join us for Week 2 of our 12 Week Series;\n\n**How to Raise Money, Buy Businesses & Manage A Portfolio of Companies**\n\nYour host; Brandon Lipman, will present an interactive workshop on;\n\n**Business Acquisition Strategies**\n\nKey Areas that will be covered:\n\n* *Sector/Industry Targeting*\n* *Developing a Thesis*\n* *Optimising for Cash on Cash Returns*\n* *Roll Up/Group Building Strategies*\n* *Buy-Build-Sell Strategies*\n* *Growth Through Acquisition*\n* *Joint Exit*\n* *Sweat Equity*\n\nSMB (Small & Medium Business Buying) is a topic heavily covered overseas - but (as per usual) Australia seems to lack its own community.\n\nNo matter whether or not;\n\n* Buying businesses is a new concept to you\n* You've been looking at businesses for a while\n* You've bought 1 or 10 businesses\n\nWe can guarantee you that this will be the group and event to join & be a part of.\n\nYou do not need to have attended any of the previous workshops in order to attend this one. At the end of the series, you'll have access to the entire series for you to watch.\n\nFeel free to bring any questions or an open mind and we look forward to meeting & connecting with you!")]

event_data_dicts = []

for event in usu_events:
    event_data = {}
    event_data["event_name"] = event[1]
    event_data["event_start_date"] = event[2]
    event_data["event_end_date"] = event[3]
    event_data["event_description"] = event[5]
    event_data["event_location"] = ""   # add scrape location code later
    event_data["event_price"] = 0.0     # change to LLM price detection later
    event_data_dicts.append(event_data)

for event in meetup_events:
    event_data = {}
    event_data["event_name"] = event[0]
    event_data["event_start_date"] = event[2]
    event_data["event_end_date"] = event[3]
    event_data["event_description"] = event[5]
    event_data["event_location"] = ""   # add scrape location code later
    event_data["event_price"] = 0.0     # change to LLM price detection later
    event_data_dicts.append(event_data)

def populate_events(event_data):
    # populate events table
    
    db.create_new_event(connection_string, event_data)

def main():
    db.retrieve_users(connection_string)
    db.retrieve_events(connection_string)
    
    for event_data in event_data_dicts:
        try:
            populate_events(event_data)
        except(Exception) as e:
            print(e)

    
    

if __name__ == "__main__":
    connection_string = db.return_connection_string()

    main()
