<h1>Willow Dale Menu - Alexa Skill</h1> <img src="https://i.imgur.com/I4EbBQV.png"/>

<h2>Introduction :mega:</h2>

<h3>Brief Overview :briefcase:</h3>

<p>
The "Willow Dale Menu Alexa Skill" is a voice-activated application designed for Amazon's Alexa platform.
It serves as a convenient tool for parents and students of Willow Dale Elementary School, providing instant access to the school's breakfast and lunch menus for the current and following day. Unlike traditional methods of checking the school's website, this Alexa Skill offers a hands-free, on-demand solution for busy families.
</p>

<h3>Motivation :muscle:</h3>

<p>
My inspiration for developing this Alexa Skill stemmed from a personal necessity. As a parent, I often found myself in a rush, struggling to visit the school's website to check the daily menu options. This challenge sparked the idea of utilizing voice-enabled technology to streamline the process.
The Alexa Skill emerged as an ideal solution, allowing users to effortlessly inquire about meal options while on the go, whether it's during the morning hustle or while preparing for the next day.
</p>

<h2>Features :high_brightness:</h2>

<h3>Functionality :battery:</h3>
<p>
This Alexa Skill is designed with simplicity and ease of use in mind. Users can ask Alexa about the breakfast and lunch menus at Willow Dale Elementary for both today and tomorrow. The Skill, through Alexa's voice, responds with the day's menu, eliminating the need to manually search for this information. This feature not only saves time but also enhances the daily routines of families.
</p>

<h3>User Interaction Examples :bust_in_silhouette:</h3>

<p>
Interaction with the Willow Dale Menu Alexa Skill is intuitive and user-friendly. Here are a few voice command examples that users can use:

* "Alexa, open Willow Dale Menu and ask, 'What’s for breakfast today?'"
* "Alexa, ask Willow Dale Menu, 'What's for breakfast and lunch tomorrow?'"
* "Alexa, ask Willow Dale Menu, 'What’s for lunch today?'"

These commands highlight the Skill's ability to provide quick and relevant menu information for both today and the next day, catering to the immediate needs of the users.
</p>

<h2>Getting Started :running:</h2>

<p>This guide outlines the process of setting up the Willow Dale Menu Alexa Skill, hosted as an AWS Lambda function using Python in the Alexa Developer Console.</p>

<h3>Prerequisites :nut_and_bolt:</h3>

* An Amazon Web Services (AWS) account (<a href="https://aws.amazon.com/free/?trk=78b916d7-7c94-4cab-98d9-0ce5e648dd5f&sc_channel=ps&s_kwcid=AL!4422!3!432339156165!e!!g!!create%20aws%20account&ef_id=Cj0KCQiAic6eBhCoARIsANlox86TYDv0SwS8ZeHSBz83fubw5sXAhH_TBkWOhPDbwLqhL2emHYOICfgaAhIMEALw_wcB:G:s&s_kwcid=AL!4422!3!432339156165!e!!g!!create%20aws%20account&all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all">you can sign up here</a> *FREE)
* An Amazon Developer account (<a href="https://developer.amazon.com/en-US/docs/alexa/ask-overviews/create-developer-account.html">sign up here</a> *FREE)
* An Alexa-enabled device (useful for additional testing)
* Amazon Alexa app on mobile device

<h3>Customizing Your Alexa Skill</h3>

<p>
After cloning the ‘school-menu-alexa’ repository to your machine, you can begin customizing it to create your own Alexa skill for reading your school's menu.

<h4>For Schools Using SchoolCafe’s Menu System:</h4>

If your school is already using SchoolCafe, you will need to update the environmental variables to match your student’s credentials. See below for the necessary credentials and an example of how they are structured:

```
SCHOOL_ID = "9fg858fc-357b-44be-8693-07f574f659g5"
GRADE = "04"
PERSON_ID = “27b6414e-a43e-3d4c-ac91-5397a30b7f17”

```

<strong>Important Note:</strong> The PERSON_ID variable is distinct from your student's school ID. This is a unique identifier used specifically by SchoolCafe for each student. You can find it in the URL when logged into the student’s SchoolCafe account.

</p>



<h2>Resources :bulb:</h2>
See this guide from the Alexa Workshop that details building an Alexa Skill: <a href="https://developer.amazon.com/en-US/docs/alexa/workshops/build-an-engaging-skill/get-started/index.html?sc_category=Paid&sc_channel=SEM&sc_campaign=ASK-cta-q2-23&sc_publisher=GO&sc_content=Banner&sc_detail=GetStarted&sc_funnel=Awareness&sc_country=WW&sc_medium=Paid_SEM_ASK-cta-q2-23_GO_Banner_GetStarted_Awareness_WW_Skill_Builders&sc_segment=Skill_Builders&sc_keyword=how%20to%20create%20alexa%20skill&gclid=Cj0KCQjwuLShBhC_ARIsAFod4fJMfzQiVFRE34seCYRCDpbo9RxNJzfkMDDzdMcFCnRoQUFd9VTGDj4aAomqEALw_wcB">Build an Engaging Alexa Skill</a>

Having trouble getting your skill published? See this guide from Amazon: <a href="https://blueprints.amazon.com/help/publish-your-skill">Publish your skill to the Alexa Skills store</a>
