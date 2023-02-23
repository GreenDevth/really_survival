import discord

from discord.ext import commands
from discord.commands import slash_command, Option

from Banks.Bank_db import Bank
from db.users import Users
from scripts.guilds import guild_data

guild_id = guild_data()["realistic"]

class UserWalletCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(self.__class__.__name__)

    @slash_command(name="bank")
    async def bank_command(
            self,
            ctx:discord.Interaction,
            member:Option(discord.Member,"เลือกผู้ใช้งาน")
    ):
        await ctx.response.defer(ephemeral=True, invisible=False)
        msg = await ctx.followup.send("ระบบกำลังประมวลผล โปรดรอสักครู่")

        try:
            if Bank().check_member(member.id) != 1:
                return await msg.edit(content=f"ไม่พบข้อมูลของ {member.mention} ในระบบ")
            else:
                total = Bank().coins(member.id)
                old = Users().wallet(member.id)
                Users().wallet_update(member.id, total + old)
                Bank().update(member.id, 0)
                await discord.DMChannel.send(member, "ระบบทำการจ่ายค่ารางวัลภารกิจจำนวน ${:,d} ไปยังบัญขี Wallet เป็นที่เรียบร้อย".format(total))
                return await msg.edit(content=f"โอนเงินให้กับ {member.mention} เป็นที่เรียบร้อย")
        except Exception as e:
            return await msg.edit(content=e)

    @slash_command(name="wallet")
    async def wallet_command(
            self,
            ctx:discord.Interaction,
            method:Option(str, "เลือกรูปแบบที่ต้องการ", choices=["add", "remove"]),
            member:Option(discord.Member, "เลือกผู้ใช้งาน"),
            amount:Option(int, "ระบุจำนวนที่ต้องการ"),
            reason:Option(str, "พิมพ์หมายเหตุของคุณ", default=None)
    ):
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
                def reason_msg():
                    if reason:
                        return reason
                    else:
                        return "..."
                await discord.DMChannel.send(member, "คุณได้รับ Wallet จำนวน ${} จากระบบ : หมายเหตุ {}".format(amount, reason_msg()))
                return await msg.edit(content="เพิ่ม Wallet จำนวน ${:d} ให้กับ {} เรียบร้อย".format(amount, member.mention))
