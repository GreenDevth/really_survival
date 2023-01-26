import discord
from discord.utils import get
from discord.ext import commands
from discord.commands import SlashCommandGroup, Option

from db.Ranking import Ranking
from func.config import update_cooldown, get_cooldown_time, img_, update_sys

from scripts.guilds import guild_data, roles_lists
from db.users import Users
from db.town import City
from views.Town.City import CityRegisterButton

guild_id = guild_data()["roleplay"]
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

    @admin.command(name="ติดตั้งระบบลงทะเบียนเมือง", description="คำสั่งติดตั้งระบบลงทะเบียนเมือง")
    async def town_reg(
            self,
            ctx:discord.Interaction
    ):
        guild = ctx.guild
        await ctx.defer(ephemeral=True, invisible=False)
        msg = await ctx.followup.send("โปรดรอสักครู่ระบบกำลังติดตั้งปุ่มลงทะเบียนเมืองให้กับคุณ")
        try:
            cate_name = "COMMUNITY CITY"
            channel_name = "📝-จดทะเบียนประชากร"
            overwrites={
                guild.default_role:discord.PermissionOverwrite(
                    send_messages=False,
                    view_channel=True
                )
            }
            cate = discord.utils.get(guild.categories, name=cate_name)
            if cate:
                channel = discord.utils.get(guild.channels, name=channel_name)
                if channel:
                    await channel.purge()
                    pass
            else:
                cate = await guild.create_category(name=cate_name, overwrites=overwrites)
                channel = await guild.create_text_channel(name=channel_name, category=cate)

        except Exception as e:
            return await msg.edit(content=e)
        else:
            embed = discord.Embed(
                title="📝 ระบบจดทะเบียนพลเมือง",
                description="ผู้เล่นต้องเลือกเข้าเป็นพลเมืองของ 1 ใน 4 เมือง ซึ่งได้แก่\n"
                            "- City A คือเมือง Alexandria\n"
                            "- City B คือเมือง Kingdom\n"
                            "- City C คือเมือง Savior\n"
                            "- City D คือเมือง Commonwealth"
            )
            embed.set_image(url=img_("bran_reg"))
            await channel.send(embed=embed, view=CityRegisterButton(self.bot))
            return await msg.edit(content="ติดตั้งระบบเรียบร้อยแล้ว")

    @admin.command(name="town",description="เช็คจำนวนเมือง")
    async def town_count(
            self,
            ctx:discord.Interaction,
            city:Option(str,"ระบุเมืองที่ต้องการเช็ค")
                         ):
        await ctx.defer(ephemeral=True, invisible=False)
        msg = await ctx.followup.send(f"ระบบกำลังตรวจนับจำนวนการลงทะเบียนของเมือง {city}")
        return await msg.edit(content=City().citizen_count(city))

    @admin.command(name="citizen", description="คำสั่งเช็คสถานะการจดทะเบียนผลเมือง")
    async def citizen_reg_check(
            self,
            ctx:discord.Interaction,
            member:Option(discord.Member, "ระบบผุ้ใช้งาน")
    ):
        await ctx.defer(ephemeral=True, invisible=False)
        msg = await ctx.followup.send("โปรดรอสักครู่ระบบกำลังทำงาน")
        try:
            if City().city(member.id) != 0:
                return await msg.edit(content=ctx.user.mention)

        except Exception as e:
            return await msg.edit(content=e)
        else:
            return await msg.edit(content=f"ไม่พบข้อมูลการจดทะเบียนพลเมืองของ {ctx.user.display_name} ในระบบ")



    @admin.command(name="ควบคุมระบบลงทะเบียน", description="คำสั่งเปิดหรือปิดระบบลงทะเบียน")
    async def register_system(self, ctx:discord.Interaction, method:Option(str, 'เลือกคำสั่งที่ต้องการ', choices=["Open", "Close"])):
        try:
            update_sys(method)
        except Exception as e:
            return await ctx.response.send_message(e, ephemeral=True)
        else:
            return await ctx.response.send_message(f"{method} ระบบลงทะเบียนเรียบร้อยแล้ว", ephemeral=True)

def setup(bot):
    bot.add_cog(AdminCommand(bot))