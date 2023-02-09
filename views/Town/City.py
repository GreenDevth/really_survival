import discord
from discord.ext import commands

from db.town import City
from db.users import Users
from func.config import get_cooldown_time, img_
from func.member import user_info
from views.Town.Func import id_card


class CityRegConfirm(discord.ui.View):
    def __init__(self, bot, data):
        super(CityRegConfirm, self).__init__(timeout=None)
        self.bot = bot
        self.data = data
        self.cooldown = commands.CooldownMapping.from_cooldown(1, int(get_cooldown_time()), commands.BucketType.member)

    @discord.ui.button(label="ยืนยัน", style=discord.ButtonStyle.success, custom_id="yes_btn")
    async def yes_btn(self, button, interaction:discord.Interaction):
        button.disabled=False
        city_name = self.data[0]
        guild = interaction.guild
        member = interaction.user
        try:
            City().new_citizen(city_name, self.data[1])
            Users().update_city(city_name, self.data[1])
            role = discord.utils.get(guild.roles, name=city_name)

        except Exception as e:
            return await interaction.response.send_message(e, ephemeral=True)

        else:
            await member.add_roles(role)
            return await interaction.response.edit_message(content="",embed=user_info(interaction.user), view=None)

    @discord.ui.button(label="ยกเลิก", style=discord.ButtonStyle.danger, custom_id="no_btn")
    async def no_btn(self, button, interaction:discord.Interaction):
        button.disabled=False
        embed =discord.Embed(
            title="ยกเลิกการจดทะเบียนเรียบร้อย ✅",
            colour=discord.Colour.from_rgb(244, 208, 63)
        )
        await interaction.response.edit_message(content="", embed=embed, view=None)


