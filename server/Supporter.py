import discord

def donate():
    txt = "**📝 ช่องทางสนับสนุนเซิร์ฟเวอร์**\n" \
          "ผู้เล่นสามารถสนับสนุนค่าใช้จ่ายสำหรับ\n" \
          "- ค่าโฮสสำหรับเซิร์ฟเวอร์เกมส์\n" \
          "- ค่าโฮสสำหรับระบบบอทดิสคอร์ด\n" \
          "ผ่านทางบัญชีธนาคารกสิกรไทย เลขที่\n" \
          "` 035-8-08192-4 ` นายธีรพงษ์ บัวงาม"
    return txt.strip()

def ticket_open():
    embed = discord.Embed(
        title="✉️ Really Survival Helper System",
        description="พิมพ์หัวข้อ หรือเรื่องที่ต้องการติดต่อพร้อมรายละเอียดที่ห้องนี้\nทางทีมงานจะพยายามตอบกลับให้เร็วที่สุด"
    )
    embed.set_footer(text="ทีมงาน Really Survival")
    return embed