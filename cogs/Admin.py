import discord
from discord.commands import SlashCommandGroup, Option
from discord.ext import commands
from discord.utils import get

from db.Ranking import Ranking
from db.Events import Event, TeaserEvent
from db.town import City
from db.users import Users
from func.city import town_list
from func.config import update_cooldown, get_cooldown_time, update_sys, update_quest
from scripts.guilds import guild_data, roles_lists

guild_id = guild_data()["realistic"]
commands_list = ["ข้อมูลผู้เล่น", "ข้อมูลการเงิน", "ปรับบทบาท"]
permissions_roles = roles_lists()
class AdminCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    admin = SlashCommandGroup(guild_ids=[guild_id], name="admin", description="คำสั่งสำหรับแอดมิน")
    database = SlashCommandGroup(guild_ids=[guild_id], name="database", description="คำสั่งจัดการฐานข้อมูล")

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

    @database.command(name="จัดการฐานข้อมูล", description="ระบบจัดการฐานข้อมูล")
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
            elif db_name == "rank":
                Ranking().drop_table()
                Ranking().create_table()
                return await ctx.response.send_message(f"reset {db_name} successfully...", ephemeral=True)
            elif db_name == "event":
                Event().drop_table()
                Event().create_table()
                return await ctx.response.send_message(f"reset {db_name} successfully...", ephemeral=True)
            elif db_name == "teaser":
                TeaserEvent().drop_table()
                TeaserEvent().create_table()
                return await ctx.response.send_message(f"reset {db_name} successfully...", ephemeral=True)
            else:
                return await ctx.response.send_message(f"database -> ` {db_name} ` : ไม่มีอยู่ในระบบ", ephemeral=True)
        except Exception as e:
            return await ctx.response.send_message(e, ephemeral=True)


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


    @admin.command(name="ควบคุมระบบลงทะเบียน", description="คำสั่งเปิดหรือปิดระบบลงทะเบียน")
    async def register_system(self, ctx:discord.Interaction, method:Option(str, 'เลือกคำสั่งที่ต้องการ', choices=["Open", "Close"])):
        try:
            update_sys(method)
        except Exception as e:
            return await ctx.response.send_message(e, ephemeral=True)
        else:
            return await ctx.response.send_message(f"{method} ระบบลงทะเบียนเรียบร้อยแล้ว", ephemeral=True)

    @admin.command(name="ควบคุมระบบเควส", description="คำสั่งเปิดหรือปิดระบบเควส")
    async def system_quest(self, ctx: discord.Interaction,
                              method: Option(str, 'เลือกคำสั่งที่ต้องการ', choices=["Open", "Close"])):
        try:
            update_quest(method)
        except Exception as e:
            return await ctx.response.send_message(e, ephemeral=True)
        else:
            return await ctx.response.send_message(f"{method} ระบบลงทะเบียนเรียบร้อยแล้ว", ephemeral=True)


    @admin.command(name="town", description="คำสั่งตรวจสอบสิทธิ์ของจำนวนเมืองคงเหลือ")
    async def limit_town(self, ctx:discord.Interaction, town:Option(str, "เลือกเมืองที่ต้องการตรวจสอบ", choices=town_list)):
        await ctx.response.defer(ephemeral=True, invisible=False)
        msg = await ctx.followup.send("โปรดรอสักครู่ระบบกำลังประมาลผลการทำงาน")
        try:
            amount = City().citizen_count(town)
            if amount:
                pass
            else:
                raise Exception("ไม่พบข้อมูลที่ต้องการตรวจสอบ")
        except Exception as e:
            return await msg.edit(content=e)
        else:
            await msg.edit(content=amount)

def setup(bot):
    bot.add_cog(AdminCommand(bot))