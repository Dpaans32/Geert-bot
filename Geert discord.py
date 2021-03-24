import os
import ssl

import random
import Gbot
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

f = open("Geert.txt", "r")
quotelist = []

for quote in f.readlines():
    quotelist.append(quote.replace('\n', ''))
    quotelist.append(quote.replace("Ã«", "ë"))

f.close()

def getRandom(list):
    return random.choice(list)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!Geert'):
        Msg = getRandom(quotelist)
        await message.channel.send(Msg)

client.run(TOKEN)