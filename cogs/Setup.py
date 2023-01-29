import discord
from discord.commands import SlashCommandGroup, Option
from discord.ext import commands

from func.city import town_list
from scripts.guilds import guild_data
from func.Channels import categories,channels

guild_id = guild_data()["realistic"]

role_list = ["Alexandria","Kingdom","Savior","Commonwealth"]
class SystemInstaller(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    setup = SlashCommandGroup(guild_ids=[guild_id], name="setup", description="คำสั่งติดตั้งสำหรับแอดมิน")
    uninstaller = SlashCommandGroup(guild_ids=[guild_id], name="uninstaller", description="คำสั่งถอนการติดตั้งสำหรับแอดมิน")

    @uninstaller.command(name="ลบห้องสนทนา", description="คำสั่งลบห้องสนทนา และห้องอื่น ๆ ภายใน Categories ที่ต้องการ")
    async def uninstall_channel_from_category(self, ctx:discord.Interaction, category:Option(str, "เลือก Category ที่ต้องลบ", choices=categories)):
        await ctx.response.defer(ephemeral=True, invisible=False)
        msg = await ctx.followup.send("กรุณารอสักครู่ระบบกำลังประมวลผล")
        guild = ctx.guild
        try:
            cate_name = category
            category = discord.utils.get(guild.categories, name=cate_name)
            if category:
                for channel in category.channels:
                    await channel.delete()
        except Exception as e:
            return await msg.edit(content=e)
        else:
            await msg.edit(content=f"ทำการลบห้องภายใน {category} เป็นที่เรียบร้อย")

    @setup.command(name="ติดตั้งสิทธิ์การใช้งานดิสคอร์ด", description="คำสั่งติดตั้งระบบ Roles")
    async def role_installer(
            self,
            ctx:discord.Interaction,

    ):
        await ctx.response.defer(ephemeral=True, invisible=False)
        msg = await ctx.followup.send("โปรดรอสักครู่ระบบกำลังประมวลผลการทำงานให้กับคุณ")
        guild = ctx.guild
        def get_color(r):
            if r == role_list[0]:
                colour = discord.Colour.from_rgb(52, 152, 219)
                return colour
            if r == role_list[1]:
                colour = discord.Colour.from_rgb(243, 156, 18)
                return colour
            if r == role_list[2]:
                colour = discord.Colour.from_rgb(231, 76, 60)
                return colour
            if r == role_list[3]:
                colour = discord.Colour.from_rgb(125, 60, 152)
                return colour
        for x in role_list:
            role = discord.utils.get(guild.roles, name=x)
            if role in guild.roles:
                pass
            else:
                role = await guild.create_role(name=x, colour=get_color(x))
                if role in guild.roles:
                    perm = discord.Permissions()
                    perm.update(use_slash_commands=True)
                    await role.edit(hoist=True, permissions=perm)
        await msg.edit(content="ติดตั้ง Role สำหรับ เมือง ทั้ง 4 เมืองให้กับระบบเรียบร้อย")

    @uninstaller.command(name="ถอนการติดตั้งระบบสิทธิ์การใช้งาน", description="คำสั่งถอนการติดตั้งระบบ Roles")
    async def uninstaller_roles(self, ctx:discord.Interaction):
        guild = ctx.guild
        await ctx.response.defer(ephemeral=True, invisible=False)
        msg = await ctx.followup.send("โปรดรอสักครู่ระบบกำลังประมวลผลการทำงานให้กับคุณ")

        for r in role_list:
            role = discord.utils.get(guild.roles, name=r)
            if role in guild.roles:
                await role.delete()

        await msg.edit(content="ถอนระบบสิทธิ์การใช้งานดิสคอร์ดของ กลุ่มเมืองเรียบร้อย")

    @setup.command(name="ติดตั้งห้องพูดคุย", description="คำสั่งติดตั้ง Voice Channel สำหรับ กลุ่มเมืองต่าง ๆ")
    async def voice_channel_installer(
            self,
            ctx:discord.Interaction,
            method:Option(str, "เลือกรูปแบบที่ต้องการ", choices=["True", "False"])
    ):
        await ctx.response.defer(ephemeral=True, invisible=False)
        choices = ["True", "False"]
        guild = ctx.guild
        overwrites={
            guild.default_role:discord.PermissionOverwrite(
                connect=False
            )
        }
        try:
            cate_name = "COMMUNITY TOWN"
            cate = discord.utils.get(guild.categories, name=cate_name)
            if cate:
                pass
            else:
                cate = await guild.create_category(name=cate_name, overwrites=overwrites)
        except Exception as e:
            return await ctx.followup.send(e, ephemeral=True)
        else:

            if method == choices[0]:
                for ch in town_list:
                    channel = discord.utils.get(guild.channels, name=ch)
                    if channel:
                        pass
                    else:
                        await guild.create_voice_channel(name=ch, category=cate)
                        for channel in cate.channels:
                            if channel.name == town_list[0]:
                                role = discord.utils.get(guild.roles, name=role_list[0])
                                await channel.set_permissions(
                                    role,
                                    overwrite=discord.PermissionOverwrite(
                                        connect=True,
                                        view_channel=True,
                                        stream=True,
                                        speak=True,
                                        change_nickname=True
                                    )
                                )
                            if channel.name == town_list[1]:
                                role = discord.utils.get(guild.roles, name=role_list[1])
                                await channel.set_permissions(
                                    role,
                                    overwrite=discord.PermissionOverwrite(
                                        connect=True,
                                        view_channel=True,
                                        stream=True,
                                        speak=True,
                                        change_nickname=True
                                    )
                                )
                                if channel.name == town_list[2]:
                                    role = discord.utils.get(guild.roles, name=role_list[2])
                                    await channel.set_permissions(
                                        role,
                                        overwrite=discord.PermissionOverwrite(
                                            connect=True,
                                            view_channel=True,
                                            stream=True,
                                            speak=True,
                                            change_nickname=True
                                        )
                                    )
                                    if channel.name == town_list[3]:
                                        role = discord.utils.get(guild.roles, name=role_list[3])
                                        await channel.set_permissions(
                                            role,
                                            overwrite=discord.PermissionOverwrite(
                                                connect=True,
                                                view_channel=True,
                                                stream=True,
                                                speak=True,
                                                change_nickname=True
                                            )
                                        )

                return await ctx.followup.send("จัดการสร้างห้องและปรับสิทธิ์ของห้องเรียบร้อยแล้ว")
            else:
                if cate:
                    for channel in cate.channels:
                        await channel.delete()
                return await ctx.followup.send("จัดการลบห้องและปรับสิทธิ์ของห้องเรียบร้อยแล้ว", ephemeral=True)

    @setup.command(name="ติดตั้งห้องทั่วไป", description="คำสั่งติดตั้ง ห้องสนทนา ห้องข้อมูลอื่น ๆ ภายในเซิร์ฟ")
    async def installer_common_channel(
            self,
            ctx:discord.Interaction,
            channel:Option(str, "เลือก Channel ที่ต้องการ", choices=channels, default=None),
    ):
        guild = ctx.guild
        if channel == channels[5]:
            try:
                ch_name = "💬-แชททั่วไป"
                channel = discord.utils.get(guild.channels, name=ch_name)
                if channel:
                    return await ctx.response.send_message(f"พบ {channel.mention} ในระบบอยู่แล้ว", ephemeral=True)
                    pass
                else:
                    overwrites = {
                        guild.default_role:discord.PermissionOverwrite(read_messages=True, view_channel=True,send_messages=True,read_message_history=True)
                    }
                    channel = await guild.create_text_channel(name=ch_name, overwrites=overwrites)
            except Exception as e:
                print(e)
            else:
                await ctx.response.send_message(f"ติดต้้ง {channel.mention} เรียบร้อย", ephemeral=True)
        elif channel == channels[4]:
            try:
                ch_name = "📰-ข่าวสารจากเซิร์ฟ"
                channel = discord.utils.get(guild.channels, name=ch_name)
                if channel:
                    return await ctx.response.send_message(f"พบ {channel.mention} ในระบบอยู่แล้ว", ephemeral=True)
                    pass
                else:
                    overwrites = {
                        guild.default_role: discord.PermissionOverwrite(read_messages=True, view_channel=True,
                                                                        send_messages=True, read_message_history=True)
                    }
                    channel = await guild.create_text_channel(name=ch_name, overwrites=overwrites)
            except Exception as e:
                print(e)
            else:
                await ctx.response.send_message(f"ติดต้้ง {channel.mention} เรียบร้อย", ephemeral=True)

def setup(bot):
    bot.add_cog(SystemInstaller(bot))