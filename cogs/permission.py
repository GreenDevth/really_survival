import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup, Option

from func.Channels import channels

from func.config import config_

guild_id = config_()["guild"]

class ChannelPermission(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(__class__.__name__, " is ready")


    ch = SlashCommandGroup(guild_ids=[guild_id], name="channel", description="คำสั่งจัดการสิทธิ์ต่าง ๆ ของห้องสนทนาและห้องอื่น ๆ")

    @ch.command(name="จำกัดสิทธิ์", description="คำสั่งจำกัดสิทธิ์การใช้งานห้อง")
    async def channel_disabled(self, ctx:discord.Interaction, channel:Option(str, "เลือกห้องที่ต้องการ", choices=channels), method:Option(str, "เลือกรูปแบบ", default=None)):
        guild = ctx.guild
        await ctx.response.defer(ephemeral=True, invisible=False)
        msg = await ctx.followup.send("โปรดรอสักครู่ระบบกำลังประมวลผลการทำงาน")

        channel = discord.utils.get(ctx.guild.channels, name=channel)
        if channel:
            if method == "view":
                await channel.set_permissions(guild.default_role, view_channel=False)
            elif method == "read":
                await channel.set_permissions(guild.default_role,view_channel=True, send_messages=False)
            elif method == "all":
                await channel.set_permissions(
                    guild.default_role,
                    read_messages=False,
                    view_channel=False,
                    send_messages=False,
                    manage_messages=False,
                    embed_links=False,
                    attach_files=False,
                    read_message_history=False)


        return await msg.edit(content=f"เพิ่มสิทธิ์ {method} ให้กับ {channel} เรียบร้อย")










    @ch.command(name="เพิ่มสิทธิ์", description="คำสั่งเพิ่มสิทธิ์การใช้งานห้อง")
    async def channel_enabled(self, ctx:discord.Interaction, channel:Option(str, "เลือกห้องที่ต้องการ", choices=channels), method:Option(str, "เลือกรูปแบบ", default=None)):
        guild = ctx.guild
        await ctx.response.defer(ephemeral=True, invisible=False)
        msg = await ctx.followup.send("โปรดรอสักครู่ระบบกำลังประมวลผลการทำงาน")

        channel = discord.utils.get(ctx.guild.channels, name=channel)
        if channel:
            if method == "view":
                await channel.set_permissions(guild.default_role, view_channel=True)
            elif method == "read":
                await channel.set_permissions(guild.default_role, read_messages=True,
                                                     read_message_history=True)
            elif method == "all":
                await channel.set_permissions(
                    guild.default_role,
                    read_messages=True,
                    view_channel=True,
                    send_messages=True,
                    manage_messages=True,
                    embed_links=True,
                    attach_files=True,
                    read_message_history=True)


        return await msg.edit(content=f"เพิ่มสิทธิ์ {method} ให้กับ {channel} เรียบร้อย")

def setup(bot):
    bot.add_cog(ChannelPermission(bot))