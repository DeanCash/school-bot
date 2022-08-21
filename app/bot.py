import os
import sys
import asyncio
import colorama

import discord
from discord.ext import commands, tasks
from discord.ext.commands import Context
from discord.message import Message

from assets.data import *

from colorama import Fore, Style
colorama.init(autoreset=True)

# fixes sibling import bug
sys.path.append("..")

intents: discord.Intents = discord.Intents.all()
bot = commands.Bot(command_prefix, intents=intents, activity=discord.Activity(type=discord.ActivityType.watching, name="SSD-2A"))
bot.token = bot_token

print(f" {log_app}Application Started")

@bot.event
async def on_ready():
    print(f" {log_bot}{bot.user} is ready :D\n")

@bot.event
async def on_message(message: Message):
    await bot.process_commands(message)


for file in os.listdir(os.path.join("app", "commands")):
    if file.endswith(".py"):
        bot.load_extension(f"commands.{file[:-3]}")


bot.run(bot.token)
