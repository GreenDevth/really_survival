import asyncio
import random

import discord
from discord.ext import commands

from Class.TeaserEvent import GetTeaser
from db.Events import TeaserEvent
from db.Ranking import Ranking
from db.town import City
from db.users import Users
from func.config import get_cooldown_time, steam_check, save_to_db, get_quest, img_
from func.member import user_info
from func.rank import ranking_img
from server.information import reg_success
from views.Contract.ContactView import ContractButton
from views.Town.CityRegister import CityRegisterConfirm


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
        if City().city(interaction.user.id) == 0:
            return await interaction.followup.send(embed=user_info(interaction.user), view=CityRegisterConfirm(self.bot))
        if City().city(interaction.user.id) == 1:
            return await interaction.followup.send(embed=user_info(interaction.user))

    @discord.ui.button(label="กระดานภารกิจ", style=discord.ButtonStyle.secondary, emoji="🎡", custom_id='user_quest')
    async def user_quest(self, button, interaction:discord.Interaction):
        button.disabled=False
        member = interaction.user
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()

        if retry:
            return await interaction.response.send_message(
                f'อีก {round(retry, int(get_cooldown_time()))} วินาที คำสั่งถึงจะพร้อมใช้งานอีกครั้ง', ephemeral=True)

        try:
            if Ranking().check(interaction.user.id) == 0:
                Ranking().new_rank(interaction.user.id)
        except Exception as e:
            print(e)

        if get_quest() == "Close":
            return await interaction.response.send_message("ขออภัยระบบเควสยังไม่เปิดใช้งานในขนะนี้", ephemeral=True)


        if TeaserEvent().event_count() == 0:
            rank = Ranking().ranking(interaction.user.id)[2]
            embed = discord.Embed(
                title="Ranking information",
                color=discord.Colour.from_rgb(255, 195, 0)
            )
            embed.add_field(name="ผู้ใช้งาน", value=interaction.user.display_name)
            embed.add_field(name="ค่าประสบการณ์", value=Ranking().ranking(interaction.user.id)[3])
            embed.set_thumbnail(url=ranking_img(rank))
            embed.set_image(url=img_("rank_embed"))
            return await interaction.response.send_message(embed=embed, ephemeral=True)

        if TeaserEvent().event_count() != 0: # หากระบบมีการอัพเดท Event เข้ามา ให้ทำการเช็ค ภารกิจของผู้เล่นอีกครั้ง
            # check ผู้เล่นว่ากดรับภารกิจไปแล้วหรือยัง
            if TeaserEvent().check(interaction.user.id) != 0: # แสดงผล หาก ผู้เล่นมีภารกิจคงค้างอยู่
                if TeaserEvent().my_teaser(interaction.user.id)[8] == 0:
                    data = TeaserEvent().my_teaser(interaction.user.id)
                    embed = discord.Embed(
                        title=f"ชื่อภารกิจ : {data[1]}",
                        description=f"เมื่อทำภารกิจสำเร็จ ผู้เล่นจะได้รับ exp หรือค่าประสบการณ์จำนวน {data[6]}exp โดยนำรหัสลับ (secret code) มากรอกให้กับระบบ",
                        colour=discord.Colour.from_rgb(245, 176, 65)
                    )
                    embed.set_image(url=data[4])
                    embed.set_footer(text=f"คำใบ้ : {data[5]}")
                    return await interaction.response.send_message(f"{interaction.user.mention} คุณมี 1 ภารกิจประจำสัปดาห์นี้", embed=embed,view=SecretCode(self.bot))
                else:
                    rank = Ranking().ranking(interaction.user.id)[2]
                    embed = discord.Embed(
                        title="Ranking information",
                        color=discord.Colour.from_rgb(255, 195, 0)
                    )
                    embed.add_field(name="ผู้ใช้งาน", value=interaction.user.display_name)
                    embed.add_field(name="ค่าประสบการณ์", value=Ranking().ranking(interaction.user.id)[3])
                    embed.set_thumbnail(url=ranking_img(rank))
                    embed.set_image(url=img_("rank_embed"))
                    return await interaction.response.send_message(embed=embed, ephemeral=True)





            else:
                if TeaserEvent().check(member.id) == 0:
                    img = discord.File('./img/event/startpack.png')
                    return await interaction.response.send_message(file=img, view=GetTeaser(self.bot))





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


