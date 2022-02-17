import discord
from discord.ext import commands


intents = discord.Intents.all()
client = commands.Bot(command_prefix='*', intents=intents)


@client.command(name="on")
async def on(context):
    await context.message.channel.send("/tts")
    await context.message.channel.send("O pai tá on!")

client.run('OTQzNTcwNjIxMjI3NDc0OTY0.Yg0-ng.8YhHGQjEpIhb22rZBUe8XQf9Mzg')
