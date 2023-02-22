import discord

from discord.ext import commands
from discord.commands import slash_command, Option

from db.users import Users
from scripts.guilds import guild_data

guild_id = guild_data()["realistic"]

class UserWalletCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(self.__class__.__name__)

    @slash_command(name="wallet")
    async def wallet_command(self, ctx:discord.Interaction, method:Option(str, "เลือกรูปแบบที่ต้องการ", choices=["add", "remove"]), member:Option(discord.Member, "เลือกผู้ใช้งาน"), amount:Option(int, "ระบุจำนวนที่ต้องการ")):
        await ctx.response.defer(ephemeral=True, invisible=False)
        msg = await ctx.followup.send("ระบบกำลังดำเนินการให้กับคุณ")

        if method == "add":
            try:
                old = Users().wallet(member.id)
                new = old + amount
                Users().wallet_update(member.id, new)
            except Exception as e:
                return await msg.edit(content=e)
            else:
                return await msg.edit(content="เพิ่ม Wallet จำนวน ฿{:d} ให้กับ {} เรียบร้อย".format(amount, member.mention))
