#   libraries
import discord
import config
import random

#   variables
bot = discord.Client()
ancmt = bot.get_channel('759670370558541845')

@bot.event
async def on_ready():
    print('sadopy is ready')

@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    if msg.content == "-sadopy":
        await msg.add_reaction("<:downvote:931014167559798835>")
        options = ["Sadopy is making some dosas. Leave him alone","Chad","SIUUUUUUUUU","Sadopy is training",
        "Sadopy is having tea right now","https://giffiles.alphacoders.com/138/13815.gif",
        "https://c.tenor.com/YXkNDKQBHTgAAAAd/chad-attacks-nothing-sado-yasutora.gif",
        "Stop bothering Sadopy",
        "Go back to work"]
        await msg.channel.send(random.choice(options))
        return

@bot.event
async def on_member_join(user):
    sends = []

@bot.event
async def on_member_remove(user):
    sens=[]

bot.run(config.token)