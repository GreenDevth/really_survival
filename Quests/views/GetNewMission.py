import datetime
import random

import discord

from Quests.db.Mission_db import Mission, UserMission
from db.users import Users


class GetMissionButton(discord.ui.View):
    def __init__(self):
        super(GetMissionButton, self).__init__(timeout=None)




    @discord.ui.button(label="กดที่ปุ่มเพื่อสุ่มรับภารกิจรายบุคคลของคุณ", style=discord.ButtonStyle.secondary, disabled=True, custom_id="get_mission_disabled")
    async def get_mission_diabled(self, button, interaction):
        await interaction.response.send_message(button.label)

    @discord.ui.button(label="คลิกเพื่อสุ่มภารกิจ", style=discord.ButtonStyle.secondary, emoji="🎲", custom_id="get_mission_button")
    async def get_mission_button(self, button, interaction:discord.Interaction):
        member = interaction.user
        button.disabld=False
        mission_list = Mission().list_id()
        match = random.randint(1, len(mission_list))
        def expire_date():
            now = datetime.datetime.now()
            date_add = now + datetime.timedelta(days=3)
            start = now.strftime("%d/%m/%Y")
            end = date_add.strftime("%d/%m/%Y")
            date_list = [start, end]
            return date_list

        if Users().check(member.id) == 0:
            return await interaction.response.edit_message(content=f"{member.mention} คุณยังไม่ได้รับสิทธิ์ให้ใช้งานระบบ Quest ของเซิร์ฟ", embed=None, view=None)
        elif Users().wallet(member.id) < 50:
            return await interaction.response.edit_message(content=f"{member.mention} :💳 Wallet ของคุณไม่เพียงพอสำหรับปลดล๊อคการใช้งานนี้", embed=None, view=None)

        elif match in mission_list:
            data = Mission().get_mission_by_id(int(match))
            embed = discord.Embed(
                title="📦 {}".format(data[1]),
                description="นำส่งสินค้าให้กับ Guild Master ตามจำนวนและเวลาที่ระบุไว้ในคำสั่ง"
            )
            embed.add_field(name="จำนวนสินค้า", value=data[3])
            embed.add_field(name="ค่าประสบการณ์", value=data[4])
            embed.add_field(name="เงินรางวัล", value=data[5])
            embed.add_field(name="วันที่รับภารกิจ", value="{}".format(expire_date()[0]))
            embed.add_field(name="ครบกำหนดส่งสินค้า", value="{}".format(expire_date()[1]))
            embed.set_image(url=data[2])
            try:
                UserMission().new(member.id, data[1], data[2],data[4], data[5], expire_date()[0], expire_date()[1])
                old = Users().wallet(member.id)
                total = old - 50
                Users().wallet_update(member.id, total)
            except Exception as e:
                return await interaction.response.edit_message(content=e, embed=None, view=None)
            else:
                return await interaction.response.edit_message(content="นี่คือภารกิจที่คุณได้รับ",embed=embed,view=None)