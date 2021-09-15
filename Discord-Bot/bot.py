import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    the_office_quotes = [
        'Would I rather be feared or loved? Easy. Both. I want people to be afraid of how much they love me.',
        'I\'m not superstitious, but I am a little stitious.',
        'The worst thing about prison was the dementors.',
        'Identity theft is not a joke, Jim! Millions of families suffer every year.',
    ]

    if message.content == 'speak!':
        response = random.choice(the_office_quotes)
        await message.channel.send(response)

client.run(TOKEN)