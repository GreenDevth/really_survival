import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup, Option


from scripts.guilds import guild_data

guild_id = guild_data()["realistic"]


def law_information():
    embed=discord.Embed(
        title="📕 กฎและข้อบังคับ",
        description="ด้วยความที่เซิร์ฟเวอร์มีรูปแบบเป็น PVE ผสามกับ Mini Story ของ ซีรี่ The Walkin Dead รูปแบบการเล่นและกฎกติกาต่าง ๆ ให้ถือความเป็น PVE เป็นส่วนใหญ่"
                    "คือการห้ามทำร้าย หรือฆ่าผู้อื่นเพื่อแย่งชิงของ รวมถึงการปล้นหรือขโมยของจากทีมหรือผู้เล่นคนอื่น ๆ และเพื่อให้รูปแบบการเล่นเพิ่มขึ้นนอกเหนือจาก PVE โดยมี The Walking Dead เป็นแนวทาง"
                    "เซิร์ฟจึงจำเป็นต้องมีกฎข้อบังคับหรือกติการ่วมกันดังนี้"
    )
    embed.add_field(name="ข้อที่ 1 ขโมย",
                    value="งัดหรือขโมยยานพาหนะสามารถทำได้ หากสิ่งของเหล่านั้นอยู่นอกบ้านหรือนอกเขตธงของผู้เล่น"
                    ,inline=False)
    embed.add_field(name="ข้อที่ 2 การปะทะและการยินยอม",
                    value="กรณีเกิดการปะทะกัน หรือปล้นเกิดขึ้น หากเป็นฝ่ายเสียเปรียบให้ทำการยินยอม หรือพูดคุยกันก่อน"
                          " หากเกิดปะทะกันให้ทำได้แค่บาดเจ็บสาหัสหรือสลบ ห้ามฆ่ากันตายทุกกรณีโดยเจตนา ห้ามดิสตัวออกหากถูกควบคุมตัวไว้ และ"
                          "ให้ส่งตัวแทนมาพูดคุยกันกรณีถูกจับเรียกค่าไถ่ เพื่อให้เกิดการต่อรองหรือ ปะทะเพื่อแย่งตัวประกัน (การตายโดยเจตนาหรือจงใจฆ่าคน มีโอกาสถูกโทษแบนได้)"
                    , inline=False)

    embed.add_field(name="ข้อที่ 3 ยานพาหนะ",
                    value="ทั้งเซิร์ฟจะมีเพียง 5 ปาร์ตี้ และ 5 ธง ยานพาหนะ 5 คัน/ลำ ต่อเมือง โดยยานพาหนะจะได้รับจากทีมงาน ประกอบด้วย"
                          "รถยนต์ 2 คัน มอร์เตอร์ไซค์ 2 คัน และ เรือ 1 ลำ (กรณียานพาหนะถูกทำลายให้ติดต่อรับภารกิจเพื่อขอรับรถคืน)"
                    , inline=False)
    embed.add_field(name="ข้อที่ 3 ทำเลในการสร้างบ้าน",
                    value="ฐานที่มั่นของผู้เล่น สามารถสร้าง ธงได้เพียง 1 ธงต่อปาร์ตี้เท่านั้น โดยกำหนดให้ผู้เล่นสร้างฐานตามทำเลที่ต้องการได้ โดยมีข้อยกเว้น ดังนี้\n"
                          "- เว้นระยห่างจากปั้ม และ outpost ในระยะ 1 กิโลเมตร\n"
                          "- ไม่สร้างกรีดขวางสะพานหรือทางเชื่อมต่าง ๆ และจุด Hight loot (ซึ่งจะเป็นจุดสำหรับทำอีเว้น โดยจะกางวงกำกับไว้)")

    embed.set_image(url="https://cdn.discordapp.com/attachments/1012319234841387109/1065840430232637450/barn.png")
    return embed



