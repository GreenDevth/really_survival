import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup, Option

from db.users import Supporter
from func.config import img_
from scripts.guilds import guild_data

guild_id = guild_data()["realistic"]


class SteamCheckCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    steam = SlashCommandGroup(guild_ids=[guild_id], name="steam", description="คำสั่งตรวจสอบผู้เล่นด้วย steam id")

    @steam.command(name="เช็ตผู้เล่นจากสตรีมไอดี", description="คำสั่งตรวจสอบข้อมูลผู้สมทบค่าเช่าเซิรืฟ")
    async def steam_check(self, ctx:discord.Interaction, steam:Option(str, "ระบบสตรีมไอดีที่ต้องการแสดงข้อมูล")):
        guild = ctx.guild
        await ctx.response.defer(ephemeral=True, invisible=False)

        try:
            for member in guild.members:
                if member.id == int(Supporter().member(steam)):
                    return await ctx.followup.send(member.display_name)
            else:
                pass
        except Exception as e:
            return await ctx.followup.send(e)
        else:
            return await ctx.followup.send(f"ไม่พบข้อมูลของหมายเลขสตรีม {steam} ในระบบ")


    @steam.command(name="ตรวจสอบสตรีมไอดี", description="คำสั่งตรวจสอบไอดีสตรีม")
    async def steam_check(self, ctx:discord.Interaction):
        await ctx.response.defer(ephemeral=True, invisible=False)
        guild = ctx.guild
        discord_id = Supporter().discord_id()
        channel_name = "📃-รายชื่อผู้สมทบทุน"
        try:
            channel = discord.utils.get(guild.channels, name=channel_name)
            for s in discord_id:
                for member in guild.members:
                    if member.id == int(s):
                        embed=discord.Embed(title="Supporter Information")
                        embed.add_field(name="DISCORD", value=member.display_name)
                        embed.add_field(name="ID", value=f"{member.id}")
                        embed.set_thumbnail(url="{}".format(member.display_avatar))
                        embed.set_image(url=img_("reg"))
                        channel_sent = await channel.send(embed=embed)
                        await channel_sent.add_reaction("💾")

        except Exception as e:
            print(e)
        else:
            await ctx.followup.send('successfully')

