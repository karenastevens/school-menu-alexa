<h1>Willow Dale Menu - Alexa Skill</h1> <img src="https://i.imgur.com/I4EbBQV.png"/>

This respository contains the code for an Alexa skill that allows users to hear the current breakfast and lunch menu for a specific school. The skill is written in Python and uses the AWS Lambda function and Alexa Skills kit to access the data.

<h2>Prerequisites :nut_and_bolt:</h2>

* An Amazon Web Services (AWS) account (<a href="https://aws.amazon.com/free/?trk=78b916d7-7c94-4cab-98d9-0ce5e648dd5f&sc_channel=ps&s_kwcid=AL!4422!3!432339156165!e!!g!!create%20aws%20account&ef_id=Cj0KCQiAic6eBhCoARIsANlox86TYDv0SwS8ZeHSBz83fubw5sXAhH_TBkWOhPDbwLqhL2emHYOICfgaAhIMEALw_wcB:G:s&s_kwcid=AL!4422!3!432339156165!e!!g!!create%20aws%20account&all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all">you can sign up here</a> *FREE)
* An Amazon Developer account (<a href="https://developer.amazon.com/en-US/docs/alexa/ask-overviews/create-developer-account.html">sign up here</a> *FREE)
* An Alexa-enabled device (useful for additional testing)
* Amazon Alexa app on mobile device

<h2>Setup</h2>

1. Create a new skill in the Alexa Developer Console
    - Name your skill
    - Choose 'Custom' for model
    - Choose 'Alexa-hosted (Python) for Hosting services
    - Choose 'Start from Scratch' for Templates
    - Click 'Create' and wait for 'Build Completed' message
2. Navigate to 'Skill Invocation Name' and change the skill invocation name relevant to your school. For example, this school uses 'willow dale menu'.
3. Navigate to 'Interaction Model' > 'Intents' and add and intent for each request you wish to add to the skill. For example this skill currently uses, 'BreakfastIntent', 'LunchIntent', 'LunchandBreakfastIntent', 'BreakfastTomorrowIntent', 'LunchTomorrowIntent', 'LunchandBreakfastTomorrowIntent'. These will be defined in the lambda function. Save and Build Model when adding intents.
4.
