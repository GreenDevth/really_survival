import discord
from discord.utils import get
from discord.commands import SlashCommandGroup, Option
from discord.ext import commands

from scripts.guilds import category, channels, guild_data, discord_roles, roles_colour, separate_channles, roles_lists
from views.InfoView import InformationViews
from views.ManualViews import PopulationManualView
from views.Members.MemberViews import UsersViews

guild_id = guild_data()["roleplay"]
categories_list = category()
channels_list = channels()

cate_list = ["info", "chat", "voice", "log", "trader", "guild"]
system_list = ["roles", "category"]
commands_list=["install", "uninstall"]
commands_lists = ["install", "uninstall", "permissions", "update"]
roles_list = discord_roles()
infor_list = separate_channles()["info"]
permissions_roles = roles_lists()

class SystemInstaller(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(InformationViews(self.bot))
        self.bot.add_view(PopulationManualView(self.bot))
        self.bot.add_view(UsersViews(self.bot))

    setup = SlashCommandGroup(guild_ids=[guild_id], name="setup", description="คำสั่งติดตั้งระบบดิสคอร์ด")

    @setup.command(name="ระบบเซิร์ฟเวอร์", description="คำสั่งติดตั้งระบบของดิสคอร์ดเซิร์ฟเวอร์")
    async def installer(
            self,
            ctx: discord.Interaction,
            command:Option(str, "เลือกคำสั่งที่ต้องการ", choices=commands_list),
            system: Option(str, "เลือกระบบที่ต้องการติดตั้ง", choices=system_list)
    ):
        await ctx.response.defer(ephemeral=True, invisible=False)
        guild = ctx.guild
        msg = await ctx.followup.send(f'⏳ โปรดรอสักครู่บอทกำลัง {command.upper()}  {system.upper()}')

        if command == commands_list[0]:
            """Install Commands"""

            if system == system_list[0]:
                for r in roles_list:
                    role = get(guild.roles, name=r)
                    if role in guild.roles:
                        pass
                    else:
                        role = await guild.create_role(name=r, colour=roles_colour(r))
                        try:
                            if role.name == roles_list[12]:
                                exclusive = get(guild.roles, name=roles_list[12])
                                if exclusive:
                                    perm = discord.Permissions()
                                    perm.update(use_slash_commands=True)
                                    await exclusive.edit(permissions=perm)
                                pass
                            else:
                                await role.edit(hoist=True)
                        except Exception as e:
                            return await msg.edit(content=e)
            if system == system_list[1]:
                overwrites = {
                    guild.default_role:discord.PermissionOverwrite(view_channel=False)
                }
                for categories in categories_list:
                    cate = get(guild.categories, name=categories)
                    if cate:
                        pass
                    else:
                        await guild.create_category(name=categories, overwrites=overwrites)
            return await msg.edit(content=f"🎉 {command.upper()} {system.upper()} เรียบร้อย")



        if command == commands_list[1]:
            """Uninstall Commands"""

            if system == system_list[0]:
                for r in roles_list:
                    role = get(guild.roles, name=r)
                    if role in guild.roles:
                        await role.delete()
            if system == system_list[1]:
                for categories in categories_list:
                    cate = get(guild.categories, name=categories)
                    if cate:
                        for channel in cate.channels:
                            await channel.delete()
                        await cate.delete()

            return await msg.edit(content=f"🎉 {command.upper()} {system.upper()} เรียบร้อย")


    @setup.command(name="ระบบแสดงข้อมูลเซิร์ฟ", description="ติดตั้งส่วนของ SERVER INFORMATION")
    async def server_information(
            self,
            ctx:discord.Interaction,
            system: Option(str, "เลือกคำสั่งที่ต้องการ", choices=commands_lists),
            roles: Option(default=None, choices=permissions_roles),
            channel : Option(default=None, choices=infor_list)
    ):

        guild = ctx.guild
        await ctx.response.defer(ephemeral=True, invisible=False)
        msg = await ctx.followup.send(f'⏳ โปรดรอสักครู่บอทกำลัง {system.upper()} {categories_list[0]}')

        if system == commands_lists[3]:
            """Update server information channels"""
            if channel == infor_list[0]:
                try:
                    channel_name = get(guild.channels, name=channel)
                    if channel_name:
                        pass
                except Exception as e:
                    return await msg.edit(content=e)
                else:
                    await channel_name.purge()
                    await channel_name.send(file=discord.File('./img/info/server_banner.png'), view=InformationViews(self.bot))
                return await msg.edit(content=f"🎉 {system} {channel_name.mention} เรียบร้อย")

            if channel == infor_list[3]:
                try:
                    channel_name = get(guild.channels, name=channel)
                    if channel_name:
                        pass
                except Exception as e:
                    return await msg.edit(content=e)
                else:
                    await channel_name.purge()
                    await channel_name.send(file=discord.File('./img/info/law.png'), view=PopulationManualView(self.bot))
                return await msg.edit(content=f"🎉 {system} {channel_name.mention} เรียบร้อย")

        if system == commands_lists[2]:
            """Set Permission for roles and channels"""
            if roles == permissions_roles[0]:
                try:
                    role = get(guild.roles, name=roles)
                    if role:
                        info_channel = get(guild.channels, name=channel)
                        if info_channel:
                            await info_channel.set_permissions(
                                role,
                                overwrite=discord.PermissionOverwrite(
                                    view_channel=True
                                ))
                except Exception as e:
                    return await msg.edit(content=e)
            if roles == permissions_roles[1]:
                try:
                    role = get(guild.roles, name=roles)
                    if role:
                        info_channel = get(guild.channels, name=channel)
                        if info_channel:
                            await info_channel.set_permissions(
                                role,
                                overwrite=discord.PermissionOverwrite(
                                    view_channel=True,
                                    send_messages=False,
                                    read_messages=True,
                                    read_message_history=True
                                ))
                except Exception as e:
                    return await msg.edit(content=e)
            if roles == permissions_roles[2]:
                """Read Only"""
                try:
                    info_channel = get(guild.channels, name=channel)
                    if info_channel:
                        await info_channel.set_permissions(
                            guild.default_role,
                            overwrite=discord.PermissionOverwrite(
                                view_channel=True,
                                send_messages=False,
                                read_messages=True,
                                read_message_history=True
                            ))
                except Exception as e:
                    return await msg.edit(content=e)

            if roles == permissions_roles[16]:
                try:
                    role = get(guild.roles, name=roles)
                    if role:
                        info_channel = get(guild.channels, name=channel)
                        if info_channel:
                            await info_channel.set_permissions(
                                role,
                                overwrite=discord.PermissionOverwrite(
                                    view_channel=True,
                                    send_messages=False,
                                    read_messages=True,
                                    read_message_history=True
                                ))
                except Exception as e:
                    return await msg.edit(content=e)
            return await msg.edit(content=f"🎉 set {roles} and {system} for {channel} เรียบร้อย")
        if system == commands_lists[0]:
            """Install SERVER INFORMATION CATEGORY"""
            try:
                information = get(guild.categories, name=categories_list[0])
                if information:
                    pass
                else:
                    overwrites = {
                        guild.default_role: discord.PermissionOverwrite(view_channel=False)
                    }
                    await guild.create_category(name=categories_list[0], overwrites=overwrites)
                    print('create server information categories successfully...')
            except Exception as e:
                print(e)
            else:
                information = get(guild.categories, name=categories_list[0])
                for x in infor_list:
                    channel = get(guild.channels, name=x)
                    if channel:
                        pass
                    else:
                        await guild.create_text_channel(name=x, category=information)
            return await msg.edit(content=f"🎉 {system.upper()} {categories_list[0]} เรียบร้อย")









def setup(bot):
    bot.add_cog(SystemInstaller(bot))
