import discord
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
        try:
            channel_name = "📚-มินิสตอรี่"
            channel = discord.utils.get(guild.channels, name=channel_name)
            if channel:
                pass
        except Exception as e:
            print(e)
        else:
            await channel.purge()
            await channel.send(embed=intro_story(), view=StoryView(self.bot))
        finally:
            return await ctx.response.send_message("ติดตั้งมินิสตอรี่เรียบร้อยแล้ว", ephemeral=True)




def setup(bot):
    bot.add_cog(StoryLauncher(bot))

