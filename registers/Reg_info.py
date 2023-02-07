import discord
from discord.ext import commands

from db.users import Users
from views.System.Register import RegisterButton


def count_access():
    amount = Users().user_count()
    total  = (30 - int(amount))
    return total


class Register_Access(discord.ui.View):
    def __init__(self, bot):
        super(Register_Access, self).__init__(timeout=None)
        self.bot = bot
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 30, commands.BucketType.member)
    @discord.ui.button(label="สมัครสมาชิก", style=discord.ButtonStyle.secondary, emoji="📝", custom_id='reg_access')
    async def reg_access(self, button, interaction: discord.Interaction):
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f'กรุณารออีก {round(retry,30)} วินาที คำสั่งถึงจะพร้อมใช้งานอีกครั้ง', ephmeral=True
            )
        if count_access() == 0:
            return await interaction.response.edit_message(content=f"{interaction.user.mention} ตอนนี้ มีผู้ลงทะเบียนขอสิทธิ์ใช้งานเซิร์ฟเวอร์ เต็มแล้ว",view=None,embed=None)

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
