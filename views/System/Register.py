import asyncio

import discord
from discord.ext import commands

from db.users import Users
from func.config import steam_check, save_to_db
from server.information import reg_success, success_register
from views.Members.MemberViews import UsersViews


class CloseRegisterButton(discord.ui.View):
    def __init__(self, bot, steam_id):
        super(CloseRegisterButton, self).__init__(timeout=None)
        self.bot = bot
        self.steam = steam_id
    @discord.ui.button(label="กดที่ปุ่ม Close เพื่อโหลดหน้าโปรไฟล์ของคุณ", style=discord.ButtonStyle.secondary, disabled=True, custom_id="confirm_close_reg_label")
    async def confirm_close_reg_label(self, button, interaction):
        button.disabled=False
        await interaction.response.send_message("ok")

    @discord.ui.button(label='Close', style=discord.ButtonStyle.danger, custom_id="close_reg")
    async def close_reg(self, button, interaction:discord.Interaction):
        button.disabled= False
        await interaction.channel.purge()
        guild = interaction.guild

        img=discord.File('./img/member/member_profile.png')
        await interaction.channel.send(
            file=img,
            view=UsersViews(self.bot)
        )
        try:
            cate_name = "REGISTER REPORT"
            overwrites = {
                guild.default_role:discord.PermissionOverwrite(
                    send_messages=False
                )
            }

            cate = discord.utils.get(guild.categories, name=cate_name)
            if cate:
                pass
            else:
                cate = await guild.create_category(name=cate_name, overwrites=overwrites)
            channel_name = "📝-รายชื่อผู้ลงทะเบียน"
            channel = discord.utils.get(guild.channels,name=channel_name)
            if channel:
                pass
            else:
                channel = await guild.create_text_channel(name=channel_name, category=cate)
        except Exception as e:
            print(e)
        else:
            add_reaction = await channel.send(embed=success_register(interaction.user,self.steam))
            await add_reaction.add_reaction("🔐")

class RegisterButton(discord.ui.View):
    def __init__(self, bot):
        super(RegisterButton, self).__init__(timeout=None)
        self.bot = bot
        self.cooldown = commands.CooldownMapping.from_cooldown(1, int(60), commands.BucketType.member)

    @discord.ui.button(label="โปรเตรียมรหัสสตรีมไอดีสำหรับลงทะเบียน", style=discord.ButtonStyle.secondary, disabled=True, custom_id="steam_reg_disabled")
    async def steam_reg_disabled(self, button, interaction):
        await interaction.response.send_message(f"{interaction.user.name} click {button.label}", ephemeral=True)

    @discord.ui.button(label="Register Now", style=discord.ButtonStyle.secondary, custom_id="steam_reg")
    async def steam_reg(self, button, interaction:discord.Interaction):
        button.disabled = False
        member = interaction.user
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f'อีก {round(retry, int(60))} วินาที คำสั่งถึงจะพร้อมใช้งานอีกครั้ง', ephemeral=True)
        await interaction.response.defer(ephemeral=False, invisible=False)

        if Users().check(member.id) == 1:
            await interaction.response.send_message(f"{member.mention} ขออภัยขณะนี้จำนวนผู้ลงทะเบียนเต็มแล้ว", ephemeral=True)

        def check(res):
            return res.author == interaction.user and res.channel == interaction.channel
        qustion = await interaction.followup.send(f"📝 {member.mention} กรุณาระบุรหัสสตรีมไอดีของคุณ")
        while True:

            try:
                steam = await self.bot.wait_for(event="message", check=check, timeout=60)
                # print(steam.content)
                if steam_check(steam.content):
                    steam_id = steam.content
                    await steam.delete()
                    # print("register successfully...")
                    await qustion.edit(content=None, embed=reg_success(member, steam.content), view=CloseRegisterButton(self.bot, steam_id))
                    return save_to_db(member.id, steam.content)
                    # return await discord.DMChannel.send(member, "")
            except asyncio.TimeoutError:
                # print("Progress TimeOut!!!!")
                await qustion.edit(f"{interaction.user.mention} : คุณใช้เวลาในการกรอกข้อมูลเช้าเกินไป กรุณากดปุ่มเพื่อเริ่มลงทะเบียนใหม่อีกครั้ง")
                await asyncio.sleep(5)
                return await qustion.delete()
            else:
                await steam.delete()
                await qustion.edit(content="info not found! Please try agian")
                # print("enter steam id again")

