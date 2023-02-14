import discord
import json
from discord.ext import commands
from discord.commands import SlashCommandGroup, Option

from db.users import Users
from func.config import img_
from registers.Reg_info import Register_Access
from registers.SubPlayer_Reg import SubPlayer_Register_Access
from scripts.guilds import guild_data

guild_id = guild_data()["realistic"]

channel_name = "📝-ลงทะเบียนเพิ่มเติม"

def user_check():
    total = Users().user_count()
    if total > 48:
        return True
    elif total < 48:
        return False


def get_subplayer():
    with open('./json_file/sys.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data["subplayer"]

def update_subplayer(method):
    system_file = open('./json_file/sys.json', 'r', encoding='utf-8')
    json_object = json.load(system_file)
    system_file.close()

    json_object["subplayer"] = method
    system_file = open('./json_file/sys.json', 'w', encoding='utf-8')
    json.dump(json_object, system_file, ensure_ascii=False, indent=4)
    system_file.close()

def subregister():
    embed = discord.Embed(
        title="ลงทะเบียนเพิ่มเติม",
        description="การลงทะเบียนเพิ่มเติมจะเปิดโอกาสให้ผู้ที่ต้องการเข้าร่วมโปรเจคสามารถลงทะเบียนเป็น SubPlayer ไว้สำหรับเข้าใช้งานได้ โดยต้องยอมรับข้อตกลงของเซิร์ฟด้วย"
    )
    embed.add_field(name="ข้อตกลงของเซิร์ฟ"
                    ,value="เซิร์ฟเปิดรับจอง Slot เพียง 40 Slot และปัจจุบันมีคนลงทะเบียนเต็มจำนวนแล้ว"
                           "ซึ่งหากสมาชิกต้องการเข้าร่วมโปรเจคนี้ สมาชิกต้องยอมรับความเสี่ยงกรณีเซิร์ฟเต็มแล้วถูกเซิร์ฟเชิญออก"
                           "และต้องสมทบทุนเช่าเซิร์ฟจำนวน 1 Slot ในราคา 100 บาทเพื่อจอง Slot สำหรับเข้าใช้งานเซิร์ฟ")
    embed.set_image(url=img_("reg"))
    return embed

class SubPlayerCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(SubPlayer_Register_Access(self.bot))

    subplayer = SlashCommandGroup(guild_ids=[guild_id], name="subplayer",description="คำสั่งจัดการระบบลงทะเบียนเพิ่มเติม")



    @subplayer.command(name="ระบบลงทะเบียน", description="คำสั่งเปิดใช้งานระบบลงทะเบียน")
    async def subplayer_register_command(self, ctx:discord.Interaction, method:Option(str, "เลือกคำสั่งที่ต้องการ", choices=["Open", "Close"])):
        guild = ctx.guild

        if method == "Open":
            try:
                channel = discord.utils.get(guild.channels, name=channel_name)
                if channel:
                    await channel.purge()
                    await ctx.response.send_message(f"update {channel.mention} successfull.", ephemeral=True)
                    await channel.send(embed=subregister(), view=SubPlayer_Register_Access(self.bot))
                    return await channel.set_permissions(guild.default_role, send_messages=False, view_channel=True)
                else:
                    channel = await guild.create_text_channel(name=channel_name)
                    await channel.set_permissions(guild.default_role, send_messages=False, view_channel=True)
            except Exception as e:
                print(e)
            else:
                await channel.send(embed=subregister(), view=SubPlayer_Register_Access(self.bot))
                return await ctx.response.send_message(f"create {channel.mention} successfull.", ephemeral=True)


