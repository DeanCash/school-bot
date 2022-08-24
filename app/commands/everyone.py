import discord
from discord.ext import commands
from discord.ext.commands import MemberConverter, Context
from discord.message import Message
from discord.member import Member
from discord.user import User

from assets.data import *
from assets.converters import *

class Everyone(commands.Cog, name="Public Commands", description="Commands everybody regarding of permissions can use."):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    async def cog_check(self, ctx: Context):
        # if not await ctx.bot.is_owner(ctx.author):
        #     raise commands.NotOwner
        return True


    @commands.command(name="ping")
    async def ping(self, ctx: Context):
        """Ping the bot"""
        latency = (self.bot.latency * 1000)
        latency_embed = discord.Embed(
            title="", description=f"🏓 Bots Latency: {round(latency, 2)}ms", color=bot_color)
        await ctx.send(embed=latency_embed)

    @commands.command(name="quote")
    async def quote_message(self, ctx: Context, *message):
        await ctx.send(f"{' '.join(message)}\n{bold(f'~ {ctx.author}')}")

    @commands.command(name="profile")
    async def profile(self, ctx: Context, user: MemberConverter):
        user: User = self.bot.get_user(user.id)
        embed = discord.Embed(title=f"{user}", url=f"https://lookup.guru/{user.id}", color=bot_color)
        embed.add_field(name="Account Created:", value=f"{format_date(user.created_at)}")
        embed.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user.id}/{user.avatar}.png")
        embed.set_author(name=f"requested by: {ctx.author}", icon_url=f"https://cdn.discordapp.com/avatars/{ctx.author.id}/{ctx.author.avatar}.png")
        embed.set_footer(text=f"ID: {user.id}")
        await ctx.send(embed=embed)

# TODO: CONVERTERS FOR 'profile', 'dm' && GROUPS

def setup(bot: commands.Bot):
    bot.add_cog(Everyone(bot))





# testing
if __name__ == "__main__":
    test = Everyone(commands.Bot('!'))
