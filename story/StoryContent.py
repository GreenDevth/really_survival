import discord
from discord.ext import commands, pages

from func.config import get_cooldown_time, img_, channels_


class StoryView(discord.ui.View):
    def __init__(self, bot):
        super(StoryView, self).__init__(timeout=None)
        self.bot = bot
        self.cooldown = commands.CooldownMapping.from_cooldown(1, int(get_cooldown_time()), commands.BucketType.member)
        self.story = [
            discord.Embed(
                title="📖บ ทที่ 1 ช่วงเวลาที่แสนสุข",
                description="ใน 1 อาทิตย์นับตั้งแต่เริ่มเปิดให้เข้าใช้งานเซิร์ฟเวอร์ จะเปิดโอกาสให้ผู้เล่นเตรียมตัว ทั้งเรื่องของการสร้างบ้าน (หมู่บ้าน)"
                            f"เรื่องของการกักตุนเสบียง และยานพาหนะต่าง ๆ\n\n(ข้อตกลงการครอบครองยานพาหนะ <#{channels_()['law']}>)\n\nเซิร์ฟจะปรับการตั้งค่าดังนี้\n"
                            "\n- ปิดหุ่นยนต์ และซอมบี้ระเบิด เปิดใช้งานแผนที่"
                            "\n- เรทดรอปตามพื้น 10% และกดค้นหา 0.5%"
                            "\n- มีดาเมจเฉพาะจุดฟาร์มหลัก ๆ และซอมบี้ประปราย"
                            "\n- outpost ซื้อขายได้ตลอด ราคาตามค่าเริ่มต้น\n"
                            "\nผู้เล่นที่สร้างปาร์ตี้ตามระบบกำหนด และประเภท Solo ต้องพยายามกักตุนอาหารและอาวุธให้พร้อมสำหรับการเปลี่ยนแปลงในครั้งต่อไป",
                colour=discord.Colour.from_rgb(85, 226, 32)
            ),
            discord.Embed(
                title="📖 บทที่ 2 โรคระบาดครั้งใหญ่",
                description="อาทิตย์ที่ 2 หลังจากที่ผู้เล่นได้เตรียมพร้อมรับการเปลี่ยนแปลงครั้งใหญ่ของเซิร์ฟ โดยการสร้างหมู่บ้าน (สำหรับผู้เล่นที่สร้างปาร์ตี้ตามที่ระบบกำหนด) หรือสร้างที่พักพิง (โซโล่) การกักตุนอาหาร และอาวุธพร้อมเรียบร้อย"
                            "\n\nเซิร์ฟจะปรับการตั้งค่าเป็นดังนี้\n"
                            "- เพิ่มจำนวนซอมบี้ในจุดฟาร์มสูงสุด\n"
                            "- ลดอัตราการดรอปพื้น เหลือ 5% ส่วนจากการค้นหายังคงเท่าเดิม\n"
                            "- ปรับสถานีน้ำมันให้น้ำมันเหลือน้อยลง\n"
                            "- ปรับเพิ่มจำนวนรถแบบไม่มีเครื่อง\n\n"
                            "ผู้เล่นประจำแต่ละปาร์ตี้เตรียมเข้าภารกิจ ส่วนผู้เล่นเดี่ยวจะได้รับภารกิจเช่นเดียวกันหากต้องการ",
                colour=discord.Colour.from_rgb(85, 226, 32)
            ),
            discord.Embed(
                title="พ่อค้า - SELLER",
                description="อาชีพพ่อค้า เป็นผู้ประกอบการธุรกิจค้าขาย ซึ่งระบบจะจำกัดอยู่เพียง 3 อัตราเท่านั้น พ่อค้า จะได้รับอภิสิทธิ์พิเศษเรื่องการสั่งซื้อของราคาถูก และขายของได้ในราคาที่แพง"
                            " และสามารถใช้งานคำสั่งระบบฝากขายสินค้าได้ สามารถขอเงินทุนในลักษณะของการกู้ยิมเงินกับระบบได้ โดยไม่เกิน 1,000,000.- discord coins และไม่มีดอกเบี้ย ส่วนที่นอกเหนือจากบทบาทเหล่านี้ให้เป็นไปตามรูปแบบของเกมส์",
                colour=discord.Colour.from_rgb(85, 226, 32)
            ),
            discord.Embed(
                title="นักผจญภัย - ADVENTURER",
                description="นักผจญภัย เป็นอาชีพอิสระไม่มีการผูกมัดหรือสิทธิ์พิเศษใด สามารถซื้อขายของได้ตามปกติทั่วไป และอาจจะได้รับภารกิจพิเศษเช่นการสำรวจพื้นที่ต่าง ๆ และยังจะเป็นหนึ่งในอาชีพที่คอยบุกเบิกเสาะแสวงหาพื้นที่สำหรับอยู่อาศัยของพลเมือง",
                colour=discord.Colour.from_rgb(85, 226, 32)
            ),
        ]
        self.story[0].set_image(url=img_('story_intro'))
        self.story[0].add_field(name="คำแนะนำ",
                                value="ผู้เล่นที่สร้างปาร์ตี้ตามที่ระบบกำหนด จะต้องหาตำแหน่งและสร้างหมู่บ้านของตนเองให้ได้ภายใน 1 อาทิตย์ โดยหัวหน้าปาร์ตี้จะได้รับชุดอุปกรณ์สร้างบ้านและยานพาหนะจำนวนนึงไว้สำหรับสร้างหมู่บ้านของตน"
                                      " และในระหว่างการออกฟาร์ม ในเขตพื้นที่สีแดงหากมีการปะทะกันเกิดขึ้น การสูญเสียต่าง ๆ ถือเป็นความประมาทของกลุ่มผู้เล่นระบบจะไม่ชดเชยให้ทุกกรณี")

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
                    "first", label="<<-", style=discord.ButtonStyle.secondary
                ),
                pages.PaginatorButton("prev", label="<-", style=discord.ButtonStyle.secondary),
                pages.PaginatorButton(
                    "page_indicator", style=discord.ButtonStyle.gray, disabled=True
                ),
                pages.PaginatorButton("next", label="->", style=discord.ButtonStyle.secondary),
                pages.PaginatorButton("last", label="->>", style=discord.ButtonStyle.secondary),
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
