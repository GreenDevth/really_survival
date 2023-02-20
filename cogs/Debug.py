import discord
from discord.ext import commands
from db.town import City
class DebugCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="check_player")
    async def check_player(self, ctx, member):
        data = City().citizen(member)
        await ctx.send(f"{data}")


def setup(bot):
    bot.add_cog(DebugCommand(bot))