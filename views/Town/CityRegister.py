import discord
from discord.ext import commands

from func.city import city_embed
from func.config import get_cooldown_time
from views.Town.City import CityRegisterButton


class CityRegisterConfirm(discord.ui.View):
    def __init__(self, bot):
        self.bot = bot
        super(CityRegisterConfirm, self).__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, int(get_cooldown_time()), commands.BucketType.member)

    @discord.ui.button(label="กดที่ปุ่มเพื่อจดทะเบียนประชากร",emoji="👉", style=discord.ButtonStyle.secondary, disabled=True)
    async def city_register_lable(self, button, interaction:discord.Interaction):
        await interaction.response.send_message("ok")
        button.disabled = False

    @discord.ui.button(label="จดทะเบียนประชากร", style=discord.ButtonStyle.success, emoji="📝", custom_id="city_register_confirm")
    async def city_regs_confirm(self, button, interaction:discord.Interaction):
        button.disabled=False
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f'อีก {round(retry, int(get_cooldown_time()))} วินาที คำสั่งถึงจะพร้อมใช้งานอีกครั้ง', ephemeral=True)
        return await interaction.response.edit_message(content="",embed=city_embed(), view=CityRegisterButton(self.bot))