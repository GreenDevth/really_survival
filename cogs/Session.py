import discord
from discord.ext import commands



class SessionCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(__class__.__name__, " is ready!")


def setup(bot):
    bot.add_cog(SessionCommand(bot))