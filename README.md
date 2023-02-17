# WhisperBot

WhisperBot is a Telegram bot that allows you to send secret or confidential messages to selected members of a group without others knowing about it. It works in inline mode, meaning you don't need to add the bot to the group to use it. You just need to mention the bot in the chat, and it will help you send two different messages to the same group: one visible to everyone and the other visible only to selected members.

This is a useful feature for people who want to share important information with only a few members of a group without revealing it to everyone. With WhisperBot, you can have more control over your conversations and protect your sensitive data.


## How to use
To use WhisperBot, simply follow these steps:

1. Open a group chat where you want to send a secret message.

2. Type `@Whisper_Bot` followed by your target members usernames or IDs and your message, using the following format: <br>
`@Whisper_Bot username1, username2, user_id3 || message1 || message2`. <br>
The first message will be visible only to the members you select, while the second message will be visible to everyone in the group.

3. Send the message by clicking on the inline result shown by the bot, and WhisperBot will take care of the rest.


## Running the Bot Locally

To run the bot locally, follow these steps:

1. Clone the repository: 
``` bash 
git clone https://github.com/sobirjonovme/WhisperBot.git
```

2. Create a virtual environment and activate it:

```bash
python -m venv env
source env/bin/activate # for Linux/Mac
.\env\Scripts\activate # for Windows
```

3. Install the required packages:

``` bash
pip install -r requirements.txt
```

4. Create a `.env` file based on the `.env.dist` file and add your Telegram Bot token. 

5. Run the bot using the command:

``` bash
python main.py
```

##### Now you can use the bot with your own Telegram bot token. Enjoy! 
