import discord
from discord.utils import get
from discord.ext import commands
from discord.commands import SlashCommandGroup, Option



from scripts.guilds import guild_data
from views.Members.MemberViews import UsersViews

guild_id = guild_data()["realistic"]


class MemberProfile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="player")
    async def i_player(self, ctx):
        member = ctx.author
        await ctx.message.delete()
        guild = ctx.guild
        cat_name = "USER PROFILES"
        room_name = "📝-ผู้ใช้งาน-id-{}".format(member.discriminator)
        try:
            channel = get(guild.channels, name=room_name)
            if ctx.channel == channel and member == ctx.author:
                await channel.purge()
                img = discord.File('./img/member/member_profile.png')
                return await channel.send(file=img, view=UsersViews(self.bot))
        except Exception as e:
            return await ctx.send(e, delete_after=5)
        else:
            return await ctx.send(f"กรุณาพิมพ์คำสั่งของคุณที่ห้อง {channel.mention} เท่านั้น", delete_after=5)

def setup(bot):
    bot.add_cog(MemberProfile(bot))