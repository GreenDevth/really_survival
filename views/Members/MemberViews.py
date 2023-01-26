import asyncio

import discord
from discord.ext import commands

from db.users import Users
from func.config import get_cooldown_time, steam_check, save_to_db
from func.member import user_info
from func.img import ranking_
from server.information import reg_success
from views.Contract.ContactView import ContractButton


class CloseRequestRegister(discord.ui.View):
    def __init__(self, bot):
        super(CloseRequestRegister, self).__init__(timeout=None)
        self.bot = bot

    @discord.ui.button(label='Close', style=discord.ButtonStyle.secondary, custom_id="close_reg")
    async def close_reg(self, button, interaction):
        button.disabled= False
        await interaction.channel.purge()

        img=discord.File('./img/member/member.png')
        await interaction.channel.send(
            file=img,
            view=UsersViews(self.bot)
        )

class RegisterRequest(discord.ui.View):
    def __init__(self, bot):
        super(RegisterRequest, self).__init__(timeout=None)
        self.bot = bot
        self.cooldown = commands.CooldownMapping.from_cooldown(1, int(60), commands.BucketType.member)

    @discord.ui.button(label="โปรเตรียมรหัสสตรีมไอดีสำหรับลงทะเบียน", style=discord.ButtonStyle.secondary,
                       disabled=True, custom_id="request_reg_disabled")
    async def request_reg_disabled(self, button, interaction):
        await interaction.response.send_message(f"{interaction.user.name} click {button.label}", ephemeral=True)

    @discord.ui.button(label="Register Now", style=discord.ButtonStyle.secondary, custom_id="request_reg")
    async def request_reg(self, button, interaction: discord.Interaction):
        button.disabled = False
        member = interaction.user
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f'อีก {round(retry, int(60))} วินาที คำสั่งถึงจะพร้อมใช้งานอีกครั้ง', ephemeral=True)
        await interaction.response.defer(ephemeral=False, invisible=False)

        def check(res):
            return res.author == interaction.user and res.channel == interaction.channel

        qustion = await interaction.followup.send(f"📝 {member.mention} กรุณาระบุรหัสสตรีมไอดีของคุณ")
        while True:

            try:
                steam = await self.bot.wait_for(event="message", check=check, timeout=60)
                # print(steam.content)
                if steam_check(steam.content):
                    await steam.delete()
                    # print("register successfully...")
                    await qustion.edit(content=None, embed=reg_success(member, steam.content),
                                       view=CloseRequestRegister(self.bot))
                    return save_to_db(member.id, steam.content)
                    # return await discord.DMChannel.send(member, "")
            except asyncio.TimeoutError:
                # print("Progress TimeOut!!!!")
                return await qustion.edit(
                    f"{interaction.user.mention} : คุณใช้เวลาในการกรอกข้อมูลเช้าเกินไป กรุณากดปุ่มเพื่อเริ่มลงทะเบียนใหม่อีกครั้ง")
            else:
                await steam.delete()
                await qustion.edit(content="info not found! Please try agian")
                # print("enter steam id again")

class UsersViews(discord.ui.View):
    def __init__(self, bot):
        super(UsersViews, self).__init__(timeout=None)
        self.bot = bot
        self.cooldown = commands.CooldownMapping.from_cooldown(1, int(get_cooldown_time()), commands.BucketType.member)

    @discord.ui.button(label="ข้อมูลผู้ใช้", style=discord.ButtonStyle.secondary, emoji="📝", custom_id='user_info')
    async def user_info(self, button, interaction:discord.Interaction):
        button.disabled=False
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f'อีก {round(retry, int(get_cooldown_time()))} วินาที คำสั่งถึงจะพร้อมใช้งานอีกครั้ง', ephemeral=True)

        if Users().check(interaction.user.id) == 0:
            return await interaction.response.send_message(f"⚠ {interaction.user.mention} คุณถูกระบบปลดสิทธิ์การเข้าใช้งานเซิร์ฟ ไม่มีข้อมูลของคุณในระบบ", view=RegisterRequest(self.bot))


        await interaction.response.defer(ephemeral=True, invisible=False)
        return await interaction.followup.send(embed=user_info(interaction.user))

    @discord.ui.button(label="กระดานภารกิจ", style=discord.ButtonStyle.secondary, emoji="🎡", custom_id='user_quest')
    async def user_quest(self, button, interaction:discord.Interaction):
        button.disabled=False
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f'อีก {round(retry, int(get_cooldown_time()))} วินาที คำสั่งถึงจะพร้อมใช้งานอีกครั้ง', ephemeral=True)
        embed = discord.Embed(
            title="Ranking information",
            color=discord.Colour.from_rgb(255, 195, 0)
        )
        embed.add_field(name="ผู้ใช้งาน", value=interaction.user.display_name)
        await interaction.response.send_message(f"{interaction.user.mention} click {button.label}")

    @discord.ui.button(label="ติดต่อทีมงาน", style=discord.ButtonStyle.secondary, emoji="☎", custom_id='contact')
    async def contact(self, button, interaction:discord.Interaction):
        button.disabled=False
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f'อีก {round(retry, int(get_cooldown_time()))} วินาที คำสั่งถึงจะพร้อมใช้งานอีกครั้ง', ephemeral=True)
        await interaction.response.send_message(f"{interaction.user.mention} click ที่ปุ่มด้านล่างเพื่อเลือกคำสั่งที่ต้องการ", view=ContractButton(self.bot), ephemeral=True)