def vehicle():
    embed = discord.Embed(
        title="🚖 การครอบครองยานพาหนะ",
        description="ยานพาหนะของเซิร์ฟทั้งหมด จะมีเพียง 25 คัน/ลำ ประกอบด้วย\n"
                    "- รถยนต์ 10 คัน\n"
                    "- รถจักรยานยนต์ 10 คัน\n"
                    "- เรือยนต์ 5 ลำ\n\n"
                    "โดยจะทำการแจกจ่ายไปยังเมืองต่าง ๆในจำนวนเท่า ๆ กัน (จะทำการบันทึกหมายเลขไอดีของยานพาหนะทุกคัน/ลำ)"
    )
    embed.add_field(name="📕 ข้อตกลง",
    value=
        "- หนึ่งเมืองครอบครองรถยนต้ได้ 2 คัน มอร์เตอร์ไซค์ 2 คัน และ เรือ 1 ลำ เท่านั้น\n"
        "- กรณียานพาหนะบั๊กหรือพัง เจ้าเมืองสามารถติดต่อขอรับคืนได้ เพียงแต่ต้องมีของแลกเปลี่ยนที่สมราคา\n"
        "- กรณียานพาหนะโดนปล้นหรือขโมย เจ้าของรถต้องดำเนินแย่งคืนกลับมาเอง\n"
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/1012319234841387109/1057635787027525742/zombie_2.png")
    return embed

def player():
    embed = discord.Embed(
        title="💀 การต่อสู้แย่งชิง หรือการปล้นและการเรียกค่าไถ่",
        description="เซิร์ฟเวอร์เป็น PVE ผสาน Mini Story จากซีรี่ The Walking Dead การต่อสู้ การปล้นและการจับตัวประกันสามารถทำได้ เว้นแต่ห้ามทำอันตรายผู้เล่นคนอื่นถึงตาย"
                    "เพราะการตายของตัวละคร ผู้เล่นที่ตายต้องรอการเกิดใหม่นานถึง 1 ชั่วโมง หรืออาจจะต้องสร้างตัวละครใหม่"
                    " ดังนั้งการปะทะกันของผู้เล่นควรเกิดหลังกรณีพูดคุยกันระหว่างเจ้าเมือง และตกลงกันไม่ได้ โดยผู้เล่นต้องถือกฎข้อบังคับดังนี้"
    )
    embed.add_field(name="📕 ข้อตกลง",
    value=
        "- กรณีเกิดการดักปล้น ฝ่ายเสียเปรียบหรือมีจำนวนน้อยกว่าต้องยอมถูกจับ หรือหลบหนีให้ได้เท่านั้น\n"
        "- กรณีพลเมืองถูกจับเป็นตัวประกัน ต้องให้เจ้าเมืองทั้ง 2 ฝ่ายทำการพูดคุยต่อรอง\n"
        "- การฆ่าผู้เล่นอื่นโดยจงใจหรือเจตนา หากมีการร้องเรียนและมีหลักฐานชัดเจน ผู้กระทำความผิดจะโดนลงแบน\n"
        "- การดักปล้น การจับตัวประกัน ฝ่ายที่เป็นเชลย ห้ามดิสตัวออกจากเกมส์จนกว่าจะทำข้อตกลงระหว่างเจ้าเมืองแล้วเสร็จ"
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/1012319234841387109/1057636789487149177/peawon.png")
    return embed

def base_and_location():
    embed = discord.Embed(
        title="🏭 ตำแหน่งฐานที่มั่นหรือเมือง",
        description="ตามข้อตกลงในการสร้างปาร์ตี้ เซิร์ฟจะถูกกำหนดไว้เพียง 5 ปาร์ตี้ จำนวน 10 ต่อ 1 ปาร์ตี้ และ ปาร์ตี้ละ 1 ธงเท่านั้น"
                    "และเนื่องจาก สถานที่ ภายในแผนที่ของเกมส์ POI หรือสถานที่สำคัญต่าง ๆ จะถูกนำมาใช้เป็นสถานที่สำหรับจัดสถานการณ์"
                    "ที่จะจัดขึ้นในแต่ละบท ดังนั้น เซิร์ฟจะไม่อนุญาตให้สร้างหรือเข้ายึดครองสถานที่ต่าง ๆ ดังนี้"
    )
    embed.add_field(name="📕 ข้อตกลง",
    value=
        "- ปั้มน้ำมัน outpost ทุกที่ห้ามเข้ายึดครอง และต้องอยู่ไกลในระยะไม่ต่ำกว่า 1 กิโลเมตร\n"
        "- POI, Bunker หรือสถานที่สำคัญใหญ่ ๆ ห้ามเข้ายึดครองหรือสร้างบ้านในระยะ 500 เมตร\n"
        "- สนามบิน B1 ค่ายทหาร B3 โรงเรือนและท่าเรือ A4 สุสานเศษเหล็ก B0 โรงเรือน D0 สานามบิน D4 สถานีรถไฟและโรงผลิตหุ่นยนต์ Z0 (ห้ามเข้ายึดครองหรือสร้างเมืองบริเวณดังกล่าว)\n"
        "- สะพานข้ามเมืองข้ามแม่น้ำต่าง ๆ ห้ามสร้างสิ่งกรีดขวางต้องปล่อยให้การสัญจรผ่านไปมาได้\n"
        "- สะพานทางเชื่อมระหว่าง โซน Z ห้ามยึดครองหรือสร้างเมืองกรีดขวางเพราะ จะใช้เป็นจุดในการสร้างสถานการณ์หรืออีเว้นต่าง ๆของโปรเจค\n"
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/1012319234841387109/1066372350213369967/bran_reg.png")
    return embed


class MainLawCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    law = SlashCommandGroup(guild_ids=[guild_id], name="law", description="คำสั่งจัดการแสดงเนื้อหาเกี่ยวกับ กฎและกติกา")

    @law.command(name="กฎกติกาหลัก", description="คำสั่งแสดง กฎและ กติกาหลักของเซิร์ฟ")
    async def main_law(self, ctx:discord.Interaction, command:Option(str, "เลือกคำสั่งที่ต้องการ", choices=["show"])):
        guild = ctx.guild

        await ctx.response.defer(ephemeral=True, invisible=False)
        msg = await ctx.followup.send("⏳ รอสักครู่ระบบกำลังประมวลผลการทำงาน")

        ch_name="📕-กฎและข้อบังคับ"

        if command == "show":
            try:
                channel = discord.utils.get(guild.channels, name=ch_name)
                if channel:
                    await channel.purge()
                    await channel.send(embed=base_and_location())
                    await channel.send(embed=player())
                    await channel.send(embed=vehicle())
                else:
                    channel = await guild.create_text_channel(name=ch_name)
                    await channel.set_permissions(guild.default_role, view_channel=True, send_messages=False)
                    await channel.send(embed=base_and_location())
                    await channel.send(embed=player())
                    await channel.send(embed=vehicle())

            except Exception as e:
                return await msg.edit(content=e)
            else:
                return await msg.edit(content=f"สร้างห้อง {channel.mention} สำเร็จ")



