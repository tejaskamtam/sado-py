#   libraries
import discord
import config
import random

bot = discord.Client

# Custom Bot class
class Bot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print('sadopy is ready')
    
    async def on_message(self, msg):
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
    
    async def on_member_join(self, user):
        opts = ["{user.mention} has joined among us!","Hey {user.mention}! Welcome to the Unswallowed Committee",
                "{user.mention} joined the server?! LETS GO!!!","{user.mention} joined the server! Salamat, Thanks!"]
        ancmt = bot.get_channel(config.ancmtid)
        msg = ancmt.send(random.choice(opts))
        await msg
        await msg.add_reaction('<:peepoUpvote:931009571932209152>')
    
    async def on_member_remove(self, user):
        opts = ["{user.mention} fell down a hole","{user.mention} went to play with some other friends",
                "All my homies hate {user.mention} for leaving the server","{user.mention} bites the dust. F"]
        ancmt = bot.get_channel(config.ancmtid)
        msg = ancmt.send(random.choice(opts))
        await msg
        await msg.add_reaction('<:downvote:931014167559798835>')

client = Bot()
client.run(config.token)
