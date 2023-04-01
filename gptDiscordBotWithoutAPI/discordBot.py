import apiManager
import discord
from discord.ext import commands
import askGpt

Bot = commands.Bot(intents=discord.Intents.all(), command_prefix='!')

#token reseted.
DISCORD_TOKEN = ""

@Bot.event
async def on_ready():
    print("Bot is ready !")

@Bot.command()
async def gpt(ctx):
    question = ctx.message.content[5:]
    apiManager.setter("question", question)
    askGpt.run()
    apiManager.getter("question")
    answer = apiManager.getter("answer")
    answer = str(answer)
    await ctx.send(answer)

Bot.run(DISCORD_TOKEN)
