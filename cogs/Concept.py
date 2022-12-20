from discord.ext import commands
from story.Storied import story_one


class ServerInformation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(__class__.__name__)

    @commands.command()
    async def story_one(self, ctx):
        await ctx.send(embed=story_one())

def setup(bot):
    bot.add_cog(ServerInformation(bot))
    