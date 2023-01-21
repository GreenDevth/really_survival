import discord
from discord.utils import get
from discord.ext import commands
from discord.commands import SlashCommandGroup, Option

from func.config import update_cooldown, get_cooldown_time
from scripts.guilds import guild_data, roles_lists
from db.users import Users
from db.town import City
from session.SessionContent import event_001

event_list = [
    "บทที่ 1",
    "บทที่ 2",
    "บทที่ 3",
    "บทที่ 4",
    "บทที่ 5",
    "บทที่ 6",
    "บทที่ 7",
    "บทที่ 8",
    "บทที่ 9",
    "บทที่ 10"
]
guild_id = guild_data()["roleplay"]
commands_list = ["ข้อมูลผู้เล่น", "ข้อมูลการเงิน", "ปรับบทบาท"]
permissions_roles = roles_lists()
class AdminCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    admin = SlashCommandGroup(guild_ids=[guild_id], name="admin", description="คำสั่งสำหรับแอดมิน")

    @admin.command(name="จัดการผู้เล่น", description="จัดการผู้เล่นในดิสคอร์ดเซิร์ฟเวอร์")
    async def manage_player(
            self,
            ctx:discord.Interaction,
            member:Option(discord.Member, "เลือกผู้เล่น"),
            command:Option(str,"เลือกคำสั่งที่ต้องการ", choices=commands_list),
            roles :Option(default=None, choices=permissions_roles)

    ):
        guild = ctx.guild
        member = guild.get_member(int(member.id))
        await ctx.response.defer(ephemeral=True, invisible=False)
        msg = await ctx.followup.send(f"โปรดรอสักครู่ ระบบกำลังดำเนินการจัดการ {command} ให้กับ {member.mention}")
        if command == commands_list[2]:
            try:
                role = get(guild.roles,name=roles)
                if role:
                    await member.add_roles(role)
            except Exception as e:
                await msg.edit(content=e)
            return await msg.edit(content=f"ระบบทำการ {command} {roles} ให้กับ {member.mention} เรียบร้อยแล้ว")

    @admin.command(name="จัดการคลูดาวน์ของปุ่มกด", description="คำสั่งสำหรับปรับแก้จำนวนเวลา cooldown ของปุ่มกด")
    async def manage_cooldown(
            self,
            ctx:discord.Interaction,
            amount:Option(int, "ระบุจำนวนเวลาให้กับระบบ คิดเป็น วินาที")):
        await ctx.response.defer(ephemeral=True, invisible=False)
        try:
            update_cooldown(amount)
            await ctx.followup.send(f"ทำการปรับ Cooldown Button เป็น {get_cooldown_time()} เรียบร้อยแล้ว")
        except Exception as e:
            await ctx.followup.send(e)

    @admin.command(name="จัดการฐานข้อมูล", description="ระบบจัดการฐานข้อมูล")
    async def database_manager(
            self,
            ctx:discord.Interaction,
            db_name:Option(str, "ระบบชื่อฐานข้อมูล")
    ):
        try:
            if db_name == "users":
                Users().drop_table()
                Users().create_table()
                return await ctx.response.send_message(f"reset {db_name} successfully...", ephemeral=True)
            elif db_name == "town":
                City().drop_table()
                City().create_table()
                return await ctx.response.send_message(f"reset {db_name} successfully...", ephemeral=True)
            else:
                return await ctx.response.send_message(f"database -> ` {db_name} ` : ไม่มีอยู่ในระบบ", ephemeral=True)
        except Exception as e:
            return await ctx.response.send_message(e, ephemeral=True)

    @admin.command(name="เช็คสิทธิ์ใช้งานเซิร์ฟคงเหลือ", description="ระบบตรวจสอบจำนวนสิทธิ์คงเหลือ")
    async def access_total(self,ctx:discord.Interaction):
        await ctx.response.send_message(Users().user_count()[0], ephemeral=True)


    @admin.command(name="ปรับสิทธิ์ใช้งานเซิร์ฟ", description="ระบบปรับสิทธิ์การเข้าใช้งานเซิร์ฟเวอร์")
    async def access_approved(
            self,
            ctx:discord.Interaction,
            choise:Option(str, "เลือกคำสั่งที่ต้องการ", choices=["ถอนสิทธิ์", "ให้สิทธิ์"]),
            member:Option(discord.Member, "เลือกผู้เล่นที่ต้องการปรับสิทธิ์เข้าใช้งานเซิร์ฟ")
    ):
        method = ["ถอนสิทธิ์", "ให้สิทธิ์"]
        try:
            if choise == method[0]:
                Users().approved(member.id, 0)
                return await ctx.response.send_message(f"ระบบทำการปลดสิทธิ์เข้าใช้งานสำหรับ {member.mention} เรียบร้อยแล้ว", ephemeral=True)
            elif choise == method[1]:
                Users().approved(member.id, 1)
                return await ctx.response.send_message(f"ระบบทำการปรับสิทธิ์เข้าใช้งานให้กับ {member.mention} เรียบร้อยแล้ว", ephemeral=True)
        except Exception as e:
            return await ctx.response.send_message(e, ephemeral=True)


    @admin.command(name="ติดตั้งระบบแสดงเนื้อหากิจกรรม", description="คำสั่งติดตั้งแคตตากอรี่และแชลแนลสำหรับแสดงเนื้อหาของอีเว้น")
    async def session_content(
            self,
            ctx:discord.Interaction,
            method:Option(str, "เลือกคำสั่งที่ต้องการ", choices=["install", "uninstall"]),
            session:Option(str, "เลือกอีเว้นที่ต้องการ", choices=event_list)
    ):
        guild = ctx.guild
        choices = ["install", "uninstall"]
        if method == choices[0]:
            cate = "EVENT CONTENT"
            overwrites = {
                guild.default_role : discord.PermissionOverwrite(
                    view_channel=True,
                    read_messages=True,
                    read_message_history=True,
                    send_messages=False
                )
            }
            try:
                if discord.utils.get(guild.categories, name=cate):
                    pass
                else:
                    await guild.create_category(name=cate, overwrites=overwrites)
            except Exception as e:
                return await ctx.response.send_message(e, ephemeral=True)
            else:
                if session == event_list[0]:
                    channel_name = "📔-บทที่-1"
                    try:
                        cates = discord.utils.get(guild.categories, name=cate)
                        channel = discord.utils.get(guild.channels, name=channel_name)
                        if channel:
                            await channel.purge()
                            await channel.send(embed=event_001())
                        else:
                            channel = await guild.create_text_channel(name=channel_name, category=cates)
                            if channel:
                                await channel.purge()
                                await channel.send(embed=event_001())
                                await ctx.response.send_message(f"{session}", ephemeral=True)
                    except Exception as e:
                        return await ctx.response.send_message(e, ephemeral=True)
                    finally:
                        await ctx.response.send_message(f"จัดการเนื้อหาของ {session} เรียบร้อยแล้ว", ephemeral=True)

        elif method == choices[1]:
            await ctx.response.send_message(f"{method}", ephemeral=True)




def setup(bot):
    bot.add_cog(AdminCommand(bot))