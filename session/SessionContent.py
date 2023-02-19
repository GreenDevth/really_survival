import discord

from func.config import img_


def police_event():
    embed=discord.Embed(
        title="🚧 ด่าน",
        description="สำนักข่าวกรองของ TEC 1 Coperation ได้รับแจ้งจากโดรนตรวจการ เหตุพบเห็นกลุ่มคนต้องสงสัยกำลังทำการขนย้ายอุปกรณ์บางอย่างขึ้นรถยนต์จำนวน 2 คัน และขับรถ"
                    "มุ่งหน้าไปยัง KRK BRIDGE 1 คัน DR.TUDMAN BRIDGE อีก 1 คัน \n\nและล่าสุดสำนักข่าว TOP TEC1 NEWS ได้รายงานสถานการณ์การปะทะกันของเจ้าหน้าที่ตำตรวจและผู้ต้องสงสัยในบริการดังกล่าว",
        color=discord.Colour.from_rgb(243, 67, 6)
    )
    embed.set_image(url=img_("event_frist"))
    embed.add_field(name="คำแนะนำ",
                    value="ให้ตัวแทนของเมืองแต่ละเมืองส่งตัวแทนหรือหัวหน้าเมืองเข้ารับการจับฉลากสุ่มบทบาทกลุ่มของตัวละคร ซึ่งจะประกอบด้วย\n"
                          "\n 1. กลุ่มของผู้ต้องสงสัย จำนวน 2 ทีม"
                          "\n 2. กลุ่มของเจ้าหน้าที่ตำรวจประจำด่าน จำนวน 2 ทีม"
                          "\n 3. เจ้าหน้าที่ตำรวจทีมสนับสนุน จำนวน 1 ทีม")
    return embed

def lose_weapon():
    embed = discord.Embed(
        title="⚔ อาวุธปืนที่หายไป",
        description="เรื่องราวขณะที่ริกส์กำลังออกตามหาภรรยาและลูกชายของตน ซึ่งในเหตุการณ์นี้ริกส์ได้ทำกระเป๋าซึ่งเต็มไปด้วยอาวุธสำคัญ"
                    "หล่นหายขณะที่หนีออกจากฝูงซอมบี้ เซิร์ฟจะจำลองเหตุการณ์ที่กลุ่มของริกส์ออกตามหาอาวุที่หล่นหายและได้เข้าปะทะกับ"
                    "กลุ่มคนอีกกลุ่นที่เป็นคนในพื้นที่ ซึ่งกำลังตามหากระเป๋าใบนั้นเช่นกัน"
    )
    embed.set_image(url=img_("weapon_lose"))
    return embed

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