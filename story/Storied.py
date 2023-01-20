import discord

from func.config import img_

def intro_story():
    embed = discord.Embed(
        title="💀 The Walking Dead Project",
        description="โปรเจค The Walking Dead จะเป็นการนำเอาเนื้อเรื่อง" \
           "ของซีรี่ The Walking Dead มาใช้ในการกำหนดรูปแบบของเซิร์ฟ" \
           " ทั้งการปรับการตั้งค่า การกำหนดสถานการณ์และเหตุการณ์ต่าง ๆ" \
           " ดังนั้นการตั้งค่าของเซิร์ฟจะมีการปรับเปลี่ยนไปตามเนื้อหาในทุกสัปดาห์" \
           "\n\nคลิกที่ปุ่มด้านล่างเพื่ออ่าน Mini Story 👇"
    )
    embed.set_image(url=img_('reg'))
    return embed


def story_one():
    embed = discord.Embed(
        title="บทที่ 1 ช่วงเวลาที่แสนสุข",
        description="ใน 1 อาทิตย์นับตั้งแต่เริ่มเปิดให้เข้าใช้งานเซิร์ฟเวอร์ (เริ่มต้นในวันจันทร์ จนถึงวันอาทิตย์) เซิร์ฟเวอรจะเปิดโอกาสให้เตรียมตัว ทั้งเรื่องของการสร้างบ้าน (หมู่บ้าน)"
                    "เรื่องของการกักตุนเสบียงต่าง ๆ โดยเซิร์ฟเวอร์จะถูกปรับแต่งเป็น ของที่ดรอปตามพื้นที่ 10% และของที่ กดค้นหา จะอยู่ที่ 0.5% ไม่มีหุ่นยนต์ ไม่มีซอมบี้ และ outpost เปิดตามปกติ"
                    "ดังนั้นผู้เล่นที่ได้ทำการสร้างกลุ่มตามที่ระบบกำหนด และผู้เล่นที่ต้องการเล่นแบบสันโดษ ต้องพยายามกักตุนอาหารและอาวุธให้พร้อมสำหรับการเปลี่ยนแปลงในครั้งต่อไป",
        colour=discord.Colour.from_rgb(146, 43, 33)
    )
    embed.set_image(url=img_('story_one'))
    return embed