import discord

from func.config import img_


def city_embed():
    embed = discord.Embed(
        title="📝 ระบบจดทะเบียนพลเมือง",
        description="ผู้เล่นต้องเลือกเข้าเป็นพลเมืองของ 1 ใน 4 เมือง ซึ่งได้แก่\n"
                    "- Town A คือเมือง Alexandria\n"
                    "- Town B คือเมือง Kingdom\n"
                    "- Town C คือเมือง Savior\n"
                    "- Town D คือเมือง Commonwealth"
    )
    embed.set_image(url=img_("bran_reg"))
    return embed