import random

import discord
from discord.ext import commands

from db.Gacha import Gacha
from db.Steam import Steam
from db.users import Users
from func.config import img_

class SaveRickCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(self.__class__.__name__)
        self.bot.add_view(SaveRickButton())


    @commands.command(name="save_rick")
    @commands.is_owner()
    async def save_rick_command(self,ctx):
        await ctx.message.delete()
        guild = ctx.guild
        cate_name = "EVENT REGISTER"
        ch_name = "🦺-ช่วยเหลือริกส์"
        embed = discord.Embed(
            title="🦺 ช่วยเหลือริกส์",
            description="เมื่อริกส์ต้องติดอยู่ในวงล้อมของซอมบี้ เขากำลังตกอยู่ในสถานการณ์ที่ย่ำแย่"
                        "ปาฏิหาริย์เดียวที่มี คือผองเพื่อนที่กำลังค้นหาตัวเขา\n\n"
                        "เกรนและกลุ่มของเขาจะตามหาและช่วยเหลือริกส์ได้ทันหรือไม่ และกระเป๋าของริกส์คนกลุ่มไหนที่ได้มันไป"
        )
        embed.add_field(name="กติกา",
                        value="```yaml\n"
                              "+ ให้ผู้เล่นสุ่มจับฉลากด้วยระบบเพื่อแบ่งเป็น 4 ทีม\n"
                              "+ ส่งตัวแทนของทีม 1 คน เพื่อเป็นเป้าหมายในการช่วยเหลือ\n"
                              "+ ห้ามนำอาวุธทุกชนิดติดตัวมาในวันจัดอีเว้นโดยเด็ดขาด\n"
                              "+ การแต่งกายให้ใช้เสื้อผ้าธรรมดา สไตล์ชาวบ้านทั่วไป\n"
                              "+ อาวุธจะมีมอบให้แต่ละกลุ่มในวันจัดอีเว้น (ไม่ต้องคาดหวัง)"
                              "\n```",
                        inline=False)
        embed.set_image(url=img_("second_event"))

        try:
            categories = discord.utils.get(guild.categories, name=cate_name)
            if categories:
                channel = discord.utils.get(guild.channels, name=ch_name)
                if channel:
                    await channel.purge()
                    await channel.send(embed=embed, view=SaveRickButton())
                    return await ctx.send(f"ติดตั้งอีเว้น {channel.mention} เรียบร้อย", delete_after=5)
                else:
                    channel = await guild.create_text_channel(name=ch_name, category=categories)
                    await channel.edit(sync_permissions=True)
                    await channel.send(embed=embed, view=SaveRickButton())
                    return await ctx.send(f"ติดตั้งอีเว้น {channel.mention} เรียบร้อย", delete_after=5)
            else:
                raise Exception(f"คุณยังไม่ได้สร้าง ห้อง {cate_name} ให้กับเซิร์ฟเวอร์")
        except Exception as e:
            return await ctx.send(e, delete_after=10)

class SaveRickButton(discord.ui.View):
    def __init__(self):
        super(SaveRickButton, self).__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, int(5), commands.BucketType.member)

    @discord.ui.button(label="คลิกที่ปุ่ม 🎲 เพื่อจับฉลากทีมสำหรับกิจกรรม", style=discord.ButtonStyle.secondary, disabled=True, custom_id="disabled_save_rick")
    async def disable_save_rick(self, button, interaction:discord.Interaction):
        await interaction.response.send_message(button.label, ephemeral=True)
    @discord.ui.button(label="จับฉลากทีม", style=discord.ButtonStyle.secondary, emoji="🎲", custom_id="save_rick")
    async def save_rick(self, button, interaction:discord.Interaction):
        button.disabled=False
        member = interaction.user

        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        # if retry:
        #     return await interaction.response.send_message(
        #         f'อีก {round(retry, int(5))} วินาที คำสั่งถึงจะพร้อมใช้งานอีกครั้ง', ephemeral=True)
        await interaction.response.defer(ephemeral=True, invisible=False)
        msg = await interaction.followup.send("ระบบกำลังสุ่มจับฉลากให้กับคุณ")
        try:
            if Gacha().member_check(member.id) == 1:
                data = Gacha().get(member.id)
                pass
                # return await interaction.response.send_message(f"{member.mention} คุณได้จับฉลากไว้แล้ว คุณได้หมายเลข {data[3]}", ephemeral=True)
            else:
                pass
        except Exception as e:
            return await msg.edit(content=e)
        else:
            while True:
                try:
                    result = random.randint(1, 4)
                    print(result)
                    steam_id = Steam().get(member.id)
                    res_1 = Gacha().count_1()
                    res_2 = Gacha().count_2()
                    res_3 = Gacha().count_3()
                    res_4 = Gacha().count_4()

                    if result == 1 and res_1 != 10:
                        Gacha().new(member.id, steam_id, 1)
                        return await msg.edit(content=result)
                    elif result == 2 and res_2 != 10:
                        Gacha().new(member.id, steam_id, 2)
                        return await msg.edit(content=result)
                    elif result == 3 and res_3 != 10:
                        Gacha().new(member.id, steam_id, 3)
                        return await msg.edit(content=result)
                    elif result == 4 and res_4 != 10:
                        Gacha().new(member.id, steam_id, 4)
                        return await msg.edit(content=result)
                    else:
                        result = random.randint(1, 4)

                except Exception as e:
                    return await msg.edit(content=e)
