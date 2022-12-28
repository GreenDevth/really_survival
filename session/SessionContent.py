import discord
from discord.ext import commands


class SessionContent(discord.ui.View):
    def __init__(self, bot):
        super(SessionContent, self).__init__(timeout=None)
        self.bot = bot