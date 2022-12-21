import asyncio

import discord


class ContactCloseButton(discord.ui.View):
    def __init__(self, bot):
        super(ContactCloseButton, self).__init__(timeout=None)
        self.bot = bot

    @discord.ui.button(label="close", style=discord.ButtonStyle.danger, emoji="🔐", custom_id="close_contact")
    async def close_contact(self, button, interaction:discord.Interaction):
        button.disabled=False
        embed = discord.Embed(
            title="⚠️ ระบบกำลังทำการปิดห้องติดต่อนี้ใน 10 วินาที",
            color=discord.Colour.from_rgb(226, 35, 32)
        )
        await interaction.response.edit_message(content=None, embed=embed, view=None)
        await asyncio.sleep(10)
        return await interaction.channel.delete()