import discord
from discord.utils import get
from discord.commands import SlashCommandGroup
from discord.ext import commands

from scripts.guilds import guild_data, roles_lists
from story.Storied import intro_story
from story.StoryContent import StoryView

guild_id = guild_data()["roleplay"]
commands_list = ["ข้อมูลผู้เล่น", "ข้อมูลการเงิน", "ปรับบทบาท"]
permissions_roles = roles_lists()

class StoryLauncher(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




    @commands.Cog.listener()
    async def on_ready(self):
        print(__class__.__name__, "online")
        self.bot.add_view(StoryView(self.bot))


    story = SlashCommandGroup(guild_ids=[guild_id], name='story', description="คำสั่งแสดงมินิสตอรี่")

    @story.command(name="เปิดใช้งานมินิสตอรี่", description="คำสั่งเปิดใช้งานเนื้อหาของมินิสตอรี่")
    async def into_story(
            self,
            ctx:discord.Interaction
    ):
        guild = ctx.guild
        cate_name = "THE WALKING DEAD"
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(
                read_messages=True,
                read_message_history = True,
                send_messages=False
            )
        }
        await ctx.defer(ephemeral=True, invisible=False)
        msg = await ctx.followup.send("ระบบกำลังจัดการะบบแสดงเนื้อหา โปรดรอสักครู่")
        try:
            cate = get(guild.categories, name=cate_name)
            if cate:
                pass
            else:
                cate = await guild.create_category(name=cate_name, overwrites=overwrites)
        except Exception as e:
            print(e)
        else:
            channel_name = "📚-เนื้อเรื่อง"
            try:
                channel = get(guild.channels, name=channel_name)
                if channel:
                    pass
                else:
                    channel = await guild.create_text_channel(name=channel_name, category=cate)
            except Exception as e:
                print(e)
            else:
                await channel.purge()
                await channel.send(embed=intro_story(), view=StoryView(self.bot))
                await msg.edit(content="จัดการระบบแสดงเนื้อหาสำเร็จ")




def setup(bot):
    bot.add_cog(StoryLauncher(bot))

