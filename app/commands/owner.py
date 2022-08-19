from discord.ext import commands
from discord.ext.commands import Context

class Owner(commands.Cog, description="Commands only the owner of the bot can use"):
    def __init__(self, bot: str) -> None:
        self.bot = bot

    @commands.command(name="lolmaoo")
    async def dwasdwa(self, ctx: Context):
        await ctx.send("WORKS!")

def setup(bot):
    bot.add_cog(Owner(bot))
