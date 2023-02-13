import asyncio

import discord
import discord.ui
from discord.ext import commands
from discord.utils import get

from Class.The_Police import ThePoliceGet
from db.town import City
from db.users import Supporter, Users
from func.city import city_list
from scripts.guilds import guild_data
from session.SessionContent import police_event
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
        # self.bot.add_view(Close())

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
                return await ctx.send(embed=police_event(), view=ThePoliceGet())
            else:
                return await ctx.send(f"กรุณาพิมพ์คำสั่งของคุณที่ห้อง {channel.mention} เท่านั้น", delete_after=5)
        except Exception as e:
            return await ctx.send(e, delete_after=5)

    @commands.command(name="boss")
    async def my_boss(self, ctx, member:discord.Member):
        user = ctx.author
        guild = ctx.guild
        await ctx.message.delete()

        try:
            if member in guild.members:
                if City().boss_check() == 1:
                    boss_id = City().boss()[0]
                    my_boss = guild.get_member(int(boss_id))
                    return await ctx.send(f"{my_boss.mention} ได้ถูกแต่งตั้งให้เป็นหัวหน้าหมู่บ้านไว้แล้ว", delete_after=10)
                else:
                    try:
                        City().update_citizen_boss(member.id)
                    except Exception as e:
                        return await ctx.send(e)
                    return await ctx.send(f"{user.mention} คุณได้เลือกให้ {member.mention} เป็นหัวหน้าหมู่บ้านของคุณเรียบร้อยแล้ว")
        except Exception as e:
            await ctx.send(e, delete_after=5)

    @my_boss.error
    async def boss_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.message.delete()
            await ctx.send(f"{ctx.author.mention} :กรุณาพิมพ์ ชื่อดิสคอร์ดของหัวหน้าของเมืองที่ต้องการแต่งตั้ง\n"
                           f"``ตัวอย่าง : @ผู้ดูแลระบบ``", delete_after=10)





    @commands.command(name="slot")
    async def slot_check_command(self, ctx):
        member = ctx.author
        await ctx.message.delete()
        guild = ctx.guild
        room_name = "📝-ผู้ใช้งาน-id-{}".format(member.discriminator)

        channel = get(guild.channels, name=room_name)
        if ctx.channel == channel and member == ctx.author:
            try:
                check = Supporter().count()
                if check == 38:
                    embed = discord.Embed(
                        title="จำนวนผู้เล่นเต็มแล้ว",
                        colour=discord.Colour.from_rgb(242, 20, 9)
                    )
                    embed.set_footer(text="พิมพ์คำสั่ง !player เพื่อรีเซ็ตหน้าโปรไฟล์ของคุณ")
                    return await ctx.send(embed=embed, view=Close())
                else:
                    pass
            except Exception as e:
                print(e)
            else:
                embed = discord.Embed(
                    title="Game Slot Avaliable",
                    description="จำนวนสล๊อตทั้งหมดของเซิร์ฟอยู่ที่ 40 โดยหักลบจำนวน 2 สล๊อตออกเพื่อให้เป็นพื้นที่ของ แอดมินและโดรน ดังนั้น สล๊อตที่สามารถใช้งานได้จริงจึงเหลือเพียง 38 สล๊อต",
                    colour=discord.Colour.from_rgb(12, 131, 73)
                )
                embed.add_field(name="จำนวนคงเหลือ",
                                value=f"```{38-check} Slot```")
                embed.set_footer(text="พิมพ์คำสั่ง !player เพื่อรีเซ็ตหน้าโปรไฟล์ของคุณ")
                return await ctx.send(embed=embed, view=Close())
        else:
            return await ctx.send(f"กรุณาพิมพ์คำสั่งของคุณที่ห้อง {channel.mention} เท่านั้น", delete_after=5)

def setup(bot):
    bot.add_cog(MemberProfile(bot))

class Close(discord.ui.View):
    def __init__(self):
        super(Close, self).__init__(timeout=None)
    @discord.ui.button(label="ปิด", style=discord.ButtonStyle.danger, custom_id="close_window")
    async def close_window(self, button,interaction:discord.Interaction):
        button.disabled=False
        await interaction.channel.purge(limit=1)