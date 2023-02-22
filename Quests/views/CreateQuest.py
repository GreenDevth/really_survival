import discord

from Quests.db.Mission_db import Mission


class CreateMissionButton(discord.ui.View):
    def __init__(self, bot, data):
        super(CreateMissionButton, self).__init__(timeout=None)
        self.bot = bot
        self.data = data

    @discord.ui.button(label="Accept", style=discord.ButtonStyle.success, emoji="💾", custom_id="new_mission_create")
    async def new_mission_create(self, button, interaction:discord.Interaction):
        button.disabled=False


        try:
            Mission().new(self.data[0], self.data[1], self.data[2], self.data[3], self.data[4])
        except Exception as e:
            return await interaction.response.send_message(e, ephemeral=True)
        else:
            return await interaction.response.edit_message(content="บันทึกข้อมูลสำเร็จ", view=None, embed=None)
    @discord.ui.button(label="Reject", style=discord.ButtonStyle.secondary, custom_id="mission_create_reject")
    async def mission_create_reject(self, button, interaction:discord.Interaction):
        button.disabled=False
        return await interaction.response.edit_message(content="ยกเลิกรายการเรียบร้อย", view=None, embed=None)
