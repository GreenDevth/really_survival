import discord
from discord.commands import user_command
from discord.ext import commands
from discord.utils import get

from db.users import Users
from scripts.guilds import guild_data
from views.Members.MemberViews import UsersViews

guild_id = guild_data()["realistic"]


class UserCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(__class__.__name__, " is ready")

    @user_command(guild_ids=[guild_id])
    async def profile(self, ctx, member:discord.Member):
        guild = ctx.guild
        room_name = "📝-ผู้ใช้งาน-id-{}".format(member.discriminator)
        cat_name = "USER PROFILES"
        if ctx.author != member:
            return await ctx.respond(f"{member.mention} ไม่อนุญาตให้ใช้งานคำสั่งของผู้ใช้อื่น", delete_after=5)
        if Users().check(member.id) == 0:
            return await ctx.respond(f"{member.mention} คำสั่งสำหรับสมาชิกเท่านั้น", delete_after=5)
        await ctx.respond("System in prgress !!!!",delete_after=3)
        msg = await ctx.send("ระบบกำลังสร้างห้อง โปรไฟล์ใหม่ให้กับคุณ")

        try:
            channel = get(guild.channels, name=room_name)
            if channel is None:
                cate = discord.utils.get(guild.categories, name=cat_name)
                register_channel = await guild.create_text_channel(name=room_name, category=cate)
                await register_channel.edit(sync_permissions=True, )
                await register_channel.set_permissions(member, view_channel=True, send_messages=True,
                                                       read_message_history=True, read_messages=True)
        except Exception as e:
            await msg.edit(content=e, delete_after=5)
        else:
            channel = get(guild.channels, name=room_name)
            await channel.purge()
            img = discord.File('./img/member/member_profile.png')
            await channel.send(file=img, view=UsersViews(self.bot))
            return await msg.edit(content=f"{member.mention} ไปยังหน้า {channel.mention} ของคุณ", delete_after=3)



