import discord
from discord.ext import pages, commands

from scripts.guilds import Occupation, get_cooldown_time, guild_data

guild_id = guild_data()["roleplay"]
occ = Occupation()


class PopulationManualView(discord.ui.View):
    def __init__(self, bot):
        super(PopulationManualView, self).__init__(timeout=None)
        self.bot = bot
        self.cooldown = commands.CooldownMapping.from_cooldown(1, int(get_cooldown_time()), commands.BucketType.member)
        self.occ = [
            discord.Embed(
                title="เกษตรกร - FARMER",
                description="อาชีพเกษตรกร ผู้เล่นได้สวมบทบาทเป็นผู้ผลิตและจัดหา ผลิตภัณฑ์ด้านการเกษตร ซื้อหรือขายสินค้าด้านการเกษตรให้กับผู้เล่นคนอื่นหรือขายให้กับระบบ"
                            "โดยผู้เล่นที่เป็นเกษตร จะได้รับส่วนลดในการสั่งซื้ออุปกรณ์และสิ่งของจากระบบรวมถึงจะได้รับเปอร์เซ็นต์เพิ่มจากการขายของให้กับระบบ ส่วนอื่นนอกจากบทบาทที่ได้รับ ให้เป็นไปตามรูปแบบของเกมส์"
            ),
            discord.Embed(
                title="วิศวกร - ENGINEER",
                description="อาชีพวิศวกร คือกลุ่มของผู้เล่นที่ให้บริการด้านการสร้าง ซ่อมแซม ต่อเดิมสิ่งของต่าง ๆ ให้กับผู้รับบริการ"
                            "และผู้เล่นที่เป็นวิศวกร จะได้สิทธิ์ในการสั่งซื้อสินค้าประเภทอุปกรณ์ก่อสร้างต่าง ๆ ในราคาที่ถูกกว่า และจะขายสินค้าให้กับระบบได้ราคาแพงกว่า ผู้เล่นอาชีพอื่น ๆ และนอกเหนือจากบทบาทที่ได้รับนี้ ให้เป็นไปตามรูปแบบของเกมส์"
            ),
            discord.Embed(
                title="พ่อค้า - SELLER",
                description="อาชีพพ่อค้า เป็นผู้ประกอบการธุรกิจค้าขาย ซึ่งระบบจะจำกัดอยู่เพียง 3 อัตราเท่านั้น พ่อค้า จะได้รับอภิสิทธิ์พิเศษเรื่องการสั่งซื้อของราคาถูก และขายของได้ในราคาที่แพง"
                            " และสามารถใช้งานคำสั่งระบบฝากขายสินค้าได้ สามารถขอเงินทุนในลักษณะของการกู้ยิมเงินกับระบบได้ โดยไม่เกิน 1,000,000.- discord coins และไม่มีดอกเบี้ย ส่วนที่นอกเหนือจากบทบาทเหล่านี้ให้เป็นไปตามรูปแบบของเกมส์"
            ),
            discord.Embed(
                title="นักผจญภัย - ADVENTURER",
                description="นักผจญภัย เป็นอาชีพอิสระไม่มีการผูกมัดหรือสิทธิ์พิเศษใด สามารถซื้อขายของได้ตามปกติทั่วไป และอาจจะได้รับภารกิจพิเศษเช่นการสำรวจพื้นที่ต่าง ๆ และยังจะเป็นหนึ่งในอาชีพที่คอยบุกเบิกเสาะแสวงหาพื้นที่สำหรับอยู่อาศัยของพลเมือง"
            ),
        ]
        self.occ[0].set_image(url=occ["farmer_img"])
        self.occ[1].set_image(url=occ["engineer_img"])
        self.occ[2].set_image(url=occ["seller_img"])
        self.occ[3].set_image(url=occ["hunter_img"])
        self.pop = [
            discord.Embed(
                title="พลเมือง - CITIZEN",
                description="พลเมือง ( CITIZEN ) คือ ผู้เล่นหรือกลุ่มของผู้เล่นที่จดทะเบียนเป็นพลเมือง"
                            " ได้รับสิทธิ์ให้อาศัยในพื้นที่เขตชุมชน คำสั่งดิสคอร์ดและได้รับการปกป้องที่อยู่อาศัยและทรัพย์สิน ภายในพื้นที่เขตชุมชน"
                            " เหตุการณ์ต่าง ๆนอกเขตชุมชนให้เป็นไปตามพื้นฐานของรูปแบบเกมส์ พลเมืองจะมีสิทธิ์ในการจดทะเบียนอาชีพตามที่ตนสนใจ ระบบจะจำกัดจำนวนคนในการจดทะเบียนอาชีพ พ่อค้า และ วิศวกร"
            ),
            discord.Embed(
                title="อาชญากร - BANDIT",
                description="โจรหรืออาชญากร ( BANDIT ) คือ ผู้เล่นหรือกลุ่มของผู้เล่นที่เลือกลงทะเบียนเป็นอาชญากร"
                            " กลุ่มของผู้เล่นประเภทอาชญากรจะไม่ได้รับความช่วยเหลือใด ๆ"
                            "และไม่สามารถใช้งานคำสั่งดิสคอร์ดบางรายการได้ ไม่อนุญาติให้สร้างบ้านหรืออยู่อาศัยในพื้นที่เขตชุมชน กลุ่มของผู้เล่นประเภทอาชญากรต้องอาศัยการยึดบ้าน NPC สำหรับเป็นที่กลบดาน"
                            "และมีสิทธิ์ในการซื้อที่ดินสำหรับปลูกสร้างที่อยู่ในพื้นที่รกร้างได้ โดยพื้นที่ 1 เขตธง จะมีมูลค่าเท่ากับ 50,000.- และจำกัดเพียง 1 คน หรือปาร์ตี้ละ 1 เขตธงเท่านั้น"
            ),
            discord.Embed(
                title="คนเร่ร่อน - HOMELESS",
                description="คนไร้บ้านหรือคนเร่ร่อน ( HOMELESS ) คือ ผู้เล่นหรือกลุ่มของผู้เล่นที่เลือกลงทะเบียนเป็นคนพเนจร กลุ่มของผู้เล่นประเภทนี้จะไม่สามารถใช้งานคำสั่งดิสคอร์ดบางรายการได้"
                            "เป็นกลุ่มคนที่ไม่มีที่อยู่อาศัยเป็นหลักแหล่ง และอาจจะหรือไม่ได้เป็นบุคคลอันตรายเช่นเดียวกับอาชญากร ผู้เล่นประเภทคนพเนจร สามารถอาศัยตามบ้าน NPC ได้เช่นเดียวกันกับ"
                            "ผู้เล่นประเภทอาชญากร และยังมีสิทธิ์ในการซื้อที่ดินสำหรับปลูกสร้างที่อยู่ในพื้นที่รกร้างได้"
            ),
        ]
        self.pop[0].set_image(
            url="https://cdn.discordapp.com/attachments/1012319234841387109/1026745266126209075/unknown.png")

        self.pop[1].set_image(
            url="https://cdn.discordapp.com/attachments/1012319234841387109/1026756274983018536/943854.jpg")

        self.pop[2].set_image(
            url="https://cdn.discordapp.com/attachments/1012319234841387109/1026754023967178842/49338-497788-SCUM003jpg-noscale.jpg")
        self.law = [
            discord.Embed(
                title="การสร้างสิ่งปลูกสร้าง - BUILDING",
                description="กติกาและข้อบังคับเกี่ยวกับการสร้างสิ่งปลูกสร้างต่าง ๆ ผู้เล่นทุกคนสามารถสร้างสิ่งปลูกสร้าง บ้าน หรือฐานที่มั่นของตนเองได้ เว้นแต่กลุ่มผู้เล่นประเภท"
                            "อาชญากรและคนพเนจร จะไม่ได้รับสิทธิ์ในการเข้ามาสร้างสิ่งปลูกสร้างต่าง ๆ ในพื้นที่เขตชุมชน และจะไม่สามารถปักธงสร้างสิ่งปลูกสร้างได้ในพื้นที่บนเกาะ"
                            "ทั้งหมดเว้นแต่ได้ทำการซื้อที่ดินไว้เป็นของตนเอง โดยระบบจำกำหนดราคา ของพื้นที่ในการปักธงไว้ดังนี้\n"
                            "- พื้นที่โดยทั่วไป ราคา 50,000.- ต่อ 1 เขตธง\n"
                            "- เกาะขนาดเล็ก ราคา 2,500,000.- ต่อ 1 เขตธง\n"
                            "- เกาะขนาดเล็ก ราคา 1,500,000.- ต่อ 1 เขตธง\n"
                            "โดยระเว้นการขอซื้อที่ดินในพื้นที่จุดฟาร์ม ให้ถือว่าเป็นพื้นที่สาธารณะไม่อนุญาติให้เป็นเจ้าของ"
            ),
            discord.Embed(
                title="ยานพาหนะ - VEHICLE",
                description="ยานพาหนะทุกคันจะทำลายตัวเองใน 7 วันหากเจ้าของไม่ได้ใช้งาน ผู้เล่นทุกคนต้องซื้อเอาจาก Outpost และ Discord Store โดยระบบได้"
                            "แยกประเภทของยานพาหนะออกเป็น รถที่นำเข้าและเสียภาษีเรียบร้อย กับ รถ HellRiders ที่ให้ตีเป็นรถหนีภาษีและผิดกฎหมาย "
                            "การครอบครองยานภาหนะ สามารถครอบครองได้ไม่จำกัด ตามที่ผู้เล่นสามารถหาเงินซื้อมาได้ เว้นแต่ ต้องปฏิบัติการกติกาของเซิร์ฟ ซึ่งประกอบด้วย\n"
                            "- ผู้เล่นประเภทพลเมืองทุกคนต้องมีใบขับขี่\n"
                            "- ยานพาหนะทุกคันต้องมีทะเบียนและเสียภาษีให้เรียบร้อย\n"
            ),
            discord.Embed(
                title="การปล้นสะดม - RAID",
                description="รูปแบบบเซิร์ฟไม่ใช่ PVE หรือ PVP แต่เป็นการอิงความเป็นจริงของรูปแบบชีวิตประจำวัน ที่มีทั้ง เพื่อน ศัตรู และอันตรายจากสิ่งแวดล้อมอื่น ๆ"
                            "ดังนั้น รูปแบบการเล่นจึงจัดให้เป็นแบบไม่มีปาร์ตี้และไม่มีแผนที่ รวมถึงเน้นให้เข้ากลุ่มเป็นชุมชน หมู่บ้าน หรือเมือง การปล้นสะดม (RAID) จะเป็นเพียง"
                            "อีเว้นที่เกิดขึ้นได้ตามปกตินอกเขตชุมชน อาจจะเป็นในลักษณะของการดักปล้น ขโมย หรือฆ่าชิงทรัพย์ของผู้เล่นคนอื่น"
            ),
        ]
        self.law[0].set_image(url="https://cdn.discordapp.com/attachments/1012319234841387109/1027110515568283748/41f37e1ee429942a7bece96526270fc1b4bc7ce3.jpg")
        self.law[1].set_image(url="https://cdn.discordapp.com/attachments/1012319234841387109/1027113979505545216/unknown.png")
        self.law[2].set_image(url="https://cdn.discordapp.com/attachments/1012319234841387109/1027117812910673932/raid.jpg")

    def get_occ(self):
        return self.occ

    def get_pop(self):
        return self.pop

    def get_law(self):
        return self.law

    @discord.ui.button(label="ข้อมูลตัวละคร", style=discord.ButtonStyle.secondary, emoji="🧑",
                       custom_id="citizen_manual")
    async def citizen_manual(self, button, interaction: discord.Interaction):
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f'อีก {round(retry, 1)} วินาที คำสั่งถึงจะพร้อมใช้งานอีกครั้ง', ephemeral=True)
        button.disabled = False
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
                pages=self.get_pop(),
                show_disabled=True,
                show_indicator=True,
                use_default_buttons=False,
                custom_buttons=pagelist,
                loop_pages=False,
            )
            await paginator.respond(interaction, ephemeral=True)
        except Exception as e:
            return await interaction.followup.send(e)

    @discord.ui.button(label="ข้อมูลอาชีพ", style=discord.ButtonStyle.secondary, emoji="💼",
                       custom_id="city_manual")
    async def city_manual(self, button, interaction: discord.Interaction):
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f'อีก {round(retry, 1)} วินาที คำสั่งถึงจะพร้อมใช้งานอีกครั้ง', ephemeral=True)
        button.disabled = False
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
                pages=self.get_occ(),
                show_disabled=True,
                show_indicator=True,
                use_default_buttons=False,
                custom_buttons=pagelist,
                loop_pages=False,
            )
            await paginator.respond(interaction, ephemeral=True)
        except Exception as e:
            return await interaction.followup.send(e)

    @discord.ui.button(label="กติกาของเกมส์", style=discord.ButtonStyle.secondary, emoji="⚖", custom_id="law_manual")
    async def map_manual(self, button, interaction: discord.Interaction):
        button.disabled = False
        await interaction.response.defer(ephemeral=True, invisible=False)
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f'อีก {round(retry, 1)} วินาที คำสั่งถึงจะพร้อมใช้งานอีกครั้ง', ephemeral=True)

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
                pages=self.get_law(),
                show_disabled=True,
                show_indicator=True,
                use_default_buttons=False,
                custom_buttons=pagelist,
                loop_pages=False,
            )
            await paginator.respond(interaction, ephemeral=True)
        except Exception as e:
            return await interaction.followup.send(e)
