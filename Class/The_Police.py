import random

import discord
from discord.utils import get
from discord.ext import commands
from discord.commands import SlashCommandGroup, Option
from db.Events import ThePolice, Event_list
from db.town import City

from scripts.guilds import guild_data
from func.config import img_

from session.SessionContent import police_event

guild_id = guild_data()["realistic"]
role_list = ["Bandit", "Police"]
class ThePoliceCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(__class__.__name__, " is ready")
        self.bot.add_view(ThePoliceGet())



    police = SlashCommandGroup(guild_ids=[guild_id], name="police", description="คำสั่งจัดการอีเว้นสกัดกั้นการขนย้ายอาวุธ")


    @police.command(name="เปิดคำสั่งใช้งานอีเว้น",description="คำสั่งเปิดการแสดงคำสั่งลงทะเบียนเลือกหน้าที่โดยหัวหน้าหมู่บ้าน")
    async def prolice_event(
            self,
            ctx:discord.Interaction,
            select:Option(str, "เลือกคำสั่งที่ต้องการ", choices=["Enabled", "Disabled"])
    ):
        choice = ["Enabled", "Disabled"]
        guild = ctx.guild

        if select == choice[0]:
            cate_name = "EVENT REGISTER"
            ch_name = "🚧-ด่าน"
            overwrites={
                guild.default_role:discord.PermissionOverwrite(
                    send_messages=False
                )
            }
            try:
                category = discord.utils.get(guild.categories, name=cate_name)
                if category:
                    channel = discord.utils.get(guild.channels, name=ch_name)
                    if channel:
                        await channel.send(embed=police_event(), view=ThePoliceGet())
                        return await ctx.response.send_message("เปิดการใช้งานฟังก์ชั่นการลงทะเบียนเรียบร้อย",
                                                       ephemeral=True)
                else:
                    category = await guild.create_category(name=cate_name, overwrites=overwrites)
                    channel = await guild.create_text_channel(name=ch_name, category=category)
                    await channel.edit(sync_permissions=True)
                    try:
                        if channel:
                            await channel.send(embed=police_event(), view=ThePoliceGet())
                            return await ctx.response.send_message("เปิดการใช้งานฟังก์ชั่นการลงทะเบียนเรียบร้อย",
                                                           ephemeral=True)
                    except Exception as e:
                        print(e)

            except Exception as e:
                return await ctx.response.send_message(e)





    @commands.command(name="police")
    async def police_event(self, ctx):
        member = ctx.author
        await ctx.message.delete()
        guild = ctx.guild
        room_name = "📝-ผู้ใช้งาน-id-{}".format(member.discriminator)



        channel = get(guild.channels, name=room_name)
        if ctx.channel == channel and member == ctx.author:
            await ctx.send(embed=police_event(), view=ThePoliceGet())
        else:
            return await ctx.send(f"กรุณาพิมพ์คำสั่งของคุณที่ห้อง {channel.mention} เท่านั้น", delete_after=5)


class ThePoliceGet(discord.ui.View):
    def __init__(self):
        super(ThePoliceGet, self).__init__(timeout=None)

    @discord.ui.button(label="คลิกเพื่อทำการจับฉลาก", style=discord.ButtonStyle.secondary, custom_id="get_role_police")
    async def get_role_police(self, button, interaction:discord.Interaction):
        button.disabled=False
        member = interaction.user
        police_list = Event_list().police_list()
        city = City().citizen(member.id)[1]

        def get_item_list():

            while True:
                try:
                    match = random.randint(1, len(police_list))
                    if match in police_list:
                        Event_list().update_police_list(city, member.id, match)
                        print(match)
                        return match
                    else:
                        pass
                except Exception as e:
                    print(e)

        if len(police_list) == 0:
            return await interaction.response.send_message("ระบบทำการจับฉลากครบแล้ว", ephemeral=True)

        if City().citizen(interaction.user.id)[3] == 1:
            data = Event_list().event(get_item_list())
            embed= discord.Embed(
                title="ผู้ต้องสงสัย" if data[0]== "bandit" else "Police",
            )
            embed.add_field(name="เมือง", value=data[1])
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            await interaction.response.send_message("คุณไม่ใช่หัวหน้าทีม ไม่สามารถใช้งานคำสั่งนี้ได้", ephemeral=True)


        