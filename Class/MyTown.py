import discord
from discord.ext import commands
from discord.utils import get

from db.town import City
from func.config import img_


class MyTownCommand(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command(name="town")
    async def i_town(self, ctx):
        member = ctx.author
        await ctx.message.delete()
        guild = ctx.guild
        room_name = "📝-ผู้ใช้งาน-id-{}".format(member.discriminator)

        if City().city(member.id) == 0:
            return await ctx.send(f"{member.mention} คุณยังไม่ได้จดทะเบียนพลเมือง", delete_after=5)
        else:
            try:
                channel = get(guild.channels, name=room_name)
                my_city = City().citizen(member.id)[1]
                if ctx.channel == channel and member == ctx.author:
                    people = City().discord_id(my_city)

                    for p in people:
                        user = await self.bot.fetch_user(p)
                        if user:
                            embed = discord.Embed(title=f"พลเมืองของ {my_city}")
                            embed.add_field(name="NAME", value=user.display_name)
                            embed.add_field(name="DISCORD", value=user.mention)
                            embed.set_thumbnail(url="{}".format(user.display_avatar))
                            embed.set_image(url=img_(my_city))
                            if City().citizen(user.id)[3] == 1:
                                embed.set_footer(text="หัวหน้าหมู่บ้าน")
                            else:
                                embed.set_footer(text="ลูกบ้าน")
                            await channel.send(embed=embed)

                    return

            except Exception as e:
                return await ctx.send(e, delete_after=5)
            else:
                return await ctx.send(f"กรุณาพิมพ์คำสั่งของคุณที่ห้อง {channel.mention} เท่านั้น", delete_after=5)


    @commands.command(name="leader")
    async def i_boss(self, ctx):
        member = ctx.author
        await ctx.message.delete()
        guild = ctx.guild
        room_name = "📝-ผู้ใช้งาน-id-{}".format(member.discriminator)

        if City().city(member.id) == 0:
            return await ctx.send(f"{member.mention} คุณยังไม่ได้จดทะเบียนพลเมือง", delete_after=5)

        try:
            channel = get(guild.channels, name=room_name)
            my_city = City().citizen(member.id)[1]
            if ctx.channel == channel and member == ctx.author:
                if City().get_boss(my_city)[1] == 1:
                    boss = City().get_boss(my_city)[0]
                    my_boss = await self.bot.fetch_user(boss)
                    if my_boss:
                        embed = discord.Embed(title=f"หัวหน้าหมู่บ้านของเมือง {my_city}")
                        embed.add_field(name="NAME", value=my_boss.display_name)
                        embed.add_field(name="DISCORD", value=my_boss.mention)
                        embed.set_thumbnail(url="{}".format(my_boss.display_avatar))
                        embed.set_image(url=img_(my_city))
                        return await channel.send(embed=embed)
                else:
                    return await ctx.send(f"{member.mention} เมือง {my_city} ยังไม่มีเจ้าเมือง พิมพ์ !boss ตามตัว ชื่อ discord ผู้ใช้งาน เพื่อเลือกหัวหน้าหมู่บ้านของคุณ", delete_after=5)
        except Exception as e:
            return await ctx.send(e, delete_after=5)

        else:
            return await ctx.send(f"กรุณาพิมพ์คำสั่งของคุณที่ห้อง {channel.mention} เท่านั้น", delete_after=5)
