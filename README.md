<h1>Willow Dale Menu - Alexa Skill</h1> <img src="https://i.imgur.com/I4EbBQV.png"/>

This respository contains the code for an Alexa skill that allows users to hear the current breakfast and lunch menu for a specific school. The skill is written in Python and uses the AWS Lambda function, Alexa Skills kit and an Amazon S3 bucket to access the data.

<h2>Prerequisites :nut_and_bolt:</h2>

* An Amazon Web Services (AWS) account (<a href="https://aws.amazon.com/free/?trk=78b916d7-7c94-4cab-98d9-0ce5e648dd5f&sc_channel=ps&s_kwcid=AL!4422!3!432339156165!e!!g!!create%20aws%20account&ef_id=Cj0KCQiAic6eBhCoARIsANlox86TYDv0SwS8ZeHSBz83fubw5sXAhH_TBkWOhPDbwLqhL2emHYOICfgaAhIMEALw_wcB:G:s&s_kwcid=AL!4422!3!432339156165!e!!g!!create%20aws%20account&all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all">you can sign up here</a> *FREE)
* An Amazon Developer account (<a href="https://developer.amazon.com/en-US/docs/alexa/ask-overviews/create-developer-account.html">sign up here</a> *FREE)
* An Alexa-enabled device (useful for additional testing)
* Amazon Alexa app on mobile device

<h2>Setup :wrench:</h2>

1. Create a new skill in the Alexa Developer Console
    - Name your skill
    - Choose 'Custom' for model
    - Choose 'Alexa-hosted (Python) for Hosting services
    - Choose 'Start from Scratch' for Templates
    - Click 'Create' and wait for 'Build Completed' message
2. Navigate to 'Skill Invocation Name' and change the skill invocation name relevant to your school. For example, this school uses 'willow dale menu'.
3. Navigate to 'Interaction Model' > 'Intents' and add and intent for each request you wish to add to the skill. For example this skill currently uses, 'BreakfastIntent', 'LunchIntent', 'LunchandBreakfastIntent', 'BreakfastTomorrowIntent', 'LunchTomorrowIntent', 'LunchandBreakfastTomorrowIntent'. These will be defined in the lambda function. Save and Build Model when adding intents.
4. Navigate to 'Code' section within console. Copy and paste code into appropriate section. Be sure to adjust paths to accomodate your specific school menu and where you are storing it. Menus shoud be in JSON format.
5. You can then 'Save', 'Deploy' and 'Test' to ensure your skill is giving the expected responses.
6. Submit your skill for Distribution and Certification if you wish to have it published in the Amazon Alexa Skill store!

<h2>Resources :bulb:</h2>
See this guide from the Alexa Workshop that details building an Alexa Skill: <a href="https://developer.amazon.com/en-US/docs/alexa/workshops/build-an-engaging-skill/get-started/index.html?sc_category=Paid&sc_channel=SEM&sc_campaign=ASK-cta-q2-23&sc_publisher=GO&sc_content=Banner&sc_detail=GetStarted&sc_funnel=Awareness&sc_country=WW&sc_medium=Paid_SEM_ASK-cta-q2-23_GO_Banner_GetStarted_Awareness_WW_Skill_Builders&sc_segment=Skill_Builders&sc_keyword=how%20to%20create%20alexa%20skill&gclid=Cj0KCQjwuLShBhC_ARIsAFod4fJMfzQiVFRE34seCYRCDpbo9RxNJzfkMDDzdMcFCnRoQUFd9VTGDj4aAomqEALw_wcB">Build an Engaging Alexa Skill</a>

Having trouble getting your skill published. See this guide from Amazon: <a href="https://blueprints.amazon.com/help/publish-your-skill">Publish your skill to the Alexa Skills store</a>
