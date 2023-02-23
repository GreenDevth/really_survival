import random

import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup, Option

from Quests.db.Mission_db import reset_mission, reset_user_mission
from Quests.views.CreateQuest import CreateMissionButton
from Quests.views.GetNewMission import GetMissionButton
from Quests.views.ReportMission import MissionReportButton, ImageUploadButton, CloseReport
from scripts.guilds import guild_data

guild_id = guild_data()["realistic"]

quest_command_list = [
    "installer",
    "uninstaller",
    "open",
    "close",
    "database",
    "new_mission",
    "user_db"
]
role_list = ["Alexandria", "Kingdom", "Savior", "Commonwealth", "Hilltop"]
cate_name = "COMMUNITY TOWN"
ch_name = "📜-กระดานภารกิจ"


class QuestCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    quest = SlashCommandGroup(guild_ids=[guild_id], name="quest", description="Setup command for Quests")

    @commands.Cog.listener()
    async def on_ready(self):
        print(self.__class__.__name__)
        self.bot.add_view(CreateMissionButton(self.bot, None))
        self.bot.add_view(GetMissionButton())
        self.bot.add_view(MissionReportButton(self.bot))
        self.bot.add_view(ImageUploadButton(self.bot))
        self.bot.add_view(CloseReport())


    @quest.command(name="quest_manager", description="function for quests management system")
    async def quest_manager(self, ctx: discord.Interaction,
                            system: Option(str, "Select funcion", choices=quest_command_list)):
        guild = ctx.guild
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(
                view_channel=False
            ),

        }
        await ctx.response.defer(ephemeral=True, invisible=False)
        msg = await ctx.followup.send("System in progress...")
        if system == quest_command_list[6]:
            reset_user_mission()
            return await msg.edit(content=f"Config for {system} successfully...")

        if system == quest_command_list[4]:
            reset_mission()
            return await msg.edit(content=f"Config for {system} successfully...")

        if system == quest_command_list[0]:
            try:
                category = discord.utils.get(guild.categories, name=cate_name)
                if category:
                    channel = discord.utils.get(guild.channels, name=ch_name)
                    if channel:
                        pass
                    else:
                        await guild.create_text_channel(name=ch_name, category=category)
                else:
                    category = await guild.create_category(name=cate_name, overwrites=overwrites)
                    await guild.create_text_channel(name=ch_name, category=category)
            except Exception as e:
                return await msg.edit(content=e)
            else:
                channel = discord.utils.get(guild.channels, name=ch_name)
                for r in role_list:
                    role = discord.utils.get(guild.roles, name=r)
                    if role:
                        await channel.set_permissions(
                            role,
                            overwrite=discord.PermissionOverwrite(
                                view_channel=True,
                                send_messages=True,
                                read_messages=True,
                                read_message_history=True,
                                attach_files=True
                            )
                        )
                    else:
                        pass
                await channel.purge()
                await channel.send("ok")
                return await msg.edit(content=f"System ` {system} ` has been complete !!!!")

        if system == quest_command_list[5]:
            await msg.edit(content="พิมพ์ชื่อภารกิจของคุณ")

            try:
                message = await self.bot.wait_for(event='message')
                if message.content:
                    await message.delete()
                    pass
            except Exception as e:
                return await msg.edit(content=e)
            else:
                title = message.content
                await msg.edit(content="ระบุ image url ของคุณ")
                try:
                    message = await self.bot.wait_for(event='message')
                    if message.content:
                        await message.delete()
                        pass
                except Exception as e:
                    return await msg.edit(content=e)
                else:
                    img = message.content
                    exp = random.randint(0,1000)
                    coins = random.randint(0,1000)
                    amount = random.randint(1,5)
                    embed = discord.Embed(
                        title="📦 {}".format(title),
                        description="นำส่งสินค้าให้กับ Guild Master ตามจำนวนและเวลาที่ระบุไว้ในคำสั่ง"
                    )
                    embed.add_field(name="จำนวนสินค้า", value="{}".format(amount))
                    embed.add_field(name="ค่าประสบการณ์", value=f"{exp}")
                    embed.add_field(name="เงินรางวัล", value=f"{coins}")
                    embed.set_image(url=img)
                    data = [
                        title,
                        img,
                        amount,
                        exp,
                        coins
                    ]

                    return await msg.edit(content=None, embed=embed, view=CreateMissionButton(self.bot, data))



