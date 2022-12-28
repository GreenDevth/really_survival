import discord
from discord.ext import commands, pages

from func.config import get_cooldown_time, img_


class StoryView(discord.ui.View):
    def __init__(self, bot):
        super(StoryView, self).__init__(timeout=None)
        self.bot = bot
        self.cooldown = commands.CooldownMapping.from_cooldown(1, int(get_cooldown_time()), commands.BucketType.member)
        self.story = [
            discord.Embed(
                title="📖 บทที่ 1 ช่วงเวลาที่แสนสุข",
                description="1 อาทิตย์ ก่อนโรคระบาดกระจาย ผู้คนบนเกาะยังดำเนินชีวิตไปอย่างปกติ ทุกคนต่างก็เป็นมิตรและพึ่งพาอาศัยซึ่งกันและกัน ทรัยากรต่าง ๆ"
                            "มีมากมาย อารยธรรมของมนุษยชาติยังคงดำเนินไปตามปกติที่ควรจะเป็น แต่ทว่าความสงบสุขเหล่านั้นกำลังจะถูกทำลายในไม่ช้า",
                colour=discord.Colour.from_rgb(85, 226, 32)
            ),
            discord.Embed(
                title="📖 บทที่ 2 โรคระบาดครั้งใหญ่",
                description="2 อาทิตย์ให้หลัง โรคระบาดเริ่มกระจายไปทั่วทั้งเกาะ ผู้คนเริ่มแตกตื่นหนีตายออกนอกเมือง"
                            "จากฝูงซอมบี้และตามหาสถานที่ปลอดภัยสำหรับตน ในขณะเดียวกันก็มีกลุ่มคนบางกลุ่มที่กำลังรวบรวมผู้คนเพื่อผลประโยชน์อะไรบางอย่าง",
                colour=discord.Colour.from_rgb(85, 226, 32)
            ),
            discord.Embed(
                title="📖 บทที่ 3 คน",
                description="อาทิตย์ที่ 3 หลังจากโรคระบาดได้กระจายไปทั่วทั้งเกาะ อาหารและที่อยู่อาศัยเริ่มเป็นสิ่งที่จำเป็นต่อการดำรงชีวิตอย่างมาก"
                            " ผู้ค้นเริ่มแย่งชิงเสบียงของกันและกัน เกิดการปะทะปล้นฆ่าแย่งชิงอาวุธแย่งชิงพื้นที่เพื่อหวังที่จะได้ครอบครองไว้เพียงผู้เดียว",
                colour=discord.Colour.from_rgb(85, 226, 32)
            ),
            discord.Embed(
                title="📖 บทที่ 4 อาหาร",
                description="ผ่านไป 4 อาทิตย์หลังจากโรคระบาดได้คร่าชีวิตผู้คนไปเป็นจำนวนมาก และในขณะเดียวกันจำนวนซอมบี้ก็ได้เพิ่มขึ้นเรื่อยๆ การจะเข้าเมืองเพื่อไปหาเสบียง"
                            "จึงเป็นไปได้ค่อนข้างยากรำบาก ทั้งเรื่องอาวุธที่มีอยู่น้อย และยานพาหนะที่ค่อย ๆ พังรวมทั้งน้ำมันก็เป็นสิ่งที่เร่ิมหาได้ยากขึ้น",
                colour=discord.Colour.from_rgb(85, 226, 32)
            ),
            discord.Embed(
                title="📖 บทที่ 5 อาวุธ",
                description="เข้าอาทิตย์ที่ 5 ผู้คนเริ่มปรับตัวกับการเปลี่ยนแปลงที่เกิดขึ้น และได้รวมกลุ่มกันเป็นเมือง เป็นหมู่บ้าน"
                            " และอยู่อาศัยกันอยากมีความสุข แต่ทว่ามีกลุ่มคนบางกลุ่มที่กำลังทำการเคลื่อนไหววางแผนอะไรบางอย่าง",
                colour=discord.Colour.from_rgb(85, 226, 32)
            )
        ]
        self.story[0].set_image(url=img_('story_intro'))
        self.story[0].add_field(name="การตั้งค่าเซิร์ฟ",
                                value="- ปิดหุ่นยนต์ ปิดซอมบี้ระเบิด เปิดใช้งานแผนที่"
                                      "\n- ปิดการสร้างปาร์ตี้ ปิดการสร้างบ้าน เพื่อรองรับอีเว้น"
                                      "\n- เรทดรอปตามพื้น 10% และกดค้นหา 0.5%"
                                      "\n- ดรอปยานพาหนะปกติจำนวน 30 คัน"
                                      "\n- มีดาเมจเฉพาะจุดฟาร์มหลัก ๆ จำนวนซอมบี้ประปราย"
                                      "\n- outpost ซื้อขายได้ตลอด ราคาตามค่าเริ่มต้น\n",
                                )
        self.story[0].add_field(name="คำแนะนำ",
                                value="วันแรกของการรันเซิร์ฟเวอร์ไปจนครบ 1 อาทิตย์"
                                      " ผู้เล่นต้องตามหากลุ่มคนของตนเพื่อรอสร้างปาร์ตี้ และก่อตั้งหมู่บ้าน พยายาม"
                                      "ระดมสรรพกำลังเพื่อจัดเตรียมและกักตุนอาหาร อาวุธและยานพาหนะต่าง ๆ"
                                      "การปะทะกันของผู้เล่นเป็นไปตามปกติ (ดาเมจจะเบากว่าปกติ เพื่อให้เกิดการต่อรอง)"
                                ,inline=False)
        self.story[1].set_image(url=img_('story_frist'))
        self.story[1].add_field(name="การตั้งค่าเซิร์ฟ",
                                value="- ปิดหุ่นยนต์ ปิดซอมบี้ระเบิด ปิดใช้งานแผนที่ ปิดการสร้างบ้าน\n"
                                      "- เปิดให้สร้างปาร์ตี้ (รองรับสูงสุดที่ 10 คน)\n"
                                      "- เรทดรอปตามพื้นปรับลดลงเหลือ 5% กดค้นหาเหลือ 0.25%\n"
                                      "- outpost ปิดการใช้งาน unlimited\n"
                                      "- เพิ่มจำนวนซอมบี้ตามเมือง (ไม่เยอะมากแต่เร่งการเกิดใหม่ให้เร็วขึ้น)\n"
                                      "- ซอมบี้ตามป่าจะน้อยหรือไม่เกิน 3 ตัว ซอมบี้ในบังเกอร์ ไม่เยอะมาก\n"
                                      "- เปิดดาเมจเพื่อสร้างโอกาสปะทะกันของกลุ่มคน (ดาเมจปกติ)"
                                )
        self.story[1].add_field(name="คำแนะนำ",
                                value="เข้าอาทิตย์ที่ 2 ช่วงเวลาแห่งการเอาชีวิตรอด โดยจะมี Event และภารกิจ ให้ผู้เล่นได้เข้าร่วมเพื่อเดินเนื้อเรื่อง"
                                      "จะเกิดการ ปะทะกันของกลุ่มคน มีภารกิจตามหาคนหรือกลุ่มคน มีภารกิจตามหาอาวุธที่ตกหล่นระหว่างหนีเอาชีวิตรอด"
                                      "จากฝูงซอมบี้ ภารกิจออกหาเสบียง และภารกิจช่วยเหลือ โดยทุกภารกิจและอีเว้น ผู้ชนะหรือผู้คนพบหรือทำภารกิจสำเร็จ"
                                      "จะได้รับ อาหารและอาวุธเพียงจำนวนหนึ่งเท่านั้น"
                                , inline=False)
        self.story[2].set_image(url=img_("prisons"))
        self.story[2].add_field(name="การตั้งค่าเซิร์ฟ",
                                value="- ปิดหุ่น ปิดซอมบี้ระเบิด ปิดใช้งานแผนที่ ปิดการสร้างบ้าน\n"
                                      "- เรดดรอปตามพื้น 5% กดค้นหา 0.25% outpost สินค้าเริ่มหมด\n"
                                      "- ซอมบี้เริ่มเยอะขึ้น ดาเมจปกติ (เร่งเวลาในการเกิดใหม่เร็วขึ้น)\n"
                                      "- ซอมบี้ตามป่าเพิ่มขึ้น เป็นไม่ต่ำกว่า 10 ตัว (ดาเมจปกติ)\n"
                                      "- ซอมบี้ตามบ้านและบังเกอร์ (เร่งเวลาในการเกิดใหม่เร็วขึ้น)\n"
                                )
        self.story[2].add_field(name="คำแนะนำ",
                                value="อาทิตย์ที่ 3 หลังจากโรคระบาด ผู้คนเริ่มเกาะกลุ่มกัน และระดมสรรพกำลังกันสำรวจและเสาะหาเสบียงกัน"
                                      "ตามเมืองและหมู่บ้านต่าง ๆ จนกระทั่งเกิดการปะทะกันของกลุ่มคนหลายกลุ่มหลายสถานที่ เซิร์ฟจะเปิดอีเว้นการ"
                                      "ปะทะกันของกลุ่มต่าง ๆ เพื่อแย่งชิงอาหารและอาวุธในจุดเมืองสำคัญ ๆ (ไม่มีการแจกอาวุธให้หาอาวุธกันมาเอง)"
                                      "ผู้ที่ชนะหรือกลุ่มที่ชนะจะได้รับอาหารและอาวุธจำนวนหนึ่ง", inline=False
                                ),
        self.story[3].set_image(url=img_("farm"))
        self.story[3].add_field(name="การตั้งค่าเซิร์ฟ",
                                value="- เปิดฟังก์ชั่นการสร้างบ้าน\n"
                                      "- จำนวนซอมบี้ตามป่า มากกว่าปกติ (ดาเมจมากกว่าปกติ)\n"
                                      "- จำนวนซอมบี้ตามหมู่บ้านและบังเกอร์ เพิ่มขึ้น\n"
                                      "- เรทดรอปตามพื้น 5% กดค้นหา 0.5% รีดรอปทุก 30 นาที"
                                )
        self.story[3].add_field(name="คำแนะนำ",
                                value="อาทิตย์ที่ 4 ของการระบาดครั้งใหญ่ ผู้คนเริ่มสำรวจและรวมตัวกันก่อตั้งหมู่บ้าน เริ่มมีการทำการเกษตร เริ่มมีการแลกเปลี่ยนสินค้า"
                                      "ระหว่างเมือง หรือหมู่บ้าน แต่ทว่า การส่งสินค้าเพื่อทำการแลกเปลี่ยนของระหว่างเมืองนั้น เต็มไปด้วยอันตรายและความยากรำบาก"
                                , inline=False)


    def get_story(self):
        return self.story

    @discord.ui.button(label="มินิสตอรี่ (The Walking Dead - Mini Story)", style=discord.ButtonStyle.secondary, emoji="📖", custom_id="read_story")
    async def read_story(self, button, interaction: discord.Interaction):
        button.disabled = False
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f'อีก {round(retry, int(get_cooldown_time()))} วินาที คำสั่งถึงจะพร้อมใช้งานอีกครั้ง', ephemeral=True)

        await interaction.response.defer(ephemeral=True, invisible=False)

        try:
            pagelist = [
                pages.PaginatorButton(
                    "first", label="หน้าแรก", style=discord.ButtonStyle.secondary
                ),
                pages.PaginatorButton("prev", label="ก่อนหน้า", style=discord.ButtonStyle.secondary),
                pages.PaginatorButton(
                    "page_indicator", style=discord.ButtonStyle.gray, disabled=True
                ),
                pages.PaginatorButton("next", label="ถัดไป", style=discord.ButtonStyle.secondary),
                pages.PaginatorButton("last", label="หน้าสุดท้าย", style=discord.ButtonStyle.secondary),
            ]
            paginator = pages.Paginator(
                pages=self.get_story(),
                show_disabled=True,
                show_indicator=True,
                use_default_buttons=False,
                custom_buttons=pagelist,
                loop_pages=False,
            )
            await paginator.respond(interaction, ephemeral=True)
        except Exception as e:
            return await interaction.followup.send(e)
