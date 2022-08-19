import os
import time
import json
import asyncio
import colorama
import importlib

import discord
from discord.ext import commands, tasks
from discord.ext.commands import Context

from assets.data import *

from colorama import Fore, Style
colorama.init(autoreset=True)

intents: discord.Intents = discord.Intents.all()
bot = bot = commands.Bot(command_prefix, intents=intents, activity=discord.Activity(type=discord.ActivityType.watching, name="SSD-2A"))
bot.token = bot_token

print(f" {pr_app}Application Started")

@bot.event
async def on_ready():
    print(f" {pr_bot}Bot is ready :D")

for file in os.listdir(os.path.join("app", "commands")):
    if file.endswith(".py"):
        bot.load_extension(f"commands.{file[:-3]}")

bot.run(bot.token)
