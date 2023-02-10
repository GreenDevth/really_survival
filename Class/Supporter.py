import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup, Option

from tabulate import tabulate
from db.users import Supporter, Users

from scripts.guilds import guild_data

guild_id = guild_data()['realistic']

class SupporterMembers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    supporter = SlashCommandGroup(guild_ids=[guild_id], name="supporter", description="คำสั่งสำหรับจัดการผู้สนับสนุนเซิร์ฟเวอร์")

    @supporter.command(name="บันทึกผู้สนับสนุนเซิร์ฟเวอร์", description="คำสั่งบันทึกข้อมูลผู้สนับสนุน ผู้เข้าร่วมโครงการ")
    async def new_supporter_recode(
            self,
            ctx:discord.Interaction,
            member:Option(discord.Member, "เลือกผู้ใช้งาน"),
            amount:Option(int,"ระบุจำนวนเงิน")
    ):
        await ctx.response.defer(ephemeral=True, invisible=False)
        msg = await ctx.followup.send("ระบบกำลังประมวลผล")
        try:
            discord_id = member.id
            discord_tag = member.discriminator
            steam_id = Users().player(member.id)[2]
        except Exception as e:
            await msg.edit(content=e)
        else:
            try:
                if Supporter().check(discord_id) == 1:
                    return await msg.edit(content=f"{member.mention} ได้บันทึกข้อมูลไว้แล้ว")
                else:
                    Supporter().new(discord_id,steam_id,discord_tag, amount)
            except Exception as e:
                print(e)
            else:
                await msg.edit(content="บันทึกข้อมูลเรียบร้อยแล้ว")

    @supporter.command(name="แสดงผลรายชื่อผู้สนับสนุน", description="คำสั่งจัดการรายชื่อผู้สนับสนุนทั้งหมด")
    async def show_support_list(
            self,
            ctx:discord.Interaction,
            method:Option(str,"เลือกคำสั่ง", choices=["True", "False"])
    ):

        guild = ctx.guild
        await ctx.response.defer(ephemeral=True, invisible=False)
        msg = await ctx.followup.send("ระบบกำลังประมวลผล")

        if method == "True":
            try:
                data = Supporter().get()
            except Exception as e:
                await msg.edit(content=e)
            else:
                print(data)
        else:
            await ctx.response.send_message('ok',ephemeral=True)