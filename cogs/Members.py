import asyncio

import discord
from discord.ext import commands
from discord.utils import get

from db.town import City
from func.city import city_list
from scripts.guilds import guild_data
from views.Members.MemberViews import UsersViews

guild_id = guild_data()["realistic"]

class CityClose(discord.ui.View):
    def __init__(self):
        super(CityClose, self).__init__(timeout=None)
    @discord.ui.button(label="Close", style=discord.ButtonStyle.secondary, custom_id="city_info_close")
    async def city_info_close(self, button, interaction:discord.Interaction):
        button.disabled=False
        await interaction.response.edit_message(content="อีกสักครู่ข้อความนี้จะหายไป", view=None, embed=None)
        await asyncio.sleep(5)
        await interaction.channel.purge(limit=1)

class MemberProfile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(CityClose())

    @commands.command(name="player")
    async def i_player(self, ctx):
        member = ctx.author
        await ctx.message.delete()
        guild = ctx.guild
        room_name = "📝-ผู้ใช้งาน-id-{}".format(member.discriminator)
        try:
            channel = get(guild.channels, name=room_name)
            if ctx.channel == channel and member == ctx.author:
                await channel.purge()
                img = discord.File('./img/member/member_profile.png')
                return await channel.send(file=img, view=UsersViews(self.bot))
        except Exception as e:
            return await ctx.send(e, delete_after=5)
        else:
            return await ctx.send(f"กรุณาพิมพ์คำสั่งของคุณที่ห้อง {channel.mention} เท่านั้น", delete_after=5)

    @commands.command(name="city")
    async def i_city(self, ctx):
        member = ctx.author
        await ctx.message.delete()
        guild = ctx.guild
        room_name = "📝-ผู้ใช้งาน-id-{}".format(member.discriminator)
        try:
            channel = get(guild.channels, name=room_name)
            if ctx.channel == channel and member == ctx.author:
                try:
                    city_1 = City().citizen_count(city_list[0])
                    city_2 = City().citizen_count(city_list[1])
                    city_3 = City().citizen_count(city_list[2])
                    city_4 = City().citizen_count(city_list[3])
                    city_5 = City().citizen_count(city_list[4])

                except Exception as e:
                    print(e)
                else:
                    embed = discord.Embed(
                        title="ข้อมูลเมืองและจำนวนพลเมือง"
                    )
                    embed.add_field(name=city_list[0], value=f"```จำนวนพลเมืองขณะนี้  {city_1}```", inline=False)
                    embed.add_field(name=city_list[1], value=f"```จำนวนพลเมืองขณะนี้  {city_2}```", inline=False)
                    embed.add_field(name=city_list[2], value=f"```จำนวนพลเมืองขณะนี้  {city_3}```", inline=False)
                    embed.add_field(name=city_list[3], value=f"```จำนวนพลเมืองขณะนี้  {city_4}```", inline=False)
                    embed.add_field(name=city_list[4], value=f"```จำนวนพลเมืองขณะนี้  {city_5}```", inline=False)

                    return await ctx.send(embed=embed, view=CityClose())
        except Exception as e:
            return await ctx.send(e, delete_after=5)
        else:
            return await ctx.send(f"กรุณาพิมพ์คำสั่งของคุณที่ห้อง {channel.mention} เท่านั้น", delete_after=5)



    @commands.command(name="event")
    async def i_event(self, ctx):
        member = ctx.author
        await ctx.message.delete()
        guild = ctx.guild
        room_name = "📝-ผู้ใช้งาน-id-{}".format(member.discriminator)

        try:
            channel = get(guild.channels, name=room_name)
            if ctx.channel == channel and member == ctx.author:
                return await ctx.send("ok", delete_after=5)
        except Exception as e:
            return await ctx.send(e, delete_after=5)
        else:
            return await ctx.send(f"กรุณาพิมพ์คำสั่งของคุณที่ห้อง {channel.mention} เท่านั้น", delete_after=5)

def setup(bot):
    bot.add_cog(MemberProfile(bot))