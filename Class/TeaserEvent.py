import discord
from db.Events import TeaserEvent
from discord.ext import commands
from discord.commands import SlashCommandGroup, Option

from scripts.guilds import guild_data

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
            url:Option(str,"ใส่ link รูปภาพแผนที่ของเซ็ตเริ่มต้น")
            ):
        data = [
            title,
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


class NewTeaser(discord.ui.View):
    def __init__(self, bot, data):
        super(NewTeaser, self).__init__(timeout=None)
        self.bot = bot
        self.data = data

    @discord.ui.button(label="insert data", style=discord.ButtonStyle.success, emoji="💾",custom_id="save_to_teaser_db")
    async def save_to_teaser_db(self, button, interaction:discord.Interaction):
        button.disabled=False
        try:
            TeaserEvent().new(self.data[0], self.data[1])
        except Exception as e:
            return await interaction.response.send_message(e)
        else:
            await interaction.response.edit_message(content="บันทึกขัอมูลเรียบร้อย", embed=None, view=None)

