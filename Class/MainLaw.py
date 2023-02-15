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
    embed.add_field(name="ข้อที่ 1 การขโมย",
                    value="งัดหรือขโมยยานพาหนะสามารถทำได้ หากสิ่งของเหล่านั้นอยู่นอกบ้านหรือนอกเขตธงของผู้เล่น"
                    ,inline=False)
    embed.add_field(name="ข้อที่ 2 ทำร้ายผู้เล่น",
                    value="กรณีเกิดการปะทะกันอนุญาตให้ใช้การชกต่อย และการใช้อาวุธระยะประชิดในการทำให้คู่กรณี เจ็บหนักและยอมแพ้แต่ไม่ถึงตาย"
                          "สามารถทำการจับกุม และดำเนินตามความเหมาะสมได้ (ควรมีการต่อรองก่อนการปะทะกัน และไม่ควรทำให้ถึงกับตัวละครตาย)"
                    , inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/1012319234841387109/1065840430232637450/barn.png")
    return embed

class MainLawCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    law = SlashCommandGroup(guild_ids=[guild_id], name="law", description="คำสั่งจัดการแสดงเนื้อหาเกี่ยวกับ กฎและกติกา")

    @law.command(name="กฎกติกาหลัก", description="คำสั่งแสดง กฎและ กติกาหลักของเซิร์ฟ")
    async def main_law(self, ctx:discord.Interaction, command:Option(str, "เลือกคำสั่งที่ต้องการ", choices=["Show"])):
        guild = ctx.guild

        await ctx.response.defer(ephemeral=True, invisible=False)
        msg = await ctx.followup.send("⏳ รอสักครู่ระบบกำลังประมวลผลการทำงาน")

        ch_name="📕-กฎและข้อบังคับ"

        if command == "Show":
            try:
                channel = discord.utils.get(guild.channels, name=ch_name)
                if channel:
                    await channel.purge()
                else:
                    channel = await guild.create_text_channel(name=ch_name)
                    await channel.set_permissions(guild.default_role, view_channel=True, send_messages=False)
                    await channel.send(embed=law_information())

            except Exception as e:
                return await msg.edit(content=e)
            else:
                return await msg.edit(content=f"สร้างห้อง {channel.mention} สำเร็จ")



