import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup, Option
from scripts.guilds import guild_data

guild_id = guild_data()["realistic"]

quest_command_list = [
    "installer",
    "uninstaller",
    "open",
    "close"
]

class QuestCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    quest = SlashCommandGroup(guild_ids=[guild_id], name="quest", description="Setup command for Quests")


    @commands.Cog.listener()
    async def on_ready(self):
        print(self.__class__.__name__)




