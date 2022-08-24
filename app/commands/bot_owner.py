import discord
from discord.ext import commands
from discord.ext.commands import MemberConverter, Context
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


    @commands.command(name="test")
    async def debug(self, ctx: Context, num: int):
        await ctx.send(f"NUMBER: {num}")

    @commands.command(name="renamebot")
    async def change_bot_name(self, ctx: Context, new_username: str):
        await self.bot.user.edit(username=new_username)

    @commands.command(name="dm")
    async def dm_user(self, ctx: Context, user: MemberConverter):
        user: discord.user.User = await self.bot.fetch_user(int(user.id))
        await user.send(" ".join(["a"]))


def setup(bot: commands.Bot):
    bot.add_cog(Owner(bot))





# testing
if __name__ == "__main__":
    test = Owner(commands.Bot('!'))
