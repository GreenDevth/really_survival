import discord.ui
import requests
from discord.ext import commands

from db.users import Users
from func.config import get_cooldown_time, config_, database_check
from includes.information import server_info, reg_info
from registers.Reg_info import Register_Access
from views.Register import RegisterButton, CloseRegisterButton

auth = config_()["battle_token"]
head = {'Authorization': 'Brarer' + auth}

def battle_info():
    res = requests.get(config_()["server_url"], headers=head)
    return res.json()

class Register(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(RegisterVeiw(self.bot))
        self.bot.add_view(RegisterButton(self.bot))
        self.bot.add_view(CloseRegisterButton(self.bot))

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
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(
                f'อีก {round(retry, int(get_cooldown_time()))} วินาที คำสั่งถึงจะพร้อมใช้งานอีกครั้ง', ephemeral=True)
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

        try:
            await interaction.response.defer(ephemeral=True, invisible=False)
            jsonObj = battle_info()
            if jsonObj:
                pass
        except Exception as e:
            return await interaction.followup.send(e)
        else:
            result = f"```\nServer: {jsonObj['data']['attributes']['name']}" \
                     f"\n======================================" \
                     f"\nIP: {jsonObj['data']['attributes']['ip']}:{jsonObj['data']['attributes']['port']}" \
                     f"\nStatus: {jsonObj['data']['attributes']['status']}" \
                     f"\nTime in Game: {jsonObj['data']['attributes']['details']['time']}" \
                     f"\nPlayers: {jsonObj['data']['attributes']['players']}/{jsonObj['data']['attributes']['maxPlayers']}" \
                     f"\nRanking: #{jsonObj['data']['attributes']['rank']}" \
                     f"\nGame version: {jsonObj['data']['attributes']['details']['version']}\n" \
                     f"\nServer Restarts Every 6 hours" \
                     f"\nDay 3.8 hours, Night 1 hours" \
                     f"\n======================================" \
                     f"\n14Studio, Copyright © 1983 - 2023```"
            return await interaction.followup.send(result.strip())
