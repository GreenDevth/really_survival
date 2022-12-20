import discord

from func.config import img_, current_time


def server_info():
    txt = "**📖 Really Survival - SCUM Community Server**\n" \
          "- ที่ตั้งเซิร์ฟ สิงคโปร์ ไอพี : ` 1.1.1.1:0000 ` 30 + 3 Slot\n" \
          "- เรทดรอปเท่ากับ 1% รีเซ็ตทุก 1 ชั่วโมง ดรอปยานพาหนะตามค่าเริ่มต้น (รถทุกคันจะมีเครื่องยนต์)\n" \
          "- ปาร์ตี้สูงสุด 10 คน ต่อ 1 ธง (300 element per flag) ครอบครองยานพาหนะ 3 คัน\n" \
          "- ยานพาหนะจะทำลายตัวเองหากไม่มีการใช้งานใน 7 วัน\n" \
          "- กางวงทั่วแผนที่ป้องกันการขโมยและอันตรายจากผู้เล่น ไม่มีดาเมจบ้าน ไม่มีดาเมจระเบิด\n" \
          "- กางวงสำหรับอีเว้น และวงตามจุดฟาร์มใหญ่ ๆ ดาเมจตามค่าเริ่มต้นทุกประการ\n" \
          "- outpost ปรับแต่งตามความเหมาะสมของอีเว้นที่สร้างขึ้นภายในเซิร์ฟ\n" \
          "- ดาเมจซอมบี้เท่ากับค่าเริ่มต้น ไม่มีหุ่นยนตร์ และ ไม่มีโดรนเงิน\n" \
          "- จำนวนซอมบี้ จะเพิ่มลดตามอีเว้นที่สร้างขึ้นภายในเซิร์ฟ\n" \
          "- ไม่มีแผนที่ กิจกรรมและภารกิจรออัพเดทในอนาคต" \
          ""
    return txt.strip()
def reg_info():
    txt ="ผู้เล่นทุกคนต้องได้รับการ Verify จึงจะเข้าใช้งานเซิร์ฟเวอร์ได้\n" \
          "รูปแบบของเซิร์ฟเวอร์เป็น PVE ผนวกกับ Mini Story \n" \
          "อิงตามเนื้อเรื่องของซีรี่ The Walking Dead \n" \
          "กดปุ่ม Accept เพื่อลงทะเบียน หากต้องการเป็นส่วนหนึ่งกับเรา"
    embed=discord.Embed(
        title="📖 Register Information",
        description=txt,
    )
    embed.set_image(url=img_('reg'))
    return embed

def steam_reg():
    txt = "Really Survival เป็นเซิร์ฟเวอร์แบบ Private Server" \
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