# ระบบกดปุ่มรับภารกิจ

class GetQuest(discord.ui.View):
    def __init__(self, bot, quest):
        super(GetQuest, self).__init__(timeout=None)
        self.bot = bot
        self.quest = quest
    @discord.ui.button(label="กดที่ปุ่มเพื่อรับภารกิจประจำสัปดาห์", style=discord.ButtonStyle.secondary, disabled=True, custom_id="get_quest_disabled")
    async def get_quest_disabled(self, button, interaction:discord.Interaction):
        button.disabled=False,
        await interaction.response.send_message(interaction.user.mention, f"click {button.label}")
    @discord.ui.button(label="กดรับภารกิจของคุณที่นี่", style=discord.ButtonStyle.secondary, emoji="🎲", custom_id="get_quest_button")
    async def get_quest_button(self, button, interaction:discord.Interaction):
        button.disabled = False
        user = interaction.user
        embed = discord.Embed(
            title=self.quest[1],
            colour=discord.Colour.from_rgb(15, 115, 51)
        )
        embed.set_image(url=self.quest[4])
        await interaction.response.edit_message(content=f"{user.mention} ระบบส่งข้อมูลภารกิจไปยัง กล่องข้อความของคุณเรียบร้อย", embed=None, view=None)
        return await discord.DMChannel.send(user, embed=embed)


class SecretCode(discord.ui.View):
    def __init__(self, bot):
        super(SecretCode, self).__init__(timeout=None)
        self.bot = bot


    @discord.ui.button(label="กดที่ปุ่ม เพื่อกรอกรหัสลับที่ได้จากกล่อง", style=discord.ButtonStyle.secondary, disabled=True, custom_id="disable_code_lock")
    async def disable_code_lock(self, button, interaction:discord.Interaction):
        button.disabled=False
        await interaction.response.send_message(button.label)
    @discord.ui.button(label="กดเพื่อกรอกรหัสลับ", style=discord.ButtonStyle.secondary, emoji="📝", custom_id="enter_code_lock")
    async def enter_code_lock(self, button, interaction:discord.Interaction):
        member = interaction.user
        await interaction.response.defer(ephemeral=True, invisible=False)
        await interaction.channel.purge(limit=1)
        msg = await interaction.followup.send("📝 กรุณาพิมพ์รหัสลับที่ได้จากกล่อง")
        button.disabled=True

        def check(res):
            return res.author == interaction.user and res.channel == interaction.channel
        while True:
            try:

                message = await self.bot.wait_for(event="message", check=check, timeout=60)
                teaser = TeaserEvent().my_teaser(interaction.user.id)[0]
                exp = TeaserEvent().my_teaser(member.id)[6]
                secret = TeaserEvent().get(teaser)[2]
                await message.delete()
                if message.content == secret:
                    try:
                        TeaserEvent().seccess(secret)
                        Ranking().update_exp(member.id, exp)
                    except Exception as e:
                        print(e)
                    else:

                        return await msg.edit(content=f"🎊 ยินดีด้วยคุณได้รับ {TeaserEvent().my_teaser(interaction.user.id)[6]} EXP สำหรับภารกิจนี้")
                else:
                    print(message.content, secret)
                    text = [
                        "คุณกรอกข้อมูลไม่ถูกต้องกรุณาลองใหม่อีกครั้ง",
                        "ข้อมูลไม่ถูกต้อง ลองใหม่อีกครั้ง",
                        "ข้อมูลที่คุณกรอกยังไม่ถูกต้อง ลองใหม่อีกครั้ง"
                    ]
                    await msg.edit(content=random.choice(text))
            except asyncio.TimeoutError:
                return await msg.edit(content="โปรดกรอกรหัสลับภายในระยะเวลา 1 นาที")

