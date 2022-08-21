import discord
from discord.ext import commands
from discord.ext.commands import Context
from discord.message import Message
from discord.ext.commands.errors import *

from assets.data import *
from assets.converters import *

class Owner(commands.Cog, name="Owner Commands", description="Commands only the owner(s) of the bot can use."):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    async def cog_check(self, ctx: Context):
        if not await ctx.bot.is_owner(ctx.author):
            raise commands.NotOwner
        return True


    @commands.Cog.listener()
    async def on_command_error(self, ctx: Context, error):
        if 0: ...
        elif isinstance(error, commands.NotOwner):
            await ctx.send(f"Only the owner(s) of the bot can use this command `{self.bot.command_prefix}{ctx.invoked_with}`")
            print(f" {log_illegal}{ctx.author} used illegal command -> {shorten(ctx.message.content, log_message_len)}")
        elif isinstance(error, commands.ConversionError):
            await ctx.send(f"Incorrect command syntax!")
            print(f" {log_error}{ctx.author} commands syntax error -> {ctx.message.content}")
        elif isinstance(error, BadArgument):
            await ctx.send(f"Incorrect command syntax!")
            print(f" {log_error}{ctx.author} commands syntax error -> {ctx.message.content}")
        else:
            print(f"{Fore.RED}{error}{Fore.RESET}")
            print(f"{Fore.RED}{type(error)}{Fore.RESET}")


    @commands.command(name="test")
    async def debug(self, ctx: Context, num: int):
        await ctx.send(f"NUMBER: {num}")

    @commands.command(name="renamebot")
    async def change_bot_name(self, ctx: Context, new_username: str):
        await self.bot.user.edit(username=new_username)

    @commands.command(name="dm")
    async def dm_user(self, ctx: Context, user_id: int):
        print(1)
        user: discord.user.User = await self.bot.fetch_user(int(user_id))
        await user.send(" ".join(["a"]))


def setup(bot: commands.Bot):
    bot.add_cog(Owner(bot))





# testing
if __name__ == "__main__":
    test = Owner(commands.Bot('!'))
