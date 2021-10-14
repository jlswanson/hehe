import os

import discord
from dotenv import load_dotenv

load_dotenv()

# discord bot token
TOKEN = os.getenv('DISCORD_TOKEN')

# initialize the bot
client = discord.Client()

@client.event
async def on_message(message):
    content = f'{message.content} hehe'

    if message.author == client.user:
        return

    if message.content[-1] is not '.':
        await message.channel.send(content)

client.run(TOKEN)