import discord
from discord.ext import commands
from dotenv import dotenv_values
import os

config = dotenv_values(".env")
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='.', intents=intents)

@client.event
async def on_ready():
    print(f'{client.user}: Tryna strike a chord and it\'s probably A-minooorrrr')
    
    for filename in os.listdir("./commands"):    
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await client.load_extension(f"commands.{filename[:-3]}")

client.run(config["TOKEN"])
