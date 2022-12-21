from discord.ext import commands

from views.Contract.ContactCloseView import ContactCloseButton
from views.Members.MemberViews import UsersViews
from views.System.InfoView import InformationViews
from views.System.ManualViews import PopulationManualView


class ViewLoader(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(InformationViews(self.bot))
        self.bot.add_view(PopulationManualView(self.bot))
        self.bot.add_view(UsersViews(self.bot))
        self.bot.add_view(ContactCloseButton(self.bot))

def setup(bot):
    bot.add_cog(ViewLoader(bot))
