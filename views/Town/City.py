import discord
from discord.ext import commands

from db.users import Users
from func.config import get_cooldown_time


class CityRegisterButton(discord.ui.View):
    def __init__(self, bot):
        super(CityRegisterButton, self).__init__(timeout=None)
        self.bot = bot
        self.cooldown = commands.CooldownMapping.from_cooldown(1, int(get_cooldown_time()), commands.BucketType.member)

    @discord.ui.button(label="City A", style=discord.ButtonStyle.secondary, emoji="🏠", custom_id="city_a")
    async def city_a(self, button, interaction:discord.Interaction):
        button.disabled=False
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f"อีก {round(retry, int(get_cooldown_time()))} วินาที คำสั่งถึงจะพร้อมใช้งานได้อีกครั้ง", ephemeral=True
            )
        if Users().check(interaction.user.id) != 0:
            return await interaction.response.send_message(interaction.user.mention, ephemeral=True)

    @discord.ui.button(label="City B", style=discord.ButtonStyle.secondary, emoji="🏠", custom_id="city_b")
    async def city_b(self, button, interaction:discord.Interaction):
        button.disabled=False
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f"อีก {round(retry, int(get_cooldown_time()))} วินาที คำสั่งถึงจะพร้อมใช้งานได้อีกครั้ง", ephemeral=True
            )
        if Users().check(interaction.user.id) != 0:
            return await interaction.response.send_message(interaction.user.mention, ephemeral=True)

    @discord.ui.button(label="City C", style=discord.ButtonStyle.secondary, emoji="🏠", custom_id="city_c")
    async def city_c(self, button, interaction: discord.Interaction):
        button.disabled = False
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f"อีก {round(retry, int(get_cooldown_time()))} วินาที คำสั่งถึงจะพร้อมใช้งานได้อีกครั้ง", ephemeral=True
            )
        if Users().check(interaction.user.id) != 0:
            return await interaction.response.send_message(interaction.user.mention, ephemeral=True)

    @discord.ui.button(label="City D", style=discord.ButtonStyle.secondary, emoji="🏠", custom_id="city_d")
    async def city_d(self, button, interaction: discord.Interaction):
        button.disabled = False
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f"อีก {round(retry, int(get_cooldown_time()))} วินาที คำสั่งถึงจะพร้อมใช้งานได้อีกครั้ง", ephemeral=True
            )
        if Users().check(interaction.user.id) != 0:
            return await interaction.response.send_message(interaction.user.mention, ephemeral=True)