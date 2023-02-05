import discord
from discord.commands import SlashCommandGroup, Option
from discord.ext import commands

from func.events import extra_list, extra_event_contents
from scripts.guilds import guild_data

guild_id = guild_data()["realistic"]


class ExtraEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    extra = SlashCommandGroup(guild_ids=[guild_id], name="extra", description="คำสั่งแสดงผลอีเว้นเพิ่มเติม")

    @extra.command(name="แสดงเนื้อหาอีเว้นเสริม", description="คำสั่งติดตั้งแคตตากอรี่และแชลแนลสำหรับแสดงเนื้อหาอีเว้นเสริม")
    async def extra_event_installer(
            self,
            ctx:discord.Interaction,
            extra:Option(str, "เลือกอีเว้นที่ต้องการ", choices=extra_list)
    ):
        guild = ctx.guild
        choices = extra_list
        cate = "EXTRA EVENT"
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
            if extra == choices[int(extra_list.index(extra))]:
                channel_name = f"📔-{extra}"
                try:
                    cates = discord.utils.get(guild.categories, name=cate)
                    channel = discord.utils.get(guild.channels, name=channel_name)
                    if channel:
                        await channel.purge()
                        await channel.send(embed=extra_event_contents(str(extra)))
                    else:
                        channle = await guild.create_text_channel(name=channel_name, category=cates)
                        await channle.send(embed=extra_event_contents(str(extra)))
                except Exception as e:
                    return await ctx.response.send_message(e, ephemeral=True)
                else:
                    return await ctx.response.send_message(f"เพิ่มข้อมูลเนื้อหาอีเว้น {extra} ให้กับระบบเรียบร้อย",
                                                           ephemeral=True)
def setup(bot):
    bot.add_cog(ExtraEvents(bot))