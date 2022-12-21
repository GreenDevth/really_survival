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
                title="บทที่ 1 ช่วงเวลาที่แสนสุข",
                description="ใน 1 อาทิตย์นับตั้งแต่เริ่มเปิดให้เข้าใช้งานเซิร์ฟเวอร์ เซิร์ฟเวอร์จะเปิดโอกาสให้ผู้เล่นเตรียมตัว ทั้งเรื่องของการสร้างบ้าน (หมู่บ้าน)"
                            "เรื่องของการกักตุนเสบียง และยานพาหนะต่าง ๆ (3 คันต่อปาร์ตี้ 1 คัน ต่อผู้เล่นสันโดษ) โดยจะปรับตั้งค่าเซิร์ฟ ดรอปตามพื้นที่ 10% และของที่กดค้นหา"
                            " จะอยู่ที่ 0.5% (เพื่อไม่ให้กักตุนอาวุธมากจนเกินไป) ไม่มีหุ่นยนต์ ซอมบี้ปานกลาง ไม่มีซอมบี้ระเบิด เปิดใช้งานแผนที่ เปิดดาเมจในจุดฟาร์มหลัก ๆ outpost ใช้ค่าเริ่มต้น"
                            "ดังนั้นผู้เล่นที่ได้ทำการสร้างกลุ่มตามที่ระบบกำหนด และผู้เล่นประเภทสันโดษ (โซโล่) ต้องพยายามกักตุนอาหารและอาวุธให้พร้อมสำหรับการเปลี่ยนแปลงในครั้งต่อไป",
                colour=discord.Colour.from_rgb(85, 226, 32)
            ),
            discord.Embed(
                title="วิศวกร - ENGINEER",
                description="อาชีพวิศวกร คือกลุ่มของผู้เล่นที่ให้บริการด้านการสร้าง ซ่อมแซม ต่อเดิมสิ่งของต่าง ๆ ให้กับผู้รับบริการ"
                            "และผู้เล่นที่เป็นวิศวกร จะได้สิทธิ์ในการสั่งซื้อสินค้าประเภทอุปกรณ์ก่อสร้างต่าง ๆ ในราคาที่ถูกกว่า และจะขายสินค้าให้กับระบบได้ราคาแพงกว่า ผู้เล่นอาชีพอื่น ๆ และนอกเหนือจากบทบาทที่ได้รับนี้ ให้เป็นไปตามรูปแบบของเกมส์",
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
        self.story[0].add_field(name="Event",
                                value="ผู้เล่นที่สร้างปาร์ตี้ตามที่ระบบกำหนด จะต้องหาตำแหน่งและสร้างหมู่บ้านของตนเองให้ได้ภายใน 1 อาทิตย์ โดยหัวห้าปาร์ตี้จะได้รับชุดอุปกรณ์ในการตัดไม้และยานพาหนะจำนวนนึงไว้สำหรับสร้างหมู่บ้านของตน"
                                      "และในระหว่างการออกฟาร์มของในเขตพื้นที่สีแดง หากมีการปะทะกันเกิดขึ้นการสูญเสียต่าง ๆ ถือเป็นความผิดพลาดของกลุ่มผู้เล่นระบบจะไม่ชดเชยให้ทุกกรณี")

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
