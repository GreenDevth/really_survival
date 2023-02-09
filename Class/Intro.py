import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup, Option

from scripts.guilds import guild_data

guild_id = guild_data()["realistic"]


class IntroEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    intro = SlashCommandGroup(guild_ids=[guild_id], name="intro", description="คำสั่งจัดการ ปฐมบทอีเว้น")

    @intro.command(name="คำสั่งแสดงอีเว้นปฐมบท", description="คำสั่งเปิดใช้งานการแจ้งอีกเว้นปฐมบท")
    async def frist_intro(self, ctx:discord.Interaction):
        guild = ctx.guild
        await ctx.response.defer(ephemeral=True, invisible=False)
        msg = await ctx.followup.send("โปรดรอสักครู่ ระบบกำลังประมวลผล")


        try:
            name = "📰-ข่าวสารจากเซิร์ฟ"
            channel = discord.utils.get(guild.channels, name=name)
            if channel:
                await channel.send('ok')
        except Exception as e:
            print(e)
        else:
            return await msg.edit(content="จัดการระบบเรียบร้อย")