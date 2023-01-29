import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup, Option

from func.events import event_list, event_contents
from scripts.guilds import guild_data


guild_id = guild_data()["realistic"]

class StoryEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    event = SlashCommandGroup(guild_ids=[guild_id], name="event", description="คำสั่งสำหรับแอดมิน")

    @event.command(name="แสดงเนื้อหาอีเว้น", description="คำสั่งติดตั้งแคตตากอรี่และแชลแนลสำหรับแสดงเนื้อหาของอีเว้น")
    async def event_installer(
            self,
            ctx:discord.Interaction,
            event:Option(str, "เลือกอีเว้นที่ต้องการ", choices=event_list)

    ):
        guild = ctx.guild
        choices = event_list
        cate = "EVENT CONTENT"
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(
                view_channel=True,
                read_messages=True,
                read_message_history=True,
                send_messages=False
            )
        }
        try:
            if discord.utils.get(guild.categories, name=cate):
                pass
            else:
                await guild.create_category(name=cate, overwrites=overwrites)
        except Exception as e:
            return await ctx.response.send_message(e, ephemeral=True)
        else:
            if event == choices[int(event_list.index(event))]:
                channel_name = f"📔-{event}"
                try:
                    cates = discord.utils.get(guild.categories, name=cate)
                    channel = discord.utils.get(guild.channels, name=channel_name)
                    if channel:
                        await channel.purge()
                        await channel.send(embed=event_contents(str(event)))
                    else:
                        channle = await guild.create_text_channel(name=channel_name, category=cates)
                        await channle.send(embed=event_contents(str(event)))
                except Exception as e:
                    return await ctx.response.send_message(e, ephemeral=True)
                else:
                    return await ctx.response.send_message(f"เพิ่มข้อมูลเนื้อหาอีเว้น {event} ให้กับระบบเรียบร้อย", ephemeral=True)



def setup(bot):
    bot.add_cog(StoryEvent(bot))
