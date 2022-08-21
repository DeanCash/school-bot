import os
import json

from discord.ext.commands import Context
from discord.message import Message

import colorama
from colorama import Fore
colorama.init(autoreset=True)

command_prefix = '!'

log_app = f"[{Fore.RED}APPLICATION{Fore.RESET}] >> "
log_bot = f"[{Fore.BLUE}BOT{Fore.RESET}] >> "
log_error = f"[{Fore.LIGHTRED_EX}ERROR{Fore.RESET}] >> "
log_illegal = f"{Fore.LIGHTRED_EX}[{Fore.RESET}ILLEGAL{Fore.LIGHTRED_EX}]{Fore.RESET} >> "
pr_err = f"{Fore.LIGHTRED_EX}!{Fore.RESET}"
log_event = f"[{Fore.CYAN}EVENT{Fore.RESET}] >> "
log_owner = f"[{Fore.YELLOW}OWNER{Fore.RESET}] >> "
log_command = lambda x: f"[{Fore.YELLOW}COMMAND{Fore.RESET}] | {x} >> "

shorten = lambda s, l: s[:l] + ' ...' if len(s) > l else s
log_message_len = 50

token_file = os.path.join("app", "private", "secrets.json")
with open(token_file, "r") as f:
    bot_token: str = json.load(f)['TOKEN']

# - - - - - - - - - - - - - - - - - - #
def bold(msg: str) -> str:
    return f"**{msg}**"

def italic(msg: str) -> str:
    return f"__{msg}__"

def strike(msg: str) -> str:
    return f"__{msg}__"

def quote(msg: str) -> str:
    return f"`{msg}`"

def to_mention(user_id: int) -> str:
    return f"<@{user_id}>"

def to_channel(channel_id: int) -> str:
    return f"<#{channel_id}>"
