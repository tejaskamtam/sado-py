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
        "Stop bothering Sadopy", "Go back to work"]
        await msg.channel.send(random.choice(options))
        return

@bot.event
async def on_member_join(user):
    opts = ["{user.mention} has joined among us!","Hey {user.mention}! Welcome to the Unswallowed Committee",
            "{user.mention} joined the server?! LETS GO!!!","{user.mention} joined the server! Salamat, Thanks!"]
    msg = ancmt.send(random.choice(opts))
    await msg
    await msg.add_reaction('<:peepoUpvote:931009571932209152>')


@bot.event
async def on_member_remove(user):
    opts = ["{user.mention} fell down a hole","{user.mention} went to play with some other friends",
            "All my homies hate {user.mention} for leaving the server","{user.mention} bites the dust. F"]
    msg = ancmt.send(random.choice(opts))
    await msg
    await msg.add_reaction('<:downvote:931014167559798835>')


bot.run(config.token)