import discord
import requests
from discord.ext import commands

from scripts.guilds import scum_uri, get_cooldown_time

auth = scum_uri()["battle_token"]
head = {'Authorization': 'Brarer' + auth}

def server_info():
    res = requests.get(scum_uri()["server_url"], headers=head)
    return res.json()

info = "" \
       "- Server ( Taipeh ) IP : 92.223.86.34:28702 [ 30 Slot ]\n" \
       "- ลงทะเบียนขอสิทธิ์เข้าใช้งานเซิร์ฟเวอร์เกมส์ และถูกตัดสิทธิ์ทันทีเมื่อออกจากดิสคอร์ด\n" \
       "- ดรอปไอเทมตามพื้น 0.3% และไอเท็มที่ต้องค้นหา 0.5% ในทุก ๆ 1 ชั่วโมง ดรอปยานพาหนะอย่างละ 5 คัน\n" \
       "- ปิดการใช้งาน Outpost ใช้การแลกเปลี่ยนสินค้าระหว่างผู้เล่นแทน\n" \
       "- ปิดการใช้งานแผนที่ ปาร์ตี้สูงสุด 4 คน อาชญากรและคนเร่ร่อนไม่สามารถสร้างบ้านได้\n" \
       "- จำแหนกประเภทประชากร มีการจดทะเบียน สวมบทบาทอาชีพ และฉายา\n" \
       "- Max Zombie 250 ดาเมจเท่ากับ 3.0% ดาเมจผู้เล่นด้วยกัน เท่ากับ 0.1%\n" \
       "- การป้องกันด้วยช๊อตไฟฟ้า 100% และไม่มีดาเมจบ้าน (ในพื้นที่รกร้าง)\n" \
       "- พื้นที่ชุมชนและศูนย์ราชการ จะเป็นพื้นที่ปลอดภัย แต่มีดาเมจจากรถและซอมบี้\n" \
       "- จำนวนคะแนนที่ใช้เกิด Random 1 FP, Sector 5, Shelter 10 FP\n" \
       "- ยานพาหนะและกล่องไม้จะทำลายตัวเองใน 15 วันหากไม่มีการใช้งาน\n" \
       "- รีเซิร์ฟทุก 6 ชั่วโมง กลางวัน 3.8 ชั่วโมง และกลางคืน 1 ชั่วโมง\n"

law = "" \
       "- Really Survival - Community\n" \
       "- ผู้เล่น 90 % เป็นวัยทำงาน กรุณาให้เกียรติและควรใช้คำพูดสุภาพ\n" \
       "- สิ่งใดที่คิดว่ามีผลกระทบต่อเซิร์ฟเวอร์และอาจสร้างความเดือดร้อนให้ผู้อื่น ขอให้งดพฤติกรรมดังกล่าว\n" \
       "- การปล้นฆ่าสามารถทำได้ตลอดเวลาในพื้นที่รกร้าง\n" \
       "- วางระเบิดนอกเขตธงเป็นสิ่งที่ไม่แนะนำ\n" \
       "- ระบบดิสคอร์ดถือเป็นทรัพย์สินส่วนบุคคลการสร้างความเสียหายให้ระบบโดยเจตนาถือเป็นความผิดร้ายแรง\n" \
       "- การแฮ๊ก หรือการใช้ช่องโหว่ของเกมส์สร้างความเดือดร้อนให้ผู้เล่นอื่น โดนแบนถาวรทันที\n" \
       "- การทุจริตในกิจกรรมและภารกิจต่าง ๆ ถือเป็นความผิดร้ายแรง\n" \
       "- ทุกความผิดกรณีเห็นว่าหรือเข้าข่ายความผิดร้ายแรง ผู้เล่นจะถูกระบบแบนออกจากดิสคอร์ดและเซิร์ฟเวอร์ทันที\n" \
       "- ทุก 6 เดือนหากเห็นสมควรทำการไวฟ์เซิร์ฟจะแจ้งที่ห้องประกาศล่วงหน้า 1 อาทิตย์\n"


class InformationViews(discord.ui.View):
    def __init__(self, bot):
        super(InformationViews, self).__init__(timeout=None)
        self.bot = bot
        self.cooldown = commands.CooldownMapping.from_cooldown(1, int(get_cooldown_time()), commands.BucketType.member)

    @discord.ui.button(label="ข้อมูลเซิร์ฟ", style=discord.ButtonStyle.secondary, emoji="📖", custom_id='server_info')
    async def server_info(self, button, interaction: discord.Interaction):
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f'อีก {round(retry, 1)} วินาที คำสั่งถึงจะพร้อมใช้งานอีกครั้ง', ephemeral=True)
        button.disabled = False
        await interaction.response.defer(ephemeral=True, invisible=False)
        await interaction.followup.send(info.strip())

    @discord.ui.button(label="สถานะเซิร์ฟเวอร์", style=discord.ButtonStyle.secondary, emoji="📡",
                       custom_id='server_status')
    async def server_status(self, button, interaction: discord.Interaction):
        button.disabled = False
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f'อีก {round(retry, 1)} วินาที คำสั่งถึงจะพร้อมใช้งานอีกครั้ง', ephemeral=True)

        try:
            await interaction.response.defer(ephemeral=True, invisible=False)
            jsonObj = server_info()
            if jsonObj:
                pass
        except Exception as e:
            return await interaction.followup.send(e)
        else:
            result = f"```\nServer: {jsonObj['data']['attributes']['name']}" \
                     f"\n======================================" \
                     f"\nIP: {jsonObj['data']['attributes']['ip']}:{jsonObj['data']['attributes']['port']}" \
                     f"\nStatus: {jsonObj['data']['attributes']['status']}" \
                     f"\nTime in Game: {jsonObj['data']['attributes']['details']['time']}" \
                     f"\nPlayers: {jsonObj['data']['attributes']['players']}/{jsonObj['data']['attributes']['maxPlayers']}" \
                     f"\nRanking: #{jsonObj['data']['attributes']['rank']}" \
                     f"\nGame version: {jsonObj['data']['attributes']['details']['version']}\n" \
                     f"\nServer Restarts Every 6 hours" \
                     f"\nDay 3.8 hours, Night 1 hours" \
                     f"\n======================================" \
                     f"\n14Studio, Copyright © 1983 - 2023```"
            return await interaction.followup.send(result.strip())

    @discord.ui.button(label="กฎกติกา", style=discord.ButtonStyle.secondary, emoji="⚖", custom_id="server_law")
    async def server_law(self, button, interaction: discord.Interaction):
        button.disabled = False
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f'อีก {round(retry, 1)} วินาที คำสั่งถึงจะพร้อมใช้งานอีกครั้ง', ephemeral=True)

        await interaction.response.defer(ephemeral=True, invisible=False)
        await interaction.followup.send(law.strip())
