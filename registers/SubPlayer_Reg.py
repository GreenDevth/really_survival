import asyncio

import discord
from discord.ext import commands

from db.users import Users
from views.System.Register import RegisterButton


def count_access():
    amount = Users().user_count()
    total  = (52 - int(amount))
    return total


class SubPlayer_Register_Access(discord.ui.View):
    def __init__(self, bot):
        super(SubPlayer_Register_Access, self).__init__(timeout=None)
        self.bot = bot
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 30, commands.BucketType.member)
    @discord.ui.button(label="สมัครสมาชิก SubPlayer", style=discord.ButtonStyle.secondary, emoji="📝", custom_id='reg_access')
    async def reg_access(self, button, interaction: discord.Interaction):
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f'กรุณารออีก {round(retry,30)} วินาที คำสั่งถึงจะพร้อมใช้งานอีกครั้ง', ephmeral=True
            )
        if Users().check(interaction.user.id) == 1:
            await interaction.response.send_message(f"{interaction.user.mention} คุณเป็นผู้เข้าร่วมโปรเจคนี้อยู่แล้ว", ephemeral=True)
        if count_access() == 0:
            return await interaction.response.send_message(f"{interaction.user.mention} ตอนนี้ มีผู้ลงทะเบียนขอสิทธิ์ใช้งานเซิร์ฟเวอร์ เต็มแล้ว",ephemeral=True)

        button.disabled = False
        member = interaction.user
        guild = interaction.guild
        cat_name = "USER PROFILES"
        room_name = "📝-ผู้ใช้งาน-id-{}".format(member.discriminator)
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(
                view_channel=False,
                read_messages=False
            )
        }
        try:
            category = discord.utils.get(guild.categories, name=cat_name)
            if category:
                pass
            else:
                await guild.create_category(name=cat_name, overwrites=overwrites)
        except Exception as e:
            return await interaction.response.edit_message(content=e, view=None)
        else:
            try:
                cate = discord.utils.get(guild.categories, name=cat_name)
                if cate:
                    channel = discord.utils.get(guild.channels, name=room_name)
                    if channel:
                        await channel.delete()
            except Exception as e:
                return await interaction.response.edit_message(content=e, view=None)
            else:
                overwrites = {
                    guild.default_role:discord.PermissionOverwrite(
                      view_channel=True
                    ),
                    member: discord.PermissionOverwrite(
                        view_channel=True,
                        read_messages=True,
                        send_messages=True,
                        read_message_history=True
                    )
                }
                register_channel = await guild.create_text_channel(name=room_name, category=cate, overwrites=overwrites)
                await register_channel.edit(sync_permissions=True,)
                await register_channel.set_permissions(member, view_channel=True, send_messages=True, read_message_history=True, read_messages=True)
                await interaction.response.edit_message(content=f"ไปยังห้อง {register_channel.mention} เพื่อเข้าสู่ระบบลงทะเบียน", view=None, embed=None)
                return await register_channel.send(file=discord.File('./img/concept/steam.png'), view=RegisterButton(self.bot))

    @discord.ui.button(label="ยกเลิก หรือ ออกจากเซิร์ฟ", style=discord.ButtonStyle.secondary, emoji="⚠", custom_id="cancle_to_reg")
    async def cancle_to_reg(self, button, interaction:discord.Interaction):
        button.disabled=False
        await interaction.response.edit_message(content="คุณต้องการออกจากเซิร์ฟเวอร์หรือไม่", view=LeaveServer(), embed=None)

class LeaveServer(discord.ui.View):
    def __init__(self):
        super(LeaveServer, self).__init__(timeout=None)

    @discord.ui.button(label="Yes", style=discord.ButtonStyle.danger, emoji="❕", custom_id="player_leave")
    async def player_leave(self, button, interaction:discord.Interaction):
        guild = interaction.guild
        button.disabled=False
        await interaction.response.edit_message(f"{interaction.user.mention} อีก 10 วินาที ระบบจะทำการนำคุณออกจากเซิร์ฟเวอร์ของเรา ขอบคุณสำหรับการเข้ามา")
        await asyncio.sleep(10)
        await guild.kick(interaction.user)
    @discord.ui.button(label="No", style=discord.ButtonStyle.secondary, emoji="🚫", custom_id="player_leave_cancle")
    async def player_leave_cancle(self, button, interaction:discord.Interaction):
        button.disabled=False
        await interaction.response.edit_message(content=f"{interaction.user.mention} ยกเลิกระบบลงทะเบียนเรียบร้อย", view=None)
