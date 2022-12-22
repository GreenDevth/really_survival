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
                description="2 อาทิตย์ให้หลัง โรคระบาดเริ่มกระจายไปทั่วทั้งเกาะ ผู้คนเริ่มแตกตื่นหนีตายออกจากเมือง"
                            " ผู้คนต่างทยอยออกตามหาสถานที่ที่คิดว่าปลอดภัยสำหรับตน แต่ก็มีกลุ่มคนบางกลุ่มที่กำลังรวบรวมผู้คนเพื่ออะไรบางอย่าง"
                            "\n\nเซิร์ฟจะปรับการตั้งค่าเป็นดังนี้\n"
                            "- เพิ่มจำนวนซอมบี้ในจุดฟาร์มสูงสุด\n"
                            "- ลดอัตราการดรอปพื้น เหลือ 5% ส่วนจากการค้นหายังคงเท่าเดิม\n"
                            "- ปรับสถานีน้ำมันให้น้ำมันเหลือน้อยลง\n"
                            "- ปรับเพิ่มจำนวนรถแบบไม่มีเครื่อง\n",
                colour=discord.Colour.from_rgb(85, 226, 32)
            ),
            discord.Embed(
                title="📖 บทที่ 3 ",
                description="อาทิตย์ที่ 3 หลังจากได้เตรียมตัว พร้อมรับการเปลี่ยนแปลงครั้งใหญ่ของเซิร์ฟ "
                            "เช่นการสร้างหมู่บ้าน สร้างที่พักพิงสำหรับผู้เล่นโซโล่ การกักตุนอาหาร และอาวุธพร้อมเรียบร้อย"
                            "\n\nเซิร์ฟจะปรับการตั้งค่าเป็นดังนี้\n"
                            "- เพิ่มจำนวนซอมบี้ในจุดฟาร์มสูงสุด\n"
                            "- ลดอัตราการดรอปพื้น เหลือ 5% ส่วนจากการค้นหายังคงเท่าเดิม\n"
                            "- ปรับสถานีน้ำมันให้น้ำมันเหลือน้อยลง\n"
                            "- ปรับเพิ่มจำนวนรถแบบไม่มีเครื่อง\n",
                colour=discord.Colour.from_rgb(85, 226, 32)
            ),
            discord.Embed(
                title="นักผจญภัย - ADVENTURER",
                description="นักผจญภัย เป็นอาชีพอิสระไม่มีการผูกมัดหรือสิทธิ์พิเศษใด สามารถซื้อขายของได้ตามปกติทั่วไป และอาจจะได้รับภารกิจพิเศษเช่นการสำรวจพื้นที่ต่าง ๆ และยังจะเป็นหนึ่งในอาชีพที่คอยบุกเบิกเสาะแสวงหาพื้นที่สำหรับอยู่อาศัยของพลเมือง",
                colour=discord.Colour.from_rgb(85, 226, 32)
            ),
        ]
        self.story[0].set_image(url=img_('story_intro'))
        self.story[0].add_field(name="การตั้งค่าเซิร์ฟ",
                                value="- ปิดหุ่นยนต์ และซอมบี้ระเบิด เปิดใช้งานแผนที่"
                                      "\n- ปรับปาร์ตี้สูงสุด 10 คน เพื่อรองรับอีเว้น"
                                      "\n- เรทดรอปตามพื้น 10% และกดค้นหา 0.5%"
                                      "\n- ดรอปยานพาหนะปกติจำนวน 30 คัน"
                                      "\n- มีดาเมจเฉพาะจุดฟาร์มหลัก ๆ และซอมบี้ประปราย"
                                      "\n- outpost ซื้อขายได้ตลอด ราคาตามค่าเริ่มต้น\n",
                                )
        self.story[0].add_field(name="คำแนะนำ",
                                value="วันแรกของการรันเซิร์ฟเวอร์ไปจนครบ 1 อาทิตย์"
                                      " ผู้เล่นต้องตามหาและสร้างปาร์ตี้ เพื่อก่อตั้งหมู่บ้าน และ"
                                      "ระดมสรรพกำลังเพื่อจัดเตรียมและกักตุนอาหาร อาวุธและยานพาหนะต่าง ๆ"
                                      "สำหรับผู้เล่นเดี่ยว (โซโล่) ให้กักตุนอาหารและยานพาหนะไว้เช่นเดียวกัน"
                                ,inline=False)
        self.story[1].set_image(url=img_('story_frist'))


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
