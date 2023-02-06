import asyncio

import discord
from discord.commands import SlashCommandGroup
from discord.ext import commands
from discord.utils import get

from scripts.guilds import guild_data

guild_id = guild_data()["realistic"]

class ServerAnnounce(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    announce = SlashCommandGroup(guild_ids=[guild_id], name="announce", description="คำสั่งจัดการประกาศของทางเซิร์ฟเวอร์")

    @announce.command(name="เขียนประกาศข่าวสารจากเซิร์ฟเวอร์", description="คำสั่งเพื่อใช้เขียนประกาศข่าวสารต่าง ๆ จากเซิร์ฟเวอร์")
    async def announce_write(self, ctx:discord.Interaction):
        guild = ctx.guild
        ch_name = "📰-ข่าวสารจากเซิร์ฟ"
        channel = get(guild.channels, name=ch_name)
        await ctx.response.defer(ephemeral=True, invisible=False)
        def check(res):
            return res.author == ctx.user and res.channel == ctx.channel

        msg = await ctx.followup.send(f'📝 พิมพ์ข้อความที่ต้องการประกาศ')

        try:
            message = await self.bot.wait_for(event="message", check=check, timeout=300)
            if channel:
                await message.delete()
                await msg.edit(content=f"ส่งข้อความประกาศไปยังห้อง {channel.mention} เป็นที่เรียบร้อยแล้ว")
                return await channel.send(message.content)
        except asyncio.TimeoutError:
            await msg.edit(content=f"{ctx.user.mention} : คุณใช้เวลาในการพิมพ์นานเกินกว่าที่ระบบกำหนด")
            await asyncio.sleep(5)
            return await msg.delete()




def setup(bot):
    bot.add_cog(ServerAnnounce(bot))