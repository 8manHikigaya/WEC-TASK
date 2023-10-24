import mysql.connector
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
prefix = "!"
bot = commands.Bot(command_prefix = prefix, help_command = None, intents= intents)
token = "MTE2NjI5MjkzMjM3OTI3OTQxMA.GF4lvW.Fjnmn4-e-n5-W0WUiA6JvMMMiMzZS384BYHIws"

@bot.event
async def on_ready():
    print("Online")
bot.run(token)