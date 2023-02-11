import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup, Option

from db.town import City
from db.users import Users
from func.city import city_list
from scripts.guilds import guild_data

guild_id = guild_data()['realistic']

class ChangeCityCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(__class__.__name__, " is ready")


    player = SlashCommandGroup(guild_ids=[guild_id], name="player", description="คำสั่งย้ายเมืองสำหรับผู้เล่น")

    @player.command(name="ย้ายเมือง", description="คำสั่งย้ายเมืองสำหรับผู้เล่น")
    async def player_change_town(self, ctx:discord.Interaction, town:Option(str, "เลือกมืองที่ต้องการย้ายเข้า", choices=city_list)):
        member = ctx.user
        guild = ctx.guild
        await ctx.response.defer(ephemeral=True, invisible=False)

        msg = await ctx.followup.send("โปรดรอสักครู่ระบบกำลังประมวลผล")

        if Users().player(member.id)[4] is None:
            return await msg.edit(content="คุณยังไม่ได้ลงทะเบียนประชากร")

        try:
            data = City().citizen(member.id)
            user = Users().player(member.id)
            player_town = data[1]
            user_town = user[4]
            new_role = discord.utils.get(guild.roles, name=town)
            old_role = discord.utils.get(guild.roles, name=user_town)

        except Exception as e:
            print(e)
        else:
            try:
                City().change_city(member.id, town)
                Users().update_city(town, member.id)
                await member.remove_roles(old_role)
                await member.add_roles(new_role)
            except Exception as e:
                print(e)
            else:
                return await msg.edit(content=f"ทำการย้ายคุณจากเมือง {player_town} ไป ยัง {town} เป็นที่เรียบร้อยแล้ว")