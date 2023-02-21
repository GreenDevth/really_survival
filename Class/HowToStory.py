import discord
from discord.ext import commands
from discord.commands import slash_command, Option

from scripts.guilds import guild_data
from func.config import img_

guild_id = guild_data()['realistic']


class HowToStoryCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(self.__class__.__name__)


    @slash_command(name="hostage")
    async def hostage(self, ctx:discord.Interaction, session:Option(str,"พิม์เนื้อหาที่ต้องการแสดง")):
        guild = ctx.guild
        await ctx.response.defer(ephemeral=True, invisible=False)
        msg = await ctx.followup.send("ระบบกำลังประมวลผลการทำงาน")

        try:
            ch_name="📙-แนวปฏิบัติร่วมกัน"
            channel = discord.utils.get(guild.channels, name=ch_name)
            if channel:
                pass
            else:
                channel = await guild.create_text_channel(name=ch_name)
                await channel.set_permissions(guild.default_role, view_channel=True, send_messages=False)
        except Exception as e:
            print(e)
        else:

            if session == "hostage_1":

                embed = discord.Embed(
                    title="🪑 แนวทางในการจับตัวประกัน",
                    description="แนวทางหรือข้อตกลงร่วมกันในกรณีผู้เล่นถูกจี้ปล้น หรือ ถุกจับเป็นตัวประกัน เพื่อให้มีแนวทางไปในรูปแบบเดียวกันเซิร์ฟจึงจำเป็นต้องกำหนดแนวทางปฏิบัติดังนี้"
                )
                embed.add_field(name="ข้อตกลงและแนวทางปฏิบัติ",
                                value="```yaml\n"
                                      "+ หากูกจับและปืนจ่อหัวในระยะหวังผลให้ผู้เล่นยินยอมแต่โดยดี\n"
                                      "+ ทีมของผู้ถูกจับห้ามขัดขืน ต่อสู้และปล่อยให้เพื่อนถูกจับไป\n"
                                      "+ ต้องแจ้งข้อเรียกร้องให้เชลยทราบภายใน 30 นาที\n"
                                      "+ เชลยต้องติดต่อเจ้าเมืองของตนเพื่อแจ้งข้อเรียกร้อง\n"
                                      "+ เจ้าเมืองทั้ง 2 ทำการเจรจาต่อรองจนกว่าจะได้ข้อสรุป\n"
                                      "+ หากการต่อรองไม่สำเร็จให้เปิด ศึกชิงตัวประกันได้\n"
                                      "+ ต้องแจ้งวันและเวลาของศึกชิงตัวประกันต่อแอดมิน\n"
                                      "+ ฝ่ายแพ้ต้องชดเชยค่าเสียหายเป็น 2% ของข้อเรียกร้อง\n"
                                      "\n```",
                                inline=False)
                embed.set_image(url=img_("hostage"))
                await channel.send(embed=embed)
            elif session == "hostage_2":
                embed = discord.Embed(
                    title="👤 ตัวประกัน",
                    description="แนวปฏิบัติกรณีถูกจับเป็นตัวประกัน และการปฏิบัติต่อเชลย เพื่อให้เป็นไปในแนวทางเดียวกันเซิร์ฟจึงกำหนดแนวปฏิบัติโดยมีเนื้อหาดังนี้"
                )
                embed.add_field(name="ข้อตกลงและแนวปฏิบัติ",
                                value="```yaml\n"
                                      "+ ผู้ที่ถูกจับตัวต้องให้ความร่วมมือจนกว่าจะถูกนำตัวไป\n"
                                      "+ ระหว่างการเดินทางห้ามขัดขืนห้ามมีการแย่งชิงเชลย\n"
                                      "+ เมื่อเชลยถึงที่หมายต้องขังในที่มิดชิดและมีการป้องกัน\n"
                                      "+ หากสถานที่คุมขังมีช่องให้หลบหนีเชลยสามารถทำได้\n"
                                      "+ การปฏิบัติต่อเชลยต้องอย่าทำให้ถึงตาย ห้องขังต้องมี\n"
                                      "+ การช่วยตัวประกันทำได้ในศึกแย่งตัวประกันเท่านั้น\n"
                                      "\n```", inline=False)
                embed.set_image(url=img_("hostage_2"))
                await channel.send(embed=embed)

            elif session == "hostage_3":
                embed = discord.Embed(
                    title="💼 การประกันตัวและการส่งมอบ",
                    description="แนวปฏิบัติในการส่งมอบตัวประกัน และเพื่อให้เป็นไปในแนวทางเดียวกันเซิร์ฟจึงกำหนดแนวปฏิบัติโดยมีเนื้อหาดังนี้"
                )
                embed.add_field(name="ข้อตกลงและแนวปฏิบัติ",
                                value="```yaml\n"
                                      "+ ระหว่างเดินทางเชลยห้ามขัดขืนให้ถือว่าหลับหรือสลบอยู่\n"
                                      "+ การนัดหมายต้องเป็นไปตามข้อตกลงทั้งสองฝ่าย\n"
                                      "+ การส่งมอบค่าไถ่และเชลยต้องเป็นแบบ 1 ต่อ 1\n"
                                      "+ ลูกน้องคนอื่น ๆ ต้องอยู่ห่างจากคนนำส่ง 100 เมตร\n"
                                      "+ ห้ามปะทะกันเด็ดขาด อาจจะมีการยิงปืนขึ้นฟ้าได้\n"
                                      "+ การส่งมอบเชลยสามารถทำได้ทันทีเมื่อทั้งสองฝ่ายพร้อม\n"
                                      "\n```", inline=False)
                embed.set_image(url=img_("hostage_3"))
                await channel.send(embed=embed)

            return await msg.edit(content="ติดตั้งแนวปฏิบัติให้กับเซิร์ฟเรียบร้อย")