class CityRegisterButton(discord.ui.View):
    def __init__(self, bot):
        super(CityRegisterButton, self).__init__(timeout=None)
        self.bot = bot
        self.cooldown = commands.CooldownMapping.from_cooldown(1, int(get_cooldown_time()), commands.BucketType.member)

    @discord.ui.button(label="A", style=discord.ButtonStyle.secondary, emoji="📝", custom_id="city_a")
    async def city_a(self, button, interaction:discord.Interaction):
        button.disabled=False
        city_name = "Alexandria"
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f"อีก {round(retry, int(get_cooldown_time()))} วินาที คำสั่งถึงจะพร้อมใช้งานได้อีกครั้ง", ephemeral=True
            )
        if City().citizen_count(city_name) == 7:
            return await interaction.response.send_message(f"เมือง {city_name} มีผู้เล่นจดทะเบียนครบแล้ว", ephemeral=True)
        if Users().check(interaction.user.id) != 0:
            if City().city(interaction.user.id) == 0:
                citizen_info = [
                    city_name,
                    interaction.user.id,

                ]
                embed = discord.Embed(
                    title=f"ยืนยันการลงทะเบียนเป็นพลเมืองของ {city_name}",
                    colour=discord.Colour.from_rgb(255, 255, 255)
                )
                embed.set_image(url=img_(city_name))
                return await interaction.response.edit_message(content="", embed=embed,
                                                               view=CityRegConfirm(self.bot, citizen_info))
            else:
                return await interaction.response.send_message(embed=id_card(interaction.guild, interaction.user.id))

    @discord.ui.button(label="B", style=discord.ButtonStyle.secondary, emoji="📝", custom_id="city_b")
    async def city_b(self, button, interaction:discord.Interaction):
        button.disabled=False
        city_name = "Kingdom"
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f"อีก {round(retry, int(get_cooldown_time()))} วินาที คำสั่งถึงจะพร้อมใช้งานได้อีกครั้ง", ephemeral=True
            )
        if City().citizen_count(city_name) == 7:
            return await interaction.response.send_message(f"เมือง {city_name} มีผู้เล่นจดทะเบียนครบแล้ว", ephemeral=True)
        if Users().check(interaction.user.id) != 0:
            if City().city(interaction.user.id) == 0:
                citizen_info = [
                    city_name,
                    interaction.user.id,

                ]
                embed = discord.Embed(
                    title=f"ยืนยันการลงทะเบียนเป็นพลเมืองของ {city_name}",
                    colour=discord.Colour.from_rgb(255, 255, 255)
                )
                embed.set_image(url=img_(city_name))
                return await interaction.response.edit_message(content="", embed=embed,
                                                               view=CityRegConfirm(self.bot, citizen_info))
            else:
                return await interaction.response.send_message(embed=id_card(interaction.guild, interaction.user.id))

    @discord.ui.button(label="C", style=discord.ButtonStyle.secondary, emoji="📝", custom_id="city_c")
    async def city_c(self, button, interaction: discord.Interaction):
        button.disabled = False
        city_name = "Savior"
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f"อีก {round(retry, int(get_cooldown_time()))} วินาที คำสั่งถึงจะพร้อมใช้งานได้อีกครั้ง", ephemeral=True
            )
        if City().citizen_count(city_name) == 7:
            return await interaction.response.send_message(f"เมือง {city_name} มีผู้เล่นจดทะเบียนครบแล้ว", ephemeral=True)
        if Users().check(interaction.user.id) != 0:
            if City().city(interaction.user.id) == 0:
                citizen_info = [
                    city_name,
                    interaction.user.id,

                ]
                embed = discord.Embed(
                    title=f"ยืนยันการลงทะเบียนเป็นพลเมืองของ {city_name}",
                    colour=discord.Colour.from_rgb(255, 255, 255)
                )
                embed.set_image(url=img_(city_name))
                return await interaction.response.edit_message(content="", embed=embed, view=CityRegConfirm(self.bot, citizen_info))
            else:
                return await interaction.response.send_message(embed=id_card(interaction.guild, interaction.user.id))

    @discord.ui.button(label="D", style=discord.ButtonStyle.secondary, emoji="📝", custom_id="city_d")
    async def city_d(self, button, interaction: discord.Interaction):
        button.disabled = False
        city_name = "Commonwealth"
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f"อีก {round(retry, int(get_cooldown_time()))} วินาที คำสั่งถึงจะพร้อมใช้งานได้อีกครั้ง", ephemeral=True
            )
        if City().citizen_count(city_name) == 7:
            return await interaction.response.send_message(f"เมือง {city_name} มีผู้เล่นจดทะเบียนครบแล้ว", ephemeral=True)
        if Users().check(interaction.user.id) != 0:
            if City().city(interaction.user.id) == 0:
                citizen_info = [
                    city_name,
                    interaction.user.id,

                ]
                embed = discord.Embed(
                    title=f"ยืนยันการลงทะเบียนเป็นพลเมืองของ {city_name}",
                    colour=discord.Colour.from_rgb(255, 255, 255)
                )
                embed.set_image(url=img_(city_name))
                return await interaction.response.edit_message(content="", embed=embed,
                                                               view=CityRegConfirm(self.bot, citizen_info))
            else:
                return await interaction.response.send_message(embed=id_card(interaction.guild, interaction.user.id))

    @discord.ui.button(label="E", style=discord.ButtonStyle.secondary, emoji="📝", custom_id="city_e")
    async def city_e(self, button, interaction: discord.Interaction):
        button.disabled = False
        city_name = "Hilltop"
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f"อีก {round(retry, int(get_cooldown_time()))} วินาที คำสั่งถึงจะพร้อมใช้งานได้อีกครั้ง", ephemeral=True
            )
        if City().citizen_count(city_name) == 7:
            return await interaction.response.send_message(f"เมือง {city_name} มีผู้เล่นจดทะเบียนครบแล้ว",
                                                           ephemeral=True)
        if Users().check(interaction.user.id) != 0:
            if City().city(interaction.user.id) == 0:
                citizen_info = [
                    city_name,
                    interaction.user.id,

                ]
                embed = discord.Embed(
                    title=f"ยืนยันการลงทะเบียนเป็นพลเมืองของ {city_name}",
                    colour=discord.Colour.from_rgb(255, 255, 255)
                )
                embed.set_image(url=img_(city_name))
                return await interaction.response.edit_message(content="", embed=embed,
                                                               view=CityRegConfirm(self.bot, citizen_info))
            else:
                return await interaction.response.send_message(embed=id_card(interaction.guild, interaction.user.id))