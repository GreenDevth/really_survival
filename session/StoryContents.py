import discord

from func.config import img_


def story_001():
    embed = discord.Embed(
        title="📖 บทที่ 1 ช่วงเวลาที่สงบสุข (ความสามัคคี)",
        description="1 อาทิตย์ ก่อนโรคระบาดกระจาย สถานการณ์ต่าง ๆบนเกาะยังดำเนินไปอย่างปกติ ขณะเดียวกันข่าวการขุดพบของใช้ที่ถูกซ่อนไว้ได้แพร่กระจายไปทั่วทั้งเกาะ"
                    "ทำให้ผู้คนบนเกาะต่างออกเดินทางตามหา เพื่อหวังจะได้พบหลุมซึ่งฝังไว้ซึ่งสมบัติอันล้ำค่ำ แต่ทว่าคำใบ้เดียวที่มีเป็นแค่เพียงแผนที่ซึ่งระบุตำแหน่งที่ไม่แน่นอน",
        color=discord.Colour.from_rgb(14, 156, 29)
    )
    embed.set_image(url=img_("startpack_box"))

    embed.add_field(name="การตั้งค่าเซิร์ฟ",
                    value="- ปิดแผนที่ ปิดปาร์ตี้ ปิดการสร้างบ้าน\n"
                          "- ไม่ดรอปไอเท็มใด ๆ ทั้งสิ้น\n"
                          "- ไม่มีซอมบี้ ไม่มีหุ่นยนต์ เพิ่มจำนวนสัตว์\n"
                          "- ไม่มีดาเมจผู้คน อาหารและน้ำลดไวกว่าปกติ\n"
                          "- หากตายต้องสร้างตัวละครใหม่เท่านั้น\n", inline=False
                    )

    embed.add_field(name="คำแนะนำ",
                    value="อาทิตย์แรกของการรันโปรเจค "
                          "ผู้เล่นจะได้รับภารกิจตามหากล่องที่ถูกฝังไว้ตามจุดต่าง ๆ (กดรับคำใบ้ที่ปุ่มกระดานภารกิจ) "
                          "โดยภายในกล่องจะมีของใช้ อาหารและบางกล่องจะมีอาวุธ และรหัสลับ (ไอดีของกล่อง)", inline=False
                    )

    embed.add_field(name="คำสั่งภารกิจ",
                    value="หลังจากผู้เล่นได้เก็บของจากกล่องที่ค้นพบ และจดเอารหัสไอดีของกล่องไว้เรียบร้อยแล้ว ให้ผู้เล่นมุ่งหน้ามายังเมื่องท่า"
                          " (จะประกาศตำแหน่งเมืองเมื่อผู้เล่น ทุกคน ลงถึงพื้นเรียบร้อยแล้ว) ที่เมืองท่า จะใช้เป็นที่ กักตุนเสบียงหรืออาหารและอาศัยชั่วคราว โดยจะมีอปุกรณ์สำหรับสร้างของเตรียมไว้ให้เป็นบางส่วน  "
                          "และเมื่อผู้เล่นทุกคนทำการปลดล๊อครหัสลับเรียบร้อย เซิร์ฟเวอร์จะทำการคืนค่าตามการตั้งค่าใน บทที่ 1 ของ mini story และจะเริ่มใช้งานได้หลังจากการรีเซิร์ฟในครั้งถัดไป", inline=False
                    )


    embed.add_field(name="คำอธิบายของ รหัสลับ",
                    value="- รหัสลับจะเป็นรหัสไอดีของกล่องที่ถูกฝังไว้\n"
                          "- รหัสลับจะใช้สำหรับการปลดล๊อคการตั้งค่าเซิร์ฟเมื่อรีเซิร์ฟครั้งถัดไป\n"
                          "- รหัสลับจะเป็นตัวปลดล๊อคค่าประสบการณ์ให้กับผู้เล่น\n", inline=False
                    )
    return embed