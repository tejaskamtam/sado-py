import discord
import config.py
client = discord.Client()

@client.event
async def on_ready():
    print('sado is ready to make dosas!')

client.run(token)