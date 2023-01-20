import discord

from func.config import img_


def event_001():
    embed = discord.Embed(
        title="🚔 ล่ากลุ่มโจร",
        description="1 สัปดาห์ต่อจากนี้ผู้เล่นทุกคนจะยังไม่ได้รับอนุญาตในการสร้างปาร์ตี้และสร้างบ้าน ผู้เล่นต้องรวมกลุ่มของตนและร่วมกันกักตุนทรัพยากรต่าง ๆ"
                    " สำหรับเตรียมเข้าสู่เนื้อเรื่องหลัก โดยภายในสัปดาห์นี้จะมี Event เล็ก ๆ เข้าเนื้อเรื่องใน The walking dead ซีซั่นที่ 1 ซึ่งจะเป็นการปะทะของตำรวจและกลุ่มโจร โดย Event จะจัดขึ้นบริเวณสะพาน"
                    "ระหว่าง Z0 ไปยัง A0 โดยจะแบ่งกลุ่มออกเป็น ทีม ตำรวจไล่ล่า 1 ทีม กลุ่มโจร และ ทีมตำรวจที่ตั้งด่านสกัดรถของกลุ่มโจร"
    )
    embed.set_image(url=img_("event_frist"))
    return embed

def event_002():
    embed = discord.Embed(
        title="⚔ อาวุธปืนที่หายไป",
        description="ในสัปดาห์ที่ 2 กำหนดให้ผู้เล่นส่งตัวแทนเพื่อเข้าร่วมเข้าเนื้อเรื่องใน The walking dead ในเหตุการณ์ ริกส์ทำกระเป๋าอาวุธหล่นไว้"
                    "โดยกำหนดพื้นที่จัดกิจกรรม เป็น เมือง D3 และพื้นที่เหล่านั้นจะเต็มไปด้วย ซอมบี้ อีเว้นนี้จะให้ผู้เล่นแบ่งเป็น 2 ทีม ต่อการดำเนินอีเว้น โดยประกอบด้วยทีมเจ้าของพื้นที่"
                    "และทีมของริกส์"
    )
    embed.set_image(url=img_("weapon_lose"))
    return embed

def event_003():
    embed = discord.Embed(
        title="🩸 สาหัส",
        description="สัปดาห์ที่ 3 กำหนดให้ผู้เล่นเข้าเนื้อเรื่องใน The walking dead ในเหตุการณ์ คาร์ลโดนยิง โดยกำหนดให้ 1 ในผู้เล่นในทีม ได้รับบาดแผลสาหัสต้องได้รับการรักษา"
                    "ภายในระยะเวลาที่กำหนด ซึ่งผู้เล่นในทีมต้องนำผู้เล่นที่ได้รับบาดเจ็บ เข้ารับรักษาตัวในตำแหน่งที่กำหนดไว้ โดยจะให้ผู้เล่นในทีมอีก 1 คนประจำตำแหน่งเพื่อรอรักษาผู้เล่นของตนให้ทัน"
    )
    embed.set_image(url=img_("carl_shoot"))
    return embed

def event_004():
    embed = discord.Embed(
        title="🏠 โรงนา",
        description="กำหนดเหตุการณ์ของกลุ่ม ริกส์และพวกในเหตุการณ์ กำจัดฝูงซอมบี้ในโรงนา และร่วมกับเหตุการณ์ที่มหาฝูงซอมบี้เข้าบุกบ้านจนทำให้กลุ่มของริกส์แตกกระจายการไปอีกครั้ง"
                    "โดย"
    )
    embed.set_image(url=img_("barn"))
    return embed