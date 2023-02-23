import discord

from db.users import Users


def user_data(discord_id):
    data = Users().player(discord_id)

    return data

def user_info(member):
    data = user_data(member.id)
    verifies = data[6]
    embed = discord.Embed(
        title=f"📝 ข้อมูลของ {member.display_name}",
        color= discord.Colour.from_rgb(21, 182, 13) if verifies == 1 else discord.Colour.from_rgb(245, 127, 16)
    )
    embed.add_field(name="ชื่อผู้ใช้งาน", value=member.mention)
    embed.add_field(name="กระเป๋าตังค์", value="${:,d}".format(data[3]))
    embed.add_field(name="รหัสผู้ใช้งาน", value="#{}".format(member.discriminator))
    embed.add_field(name="เลขสตรีม", value="{}...".format(data[2][:10]))
    embed.add_field(name="ประชากรของ", value= "ยังไม่เข้าร่วมกลุ่ม" if data[4] is None else data[4])
    embed.add_field(name="สิทธิ์ใช้งานเซิร์ฟ", value="🟢 อนุมัติ" if data[6] == 1 else "🟠 รออนุมัติ")
    embed.set_thumbnail(url=member.display_avatar)

    return embed
