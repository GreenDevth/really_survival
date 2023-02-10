
from discord.utils import get
from discord.ext import commands
from func.Story import *

from discord.commands import SlashCommandGroup, Option

from scripts.guilds import guild_data

guild_id = guild_data()["realistic"]

class StartProject(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    start = SlashCommandGroup(guild_ids=[guild_id], name="start", description="คำสั่งรัน mini story รายสัปดาห์")

    @start.command(name="แสดงเนื้อหาประจำสัปดาห์", description="คำสั่งเปิดการแสดงเนื้อหาของประจำแต่ละสัปดาห์")
    async def show_story_by_week(
            self,
            ctx:discord.Interaction,
            stories:Option(str, "เลือกเนื้อหาที่ต้องการแสดงสำหรับอาทิตย์นี้", choices=story_lists)
    ):

        guild = ctx.guild
        cate_name = "THE WALKING DEAD"
        choices = story_lists
        await ctx.response.defer(ephemeral=True, invisible=False)
        msg = await ctx.followup.send("ระบบกำลังจัดการะบบแสดงเนื้อหา โปรดรอสักครู่")
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(
                read_messages=True,
                read_message_history=True,
                send_messages=False
            )
        }

        try:
            cate = get(guild.categories, name=cate_name)
            if cate:
                pass
            else:
                cate = await guild.create_category(name=cate_name, overwrites=overwrites)
        except Exception as e:
            return await msg.edit(content=e)
        else:
            if stories == choices[int(story_lists.index(stories))]:
                channel_name = f"📔-{stories}"
                try:
                    channel = discord.utils.get(guild.channels, name=channel_name)
                    if channel:
                        await channel.purge()
                        await channel.send(embed=story_content(str(stories)))
                    else:
                        channel = await guild.create_text_channel(name=channel_name, category=cate)
                        await channel.send(embed=story_content(str(stories)))
                except Exception as e:
                    return await msg.edit(content=e)
                else:
                    return await msg.edit(content=f"เพิ่มข้อมูลเนื้อหาอีเว้น {stories} ให้กับระบบเรียบร้อย")


