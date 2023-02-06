import discord
from discord.ext import commands
from scripts.guilds import guild_data


guild_id = guild_data()["realistic"]
manage_member = ["🌐-join-server", "👋-good-bye"]

class JoinerMember(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member:discord.Member):
        guild = self.bot.get_guild(guild_id)
        channel = discord.utils.get(guild.channels, name=manage_member[0])
        await discord.DMChannel.send(member, "Welcome to Realistic Survival - Community")
        await channel.send(f'{member.mention} Join to discord server')
        print("New Member Joined in Discord Server")


    @commands.Cog.listener()
    async def on_member_remove(self, member:discord.Member):
        guild = self.bot.get_guild(guild_id)
        channel = discord.utils.get(guild.channels, name=manage_member[1])
        await channel.send(f'Goodbye {member.display_name}')
        print("Memeber has been leave from discord server")



def setup(bot):
    bot.add_cog(JoinerMember(bot))