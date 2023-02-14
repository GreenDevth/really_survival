import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup, Option

from db.users import Supporter
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

    @steam.command(name="แสดงรายชื่อผู้สมทบทุนทั้งหมด",description="คำสั่งแสดงผุ้สมทบทุนทั้งหมด")
    async def all_support_list(self, ctx:discord.Interaction):
        guild = ctx.guild
        await ctx.response.defer(ephemeral=True, invisible=False)

        try:
            steam_list = Supporter().steam_id()
            for s in steam_list:
                embed=discord.Embed(title="รายชื่อผู้สมทบทุน")
                for member in guild.members:
                    if member.id == int(s):
                        embed.add_field(name="ชื่อสมาชิก", value=member.display_name)
                    else:
                        pass
                await ctx.followup.send(embed=embed)

        except Exception as e:
            await ctx.followup.send(e)
        else:
            await ctx.followup.send('successfully.')

    @steam.command(name="ตรวจสอบสตรีมไอดี", description="คำสั่งตรวจสอบไอดีสตรีม")
    async def steam_check(self, ctx:discord.Interaction):
        guild = ctx.guild
        # await ctx.response.send_message(len(Supporter().steam_id()))

        for x in Supporter().steam_id():
            discord_id = Supporter().member(x)
            await ctx.response.send_message(guild.get_member(int(discord_id)).display_name)
        return await ctx.followup.send("successfully!!!!")
