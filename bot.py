import discord
import config
client = discord.Client()

@client.event
async def on_ready():
    print('sado is ready to make dosas!')

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    if msg.content == "-sado":
        for role in msg.author.roles:
            if role.name == 'chad(s)':
                await msg.channel.send("sigma > chad")
                return
        await msg.channel.send("sado makin dosas")
        return
    

client.run(config.token)