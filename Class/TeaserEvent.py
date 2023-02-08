import random

import discord
from db.Events import TeaserEvent
from discord.ext import commands
from discord.commands import SlashCommandGroup, Option

from scripts.guilds import guild_data
from func.config import get_teaser
from func.Teaser import teaser_list

guild_id = guild_data()["realistic"]


class TeaserEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    teaser = SlashCommandGroup(guild_ids=[guild_id], name="teaser", description="คำสั่งจัดการอีเว้นตามหาเซ็ตเริ่มต้น")


    @teaser.command(name="เพิ่มข้อมูลเซ็ตเริ่มต้น", description="คำสั่งเพิ่มข้อมูลสำหรับเซ็ตเริ่มต้น")
    async def teaser_insert(
            self,
            ctx:discord.Interaction,
            title:Option(str,"กำหนดชื่อให้กำเซ็ตเริ่มต้น"),
            secret_code:Option(str,"ใส่รหัสลับของคุณ"),
            url:Option(str,"ใส่ link รูปภาพแผนที่ของเซ็ตเริ่มต้น")
            ):
        data = [
            title,
            secret_code,
            url
        ]
        await ctx.response.defer(ephemeral=True, invisible=False)
        embed = discord.Embed(
            title=title,
            colour=discord.Colour.from_rgb(240, 96, 19)
        )
        embed.set_image(url=url)
        msg = await ctx.followup.send("โปรดรอสักครู่ระบบกำลังประมวลผลการทำงาน")

        await msg.edit(content=None, embed=embed, view=NewTeaser(self.bot, data))


    @commands.Cog.listener()
    async def on_ready(self):
        print(__class__.__name__, " is ready on server")



    @commands.command(name="teaser")
    async def i_tearser(self, ctx):
        guild = ctx.guild
        member = ctx.author
        room_name = "📝-ผู้ใช้งาน-id-{}".format(member.discriminator)
        teaser_id = list(TeaserEvent().teaser_list())
        await ctx.message.delete()
        if len(teaser_id) == 0:
            return await ctx.send(f"{member.mention} ระบบยังไม่มีภารกิจใหม่ในอาทิตย์นี้",delete_after=5)
        if get_teaser() == "Close":
            return await ctx.send(
                f"{member.mention} ยังไม่ภารกิจสำหรับตอนนี้", delete_after=5)
        try:
            channel = discord.utils.get(guild.channels, name=room_name)
            if ctx.author == member and ctx.channel == channel:
                if TeaserEvent().check(member.id) == 1:
                    my_teaser = TeaserEvent().my_teaser(member.id)
                    return await ctx.send(my_teaser)
                elif TeaserEvent().check(member.id) == 0:
                    img = discord.File('./img/event/startpack.png')
                    return await ctx.send(file=img,view=GetTeaser(self.bot))

            else:
                return await ctx.send(f"กรุณาพิมพ์คำสั่งของคุณที่ห้อง {channel.mention} เท่านั้น", delete_after=5)

        except Exception as e:
            return await ctx.send(e, delete_after=10)



class NewTeaser(discord.ui.View):
    def __init__(self, bot, data):
        super(NewTeaser, self).__init__(timeout=None)
        self.bot = bot
        self.data = data

    @discord.ui.button(label="insert data", style=discord.ButtonStyle.success, emoji="💾",custom_id="save_to_teaser_db")
    async def save_to_teaser_db(self, button, interaction:discord.Interaction):
        button.disabled=False
        try:
            TeaserEvent().new(self.data[0], self.data[1], self.data[2])
        except Exception as e:
            return await interaction.response.send_message(e)
        else:
            await interaction.response.edit_message(content="บันทึกขัอมูลเรียบร้อย", embed=None, view=None)



class GetTeaser(discord.ui.View):
    def __init__(self, bot):
        super(GetTeaser, self).__init__(timeout=None)
        self.bot = bot


    @discord.ui.button(label="กดที่ปุ่มเพื่อรับภารกิจเริ่มต้นของคุณ", style=discord.ButtonStyle.secondary, disabled=True, custom_id="get_teaser_disabled")
    async def teaser_label(self, button, interaction:discord.Interaction):
        button.disabled=False
        await interaction.response.send(button.label)


    @discord.ui.button(label="รับแผนที่ตำแหน่ง", style=discord.ButtonStyle.secondary, emoji="🗺",custom_id="get_teaser_frist")
    async def get_teaser_frist(self, button, interaction:discord.Interaction):
        button.disabled=False
        member = interaction.user
        await interaction.response.defer(ephemeral=True, invisible=False)
        msg = await interaction.followup.send("ระบบกำลังจับคู่ภารกิจให้กับคุณ ⏳โปรดรอสักครู่")
        teaser_id = list(TeaserEvent().teaser_list())
        if len(teaser_id) == 0:
            await interaction.channel.purge(limit=1)
            return await msg.edit(content="ภารกิจชุดที่ 1 ได้ส่งมอบให้ผู้เล่นหมดแล้ว")


        def get_item_list():

            while True:
                try:
                    match = random.randint(1,3)
                    if match in teaser_id:
                        TeaserEvent().update_list(member.id, match)
                        return match
                    else:
                        pass
                except Exception as e:
                    print(e)



        # ตรวจสอบว่าผู้เล่นได้กดรับภารกิจไปแล้วหรือยัง
        if TeaserEvent().check(member.id) == 0:
            data = TeaserEvent().teaser(get_item_list())
            print(data)
            embed = discord.Embed(
                title=data[1],
                color=discord.Colour.from_rgb(255,50,66)
            )
            embed.set_image(url=data[4])
            return await msg.edit(content=f"นี่คือแผนที่ตำแหน่งสินค้าของคุณ", embed=embed)


