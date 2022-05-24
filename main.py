# in this project we'll be coding a bot using python for discord

from discord.ext import commands
import json
import requests

client = commands.Bot(command_prefix = '$')
# we have got our client right now

def get_message():
    resp = requests.get("https://zenquotes.io/api/random")
    # we have got the response portion 
    # now the resp.text is the string containing json
    # next up we have to parse(that is convert to list of dictionaries the json part i.e. resp.text
    
    data = json.loads(resp.text)
    # data is the list of python dictionaries 
    mes = data[0]['q'] + '\n -' + data[0]['a']
    return mes

@client.event
async def on_ready():
    # gives the message on the terminal when the bot is ready to use
    print ('We have logged in as {0.user}'.format(client))

@client.command(aliases = ['encourage'])
async def inspire(mes):
    # we are using asynchronous programming in order to wait for our bot
    # to respond to the message
    await mes.channel.send(get_message())

@client.command(aliases = ['clear', 'cls'])
@commands.is_owner()
async def clean(cont, amount = 5):
    await cont.channel.purge(limit = amount)
    # this deletes the previous amount number of messages 
    # this sends the stats about the time taken to delete amount number of messages

@client.command()
@commands.is_owner()
async def close(cont):
    exit()

client.run('OTcyMDIzMzMyNDIzNzUzNzc4.GqCOoP.jPBEmmrH9vCv3TL3TpCcmApN7qKGA-MZ58UlEc')

