import discord

from func.config import img_

town_list = ["Alexandria","Kingdom","Savior","Commonwealth"]

def city_embed():
    embed = discord.Embed(
        title="📝 ระบบจดทะเบียนพลเมือง",
        description="ผู้เล่นต้องเลือกเข้าเป็นพลเมืองของ 1 ใน 5 เมือง ซึ่งได้แก่\n"
                    "- A คือเมือง Alexandria\n"
                    "- B คือเมือง Kingdom\n"
                    "- C คือเมือง Savior\n"
                    "- D คือเมือง Commonwealth\n"
                    "- E คือเมือง Hilltop"
    )
    embed.set_image(url=img_("bran_reg"))
    return embed


city_list = [
    "Alexandria",
    "Kingdom",
    "Savior",
    "Commonwealth",
    "Hilltop"
]