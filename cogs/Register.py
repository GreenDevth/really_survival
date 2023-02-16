import discord.ui
from discord.ext import commands

from db.users import Users
from func.config import get_cooldown_time, database_check, battle_info, server_status, get_system, get_server_info, \
    reg_amount
from registers.Reg_info import Register_Access
from server.information import server_info, reg_info
from views.System.Register import RegisterButton, CloseRegisterButton


class Register(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(RegisterVeiw(self.bot))
        self.bot.add_view(RegisterButton(self.bot))
        self.bot.add_view(CloseRegisterButton(self.bot, steam_id=None))

    @commands.command(name="register_setup")
    @commands.is_owner()
    async def reg_setup(self, ctx):
        try:
            await ctx.message.delete()
            await ctx.channel.purge()
        except Exception as e:
            return await ctx.send(e, delete_after=1)
        else:
            img = discord.File('./img/concept/info.png')

            return await ctx.send(file=img, view=RegisterVeiw(self.bot))


def setup(bot):
    bot.add_cog(Register(bot))

def get_reg_access(x):
    return x

class RegisterVeiw(discord.ui.View):
    def __init__(self, bot):
        super(RegisterVeiw, self).__init__(timeout=None)
        self.bot = bot
        self.cooldown = commands.CooldownMapping.from_cooldown(1, int(get_cooldown_time()), commands.BucketType.member)

    @discord.ui.button(label='ขอสิทธิ์ใช้งาน', style=discord.ButtonStyle.secondary, emoji="📝", custom_id="requrest")
    async def request(self, button, interaction: discord.Interaction):
        button.disabled = False
        member = interaction.user
        guild = interaction.guild
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()

        def user_check():
            total = Users().user_count()
            if total > int(reg_amount()):
                return True
            elif total < int(reg_amount()):
                return False

        if retry:
            return await interaction.response.send_message(
                f'อีก {round(retry, int(get_cooldown_time()))} วินาที คำสั่งถึงจะพร้อมใช้งานอีกครั้ง', ephemeral=True)


        if get_system() == "Close":
            return await interaction.response.send_message(
                f"{interaction.user.mention} ยังไม่เปิดให้ลงทะเบียน", ephemeral=True)

        if user_check():
            return await interaction.response.send_message(f"⚠ {interaction.user.mention} ขออภัยขณะนี้สิทธิ์ในการใช้งานเซิร์ฟเวอร์ครบจำนวน {Users().user_count()} แล้ว", ephemeral=True)

        if Users().check(interaction.user.id) != 0:
            room_name = "📝-ผู้ใช้งาน-id-{}".format(member.discriminator)
            try:
                channel = discord.utils.get(guild.channels,name=room_name)
                if channel:
                    return await interaction.response.send_message(f"⚠ {interaction.user.mention} คุณได้สมัครเข้าร่วมโปรเจค The Walking Dead เป็นที่เรียบร้อยแล้ว {channel.mention}", ephemeral=True)
                else:
                    channel = await guild.create_text_channel(name=room_name)
                    await channel.set_permissions(guild.default_role, view_channel=False)
                    await channel.set_permissions(member, view_channel=True, send_messages=True)
                    return await interaction.response.send_message(f"{member.mention} ไปยังห้องของคุณได้ที่ {channel.mention}", ephemeral=True)
            except Exception as e:
                return await interaction.response.send_message(e)
        else:

            await interaction.response.defer(ephemeral=True, invisible=False)
            try:
                if database_check(r'./db/users.db'):
                    pass
                else:
                    Users().create_table()
                    print("database has been created.")
            except Exception as e:
                print(e)
            else:
                return await interaction.followup.send(embed=reg_info(),view=Register_Access(self.bot))

    @discord.ui.button(label='ข้อมูลเซิร์ฟ', style=discord.ButtonStyle.secondary, emoji="📖",
                       custom_id="setting")
    async def setting(self, button, interaction: discord.Interaction):
        button.disabled = False
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f'อีก {round(retry, int(get_cooldown_time()))} วินาที คำสั่งถึงจะพร้อมใช้งานอีกครั้ง', ephemeral=True)

        if get_server_info() == "Close":
            return await interaction.response.send_message(
                f"{interaction.user.mention} เซิร์ฟเวอร์อยู่ระหว่างพัฒนาระบบ", ephemeral=True)


        await interaction.response.defer(ephemeral=True, invisible=False)
        await interaction.followup.send(server_info())

    @discord.ui.button(label='สถานะเซิร์ฟ', style=discord.ButtonStyle.secondary, emoji="🌐",
                       custom_id="server")
    async def server(self, button, interaction: discord.Interaction):
        button.disabled = False
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f'อีก {round(retry, int(get_cooldown_time()))} วินาที คำสั่งถึงจะพร้อมใช้งานอีกครั้ง', ephemeral=True)

        if get_server_info() == "Close":
            return await interaction.response.send_message(
                f"{interaction.user.mention} เซิร์ฟเวอร์ยังไม่พร้อมให้บริการ", ephemeral=True)

        try:
            await interaction.response.defer(ephemeral=True, invisible=False)
            jsonObj = battle_info()
            if jsonObj:
                pass
        except Exception as e:
            return await interaction.followup.send(e)
        else:
            return await interaction.followup.send(server_status())
