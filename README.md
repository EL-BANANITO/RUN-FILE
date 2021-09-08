
With this code you can run files on many pc. you can use it with telegram-bot-manager to conntroll many pc.

step 1*.
        Create telegram bot for this you need telegram on your pc. Enter @Botfather in the search tab and choose this bot. Choose or type the /newbot command and send it. 
        Choose a name for your bot — your subscribers will see it in the conversation. ... Go to the @BotFather bot and send the command /token .
step 2*.
       enter this token in code main.py example: bot = telebot.TeleBot('1828267547:AAESVt_qMBUtsxVGS7Ag3WTiKWVmqJUkMUY')
step 3*.
       1. Go to the Google APIs Console.
       2. Create a new project.
       3. Click Enable API. ...
       4. Create credentials for a Web Server to access Application Data.
       5. Name the service account and grant it a Project Role of Editor.
       6. Download the JSON file.
       or you can use this video: https://www.youtube.com/watch?v=ct0xvw_Z0tU
step 4*.
       install all libraries: windows: pip install -r requirements.txt Macos and linux: pip3 install -r requirements.txt
step 5*.
       file run.py and .json file must be on pc that you whant to run some file. file main.py must be on other pc or server adn of course all pc's must have connection to internet
commands:
         /help - explain all commands. 
         /start - start bot use only 1 time or if you update something.
         r "hostname" - run file.
         e "hostname" - exit file.
kayboard:
         pc hostnames - show all pc's hostname that have this files on.
