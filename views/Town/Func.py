import discord

from db.town import City
from func.config import img_


def id_card(guild,member):
    user = guild.get_member(member)
    city = City().citizen(user.id)
    embed = discord.Embed(
        title=f"บัตรประจำตัวพลเมือง",
        colour=discord.Colour.from_rgb(245, 176, 65)
    )
    embed.set_thumbnail(url=user.display_avatar)
    embed.add_field(name="ชื่อผู้ใช้งาน", value=user.display_name)
    embed.add_field(name="ชื่อตัวละคร", value=city[5])
    embed.add_field(name="ชื่อเมือง", value=city[1])
    embed.add_field(name="สถานะพลเมือง", value="เจ้าเมือง" if city[3] == 1 else "ผู้อาศัย", inline=False)
    embed.set_image(url=img_(city[1]))
    return embed