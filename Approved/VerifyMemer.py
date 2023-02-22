import discord
from discord.ext import commands
from discord.commands import slash_command, Option

from db.users import Users


class VerifyMemberCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(self.__class__.__name__)

    @slash_command(name="verify")
    async def verify_command(self, ctx:discord.Interaction, member:Option(discord.Member, "เลือกผู้ใช้งานที่ต้องการ Verify")):

        if Users().check(member.id) != 1:
            return await ctx.response.send_message(f"ไม่พบข้อมูลของ {member.mention}", ephemeral=True)
        else:
            try:
                if Users().player(member.id)[6] == 1:
                    pass
                else:
                    Users().approved(member.id)
                    await discord.DMChannel.send(member, "คุณได้รับการ Verify จากระบบเป็นที่เรียบร้อยแล้ว")
                    return await ctx.response.send_message(f"ระบบทำการ Verify ให้กับ {member.mention} เป็นที่เรียบร้อยแล้ว", ephemeral=True)
            except Exception as e:
                return await ctx.response.send_message(e, ephemeral=True)
            else:
                return  await ctx.response.send_message(f"{member.mention} ได้ทำการ Verify ไว้เรียบร้อยแล้ว", ephemeral=True)
