
## Discord bot using discord.py module

#### Running python app locally
```sh
$ python3 main.py
```

#### Deploying python bot to heroku
Files you must have in order to deploy your python app to heroku:
- Procfile 
- main.py
- requirements.txt <br/>
Type the following in your terminal to create requirements.txt
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

