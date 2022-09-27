import os
import sys
import asyncio
import colorama

import discord
from discord.ext import commands, tasks
from discord.ext.commands import Context
from discord.message import Message
from discord.member import Member, User
from discord import Guild

from typing import Union

from assets.data import *

from colorama import Fore, Style
colorama.init(autoreset=True)

# fixes sibling import bug
sys.path.append("..")

intents: discord.Intents = discord.Intents.all()
bot = commands.Bot(command_prefix, intents=intents, help_command=commands.MinimalHelpCommand())
bot.token = bot_token

print(f" {log_app}Application Started")

@bot.event
async def on_ready():
    server: Guild = bot.get_guild(school_server)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{server.member_count} members!"))
    print(f" {log_bot}Logged in as <{Fore.BLUE}{bot.user}{Fore.RESET}>\n")

@bot.event
async def on_message(message: Message):
    # code here
    await bot.process_commands(message)

@bot.event
async def on_reaction_add(emoji: discord.Reaction, user: Union[Member, User]):
    ...


for file in os.listdir(os.path.join("app", "commands")):
    if file.endswith(".py"):
        bot.load_extension(f"commands.{file[:-3]}")


bot.run(bot.token)
