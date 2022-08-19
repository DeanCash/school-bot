import os
import json

from discord.ext.commands import Context
from discord.message import Message

import colorama
from colorama import Fore
colorama.init(autoreset=True)

command_prefix = '!'

pr_app = f"[{Fore.RED}APPLICATION{Fore.RESET}] >> "
pr_bot = f"[{Fore.BLUE}BOT{Fore.RESET}] >> "
pr_error = f"[{Fore.LIGHTRED_EX}ERROR{Fore.RESET}] >> "
pr_event = f"[{Fore.CYAN}EVENT{Fore.RESET}] >> "
pr_command = lambda x: f"[{Fore.YELLOW}COMMAND{Fore.RESET}] | {x} >> "

token_file = os.path.join("app", "private", "token.json")
with open(token_file, "r") as f:
    bot_token: str = json.load(f)['TOKEN']

# - - - - - - - - - - - - - - - - - - #
def bold(msg: str) -> str:
    return f"**{msg}**"

def italic(msg: str) -> str:
    return f"__{msg}__"

def strike(msg: str) -> str:
    return f"__{msg}__"

def code(msg: str) -> str:
    return f"`{msg}`"

def to_mention(user_id: int) -> str:
    return f"<@{user_id}>"

def to_channel(channel_id: int) -> str:
    return f"<#{channel_id}>"
