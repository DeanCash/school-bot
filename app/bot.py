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

# 

bot.run(bot.token)
