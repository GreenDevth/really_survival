import discord

from db.users import Users
from func.config import img_, current_time


def server_info():
    txt = "**📖 Really Survival - SCUM Community Server**\n" \
          "- ที่ตั้งเซิร์ฟ สิงคโปร์ ไอพี : ` 1.1.1.1:0000 ` 30 + 3 Slot\n" \
          "- เรทดรอปปรับเปลี่ยนไปตามเนื้อเรื่องที่ได้กำหนดไว้ใน mini story\n" \
          "- ปาร์ตี้สูงสุด 8 คน ต่อ 1 ธง (จำกัด 4 ทีม) ครอบครองยานพาหนะ 2 คัน\n" \
          "- ยานพาหนะจะทำลายตัวเองหากไม่มีการใช้งานใน 7 วัน\n" \
          "- กางวงสำหรับอีเว้น และวงตามจุดฟาร์มใหญ่ ๆ ดาเมจตามเหตุการณ์ของอีเว้น\n" \
          "- outpost ปรับแต่งตามความเหมาะสมของอีเว้นที่สร้างขึ้นภายในเซิร์ฟ\n" \
          "- ดาเมจซอมบี้ปรับตามเหตุการณ์ ไม่มีหุ่นยนตร์ และ ไม่มีโดรนเงิน\n" \
          "- จำนวนซอมบี้ จะเพิ่มลดตามอีเว้นที่สร้างขึ้นภายในเซิร์ฟ\n" \
          "- ไม่มีแผนที่ กิจกรรมและภารกิจรออัพเดทในอนาคต" \
          ""
    return txt.strip()
def reg_info():
    txt ="Realistic Survival เซิร์ฟเวอร์ที่ผู้เล่นต้องได้รับการ Verify Whitelist จากแอดมินเสียก่อน" \
         " จึงจะสามารถเข้าใช้งานเซิร์ฟเวอร์ได้ รูปแบบเซิร์ฟเป็น PVE และ Mini Story อ้างอิงเนื้อหาของซีรี่ The Walking Dead\n" \
         "**จำนวนสิทธิ์คงเหลือ**\n" \
         f"{int(30) - Users().user_count()} สิทธิ์"
    embed=discord.Embed(
        title="📖 คำแนะนำ",
        description=txt,
    )
    embed.set_image(url=img_('reg'))
    return embed

def steam_reg():
    txt = "Realistic Survival เป็นเซิร์ฟเวอร์แบบ Private Server" \
          " โปรดรอข้อความยืนยันสิทธิ์การเข้าใช้งานจากระบบอีกครั้ง"
    return txt.strip()

def reg_success(member, steam_id):
    embed = discord.Embed(
        title="💾 บันทึกข้อมูลสำหรับเร็จ 🟢",
        description=steam_reg(),
        colour=discord.Colour.from_rgb(46, 197, 19)
    )
    # embed.add_field(name="ผู้ลงทะเบียน", value=member.display_name)
    embed.add_field(name="หมายเลขสตรีม", value=steam_id)
    embed.add_field(name="วันที่ลงทะเบียน", value=current_time("%m-%d-%Y, %H:%M:%S"))
    embed.add_field(name="สิทธิ์การใช้งาน", value="🟠 รอการอนุมัติ")
    embed.set_thumbnail(url=member.display_avatar)
    # embed.set_image(url=img_('reg_success'))
    return embed

def success_register(member, steam_id):
    embed = discord.Embed(
        title="💾 ลงทะเบียนสำหรับเร็จ 🟢",
        colour=discord.Colour.from_rgb(46, 197, 19)
    )
    embed.add_field(name="ผู้ลงทะเบียน", value=member.display_name)
    embed.add_field(name="หมายเลขสตรีม", value=steam_id)
    embed.add_field(name="วันที่ลงทะเบียน", value=current_time("%m-%d-%Y, %H:%M:%S"))
    embed.set_thumbnail(url=member.display_avatar)
    return embed