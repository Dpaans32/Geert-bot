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

islam_woorden=["islam", "Islam", "Moslim", "moslim", "allah", "Allah"]
islam_woorden_antwoord=["Onze cultuur is veel beter dan de achterlijke islamitische cultuur", "De Nederlandse cultuur is duizend keer beter dan de islam", "Ik ga er als eerste met cement en stenen heen om die moskeeën dicht te metselen"]

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    mesg = message.content

    if message.content.startswith('!Geert'):
        Msg = getRandom(quotelist)
        await message.channel.send(Msg)
    
    if message.content.startswith('!Fitna'):
        await message.channel.send('Bekijk hier mijn fantastische film over de islam: https://vimeo.com/174087977')

    if message.content.startswith('!Help'):
        await message.channel.send('!Geert: genereert een van mijn quotes\n!Fitna: speelt mijn film over de islam af')

    if any(word in mesg for word in islam_woorden):
        await message.channel.send(random.choice(islam_woorden_antwoord))

client.run(TOKEN)