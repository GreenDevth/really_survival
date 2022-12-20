import discord
from discord.ext import commands

from func.config import get_cooldown_time


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
        await interaction.response.send_message(f"{interaction.user.mention} click {button.label}")

    @discord.ui.button(label="กระดานภารกิจ", style=discord.ButtonStyle.secondary, emoji="🎡", custom_id='user_quest')
    async def user_quest(self, button, interaction:discord.Interaction):
        button.disabled=False
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f'อีก {round(retry, int(get_cooldown_time()))} วินาที คำสั่งถึงจะพร้อมใช้งานอีกครั้ง', ephemeral=True)
        await interaction.response.send_message(f"{interaction.user.mention} click {button.label}")

    @discord.ui.button(label="ติดต่อแอดมิน", style=discord.ButtonStyle.secondary, emoji="☎", custom_id='contract')
    async def contract(self, button, interaction:discord.Interaction):
        button.disabled=False
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f'อีก {round(retry, int(get_cooldown_time()))} วินาที คำสั่งถึงจะพร้อมใช้งานอีกครั้ง', ephemeral=True)
        await interaction.response.send_message(f"{interaction.user.mention} click {button.label}")