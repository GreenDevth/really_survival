import discord

from discord.ext import commands
from discord.commands import SlashCommandGroup, Option

from scripts.guilds import guild_data

guild_id = guild_data()["realistic"]

from db.users import Users
from db.Events import TeaserEvent


class Wallet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    wallet = SlashCommandGroup(guild_ids=[guild_id], name="wallet", description="คำสั่งเกี่ยวกับเงินของผู้เล่น")