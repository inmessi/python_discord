
## Discord bot using discord.py module

#### Description
This discord bot can perform two operations:
1. Command '$encourage' or '$inspire': The bot will return a random motivational quote.
2. Command '$clear': This will enable the bot to clear the previous n messages. If the number of messages to be deleted is not given as input then it will clear the previous 5 messages. 

#### Running python app locally
```sh
$ python3 main.py
```

#### Deploying python bot to heroku
Files you must have in order to deploy your python app to heroku:
- Procfile 
- main.py
- requirements.txt (Type the following in your terminal to create requirements.txt)
```sh
$ pip freeze > requirements.txt
```
- runtime.txt
 
Go through these files to know how they work. 

Link to heroku: [https://dashboard.heroku.com/apps](https://dashboard.heroku.com/apps). <br/>
Open the above mentioned link and then go to terminal to type the following:
```sh
$ heroku git:clone -a inmessi
$ cd inmessi
$ git add . && git commit -m 'done'
$ git push heroku master 
```
Or simply connect this repository and you're done.

