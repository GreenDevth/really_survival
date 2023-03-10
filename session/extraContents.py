import discord
from func.config import img_


def extra_000():
    embed = discord.Embed(
        title="📦 เสบียง และการรวมกลุ่ม",
        description="กำหนดให้ผู้เล่นทุกคน ต้องตามหากล่องเสบียงที่ถูกฝังทิ้งไว้ โดยกลุ่มคนกลุ่มหนึ่ง จงขุดมันขึ้นมาและนำเอา ID ของกล่องมาปลดล๊อค รับค่าประสบการณ์จากระบบ"
                    " โดยภายในกล่องจะมีอาหาร ยา และอุปกรณ์ยังชีพเบื้องต้น และ 5 ในกล่องทั้งหมดจะมีกุญแจของเมืองใส่ไว้ข้างในด้วย"
    )
    embed.set_image(url=img_("startpack_box"))
    embed.add_field(name="คำสั่งเพิ่มเติม",
                    value="จงนำกุญแจที่ได้รับมายังเมือง ท่า (สร้างขึ้นเพื่อใช้เป็นสถานที่จัดอีเว้น) และนำรถไปรับผู้เล่นคนอื่นกลับมายังเมืองท่า ให้ครบทุกคน เพื่อเตรียมเข้าสู่สถานการณ์ต่อไป")
    return embed

def lose_weapon():
    embed = discord.Embed(
        title="⚔ อาวุธปืน",
        description="ริกส์และกลุ่มของเกรนได้ย้อนกลับไปยังตำแหน่งที่คาดว่าริกส์ได้ทำกระเป๋าที่ใส่อาวุธปืนหล่นไว้ พวกเขาต้องพยายามไปอย่างเงียบ ๆ "
                    "เพื่อไม่ให้ฝูงซอมบี้แตกตื่น ในขณะเดียวกันก็มีอีกหลายกลุ่มก็กำลังจะไปยังตำแหน่งกระเป๋าใส่ปืนของริกส์เช่นเดียวกัน"
    )
    embed.set_image(url=img_("weapon_lose"))
    embed.add_field(name="คำแนะนำ",
                    value="```hello\n"
                          "+ อีเว้นต่อเนื่องเมื่อช่วยเหลือตัวแทนผู้เล่นของทีมสำเร็จ\n"
                          "+ จะมีกล่องไม้อยู่ใกล้ๆ ให้นำไอดีมาปลดล๊อคตำแหน่งอาวุธ\n"
                          "+ ทั้ง 4 ทีมต้องต่อสู้แย่งชิงกระเป๋ากันให้ได้ภายใน 1 ชั่วโมง\n"
                          "+ ทีมที่ได้กระเป๋าอาวุธต้องรวมกันที่ Vato Area (ประกาศวันจัด)\n"
                          "+ ทีมที่เหลือจะต้องสกัดกั้นและแย่งชิงมาให้ได้\n"
                          "+ ภารกิจจะสิ้นสุดเมื่อแอดมินจุดพลุส่งสัญญาณ\n"
                          "\n```"
                    ,inline=False)
    return embed

def extra_001():
    embed = discord.Embed(
        title="💊 ยา",
        description="กำหนดให้ส่งตัวแทนผู้เล่นของกลุ่มจำนวน 2 คน เข้าร่วมในสถานการณ์ โดยเซิร์ฟจะจำลองเหตุการณ์ใน The Walking Dead SS2 โดยกำหนดให้ผู้เล่น"
                    "ตามหาอุปกรณ์เพื่อใช้รักษาเพื่อนร่วมทีมที่ได้รับบาดเจ็บ โดยจะจำลองสถานการณ์ขึ้นในตำแหน่งของโรงพยาบาล และเพิ่มเรื่องของการแย่งชิงเข้ามา"
                    "โดยแต่ละทีมจะต้องแย่งชิงอุปกรณ์ทางการแพทย์กลับไปช่วยเพื่อนในทีม"
    )
    embed.set_image(url=img_("medicine"))
    return embed

