import discord
from discord.utils import get
from discord.ext import commands
from discord.commands import SlashCommandGroup, Option
from db.Events import ThePolice
from db.town import City

from scripts.guilds import guild_data

guild_id = guild_data()["realistic"]
role_list = ["Bandit", "Police"]
class ThePoliceCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    police = SlashCommandGroup(guild_ids=[guild_id], name="police", description="คำสั่งจัดการอีเว้นสกัดกั้นการขนย้ายอาวุธ")

    @commands.command(name="police")
    async def police_event(self, ctx):
        member = ctx.author
        await ctx.message.delete()
        guild = ctx.guild
        room_name = "📝-ผู้ใช้งาน-id-{}".format(member.discriminator)



        channel = get(guild.channels, name=room_name)
        if ctx.channel == channel and member == ctx.author:
            try:
                check = ThePolice().check(member.id)
                town = City().citizen(member.id)[1]
                if check == 1 and ThePolice().town_check(town) == 1:
                    return await ctx.send(f"เจ้าเมืองของ {town} ได้ทำการลงทะเบียนไว้แล้ว")
                else:
                    return await ctx.send("กดที่ปุ่มเพื่อการสุ่มเลือก Role สำหรับอีกเว้นนี้")
            except Exception as e:
                return await ctx.send(e, delete_after=10)
        else:
            return await ctx.send(f"กรุณาพิมพ์คำสั่งของคุณที่ห้อง {channel.mention} เท่านั้น", delete_after=5)


class ThePoliceGet(discord.ui.View):
    def __init__(self, data):
        self.data = data
        super(ThePoliceGet, self).__init__(timeout=60)

    @discord.ui.button(label="คลิกเพื่อทำการจับฉลาก", style=discord.ButtonStyle.secondary, custom_id="get_role_police")
    async def get_role_event_police(self, button, interaction:discord.Interaction):
        button.disabled=False


        