import discord
from discord.utils import get
from discord.ext import commands
from discord.commands import SlashCommandGroup, Option

from db.users import Supporter
from scripts.guilds import guild_data


guild_id = guild_data()["realistic"]


class VerifyPlayerCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(VerifyButton(self.bot))

    verify = SlashCommandGroup(guild_ids=[guild_id], name="verify", description="คำสั่งรันระบบตรวจสอบผู้เล่น")

    @verify.command(name="เปิดใช้งานระบบตรวจสอบผู้เล่น", description="คำสั่งเปิดระบบตรวจสอบผู้เล่น หรือการ verify ผู้เล่น")
    async def verify_commands(self, ctx:discord.Interaction, method:Option(str,"เลือกคำสั่งที่ต้องการ", choices=["True", "False"])):
        member = ctx.user
        await ctx.response.defer(ephemeral=True, invisible=False)

        if method == "True":
            try:
                #ตรวจสอบว่าเป็นผู้เล่น ที่สมทบทุนหรือไม่
                if Supporter().check(member.id) == 1:
                    # show verify button for player
                    return await ctx.followup.send("คุณได้รับสิทธิ์ Exclusive Member แล้วขณะนี้")
                else:
                    pass
            except Exception as e:
                return await ctx.followup.send(e)
            else:
                return await ctx.followup.send("คุณยังไม่ได้รับสิทธิ์เป็น Exclusive Member", view=VerifyButton(self.bot))


class VerifyButton(discord.ui.View):
    def __init__(self, bot):
        super(VerifyButton, self).__init__(timeout=None)
        self.bot = bot

    @discord.ui.button(label="Exclusive Verify", style=discord.ButtonStyle.secondary, emoji="🔓", custom_id="verify_players")
    async def verify_player_button(self, button, interaction:discord.Interaction):
        button.disabled=False
        await interaction.response.defer(ephemeral=True, invisible=False)

        try:
            total = Supporter().count()
        except Exception as e:
            print(e)
        else:
            await interaction.followup.send(total)