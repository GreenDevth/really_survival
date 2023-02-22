from Approved.VerifyMemer import VerifyMemberCommand
from Banks.Wallet import UserWalletCommand
from Class.ChangeCity import ChangeCityCommand
from Class.EventCommand import EventCommands
from Class.HowToStory import HowToStoryCommand
from Class.MainLaw import MainLawCommand
from Class.MyTown import MyTownCommand
from Class.Save_Rick import SaveRickCommand
from Class.SteamCheck import SteamCheckCommand
from Class.SteamUpdate import SteamUpdateCommand
from Class.SubPlayer import SubPlayerCommand
from Class.TeaserEvent import TeaserEvents
from Class.Intro import IntroEvent
from Class.Start import StartProject
from Class.Supporter import SupporterMembers
from Class.The_Police import ThePoliceCommand
from Class.UserCommands import UserCommands
from Class.VerifyPlayer import VerifyPlayerCommand
from Quests.Quest import QuestCommand


def setup(bot):
    bot.add_cog(TeaserEvents(bot))
    bot.add_cog(IntroEvent(bot))
    bot.add_cog(StartProject(bot))
    bot.add_cog(SupporterMembers(bot))
    bot.add_cog(ChangeCityCommand(bot))
    bot.add_cog(ThePoliceCommand(bot))
    bot.add_cog(SubPlayerCommand(bot))
    bot.add_cog(VerifyPlayerCommand(bot))
    bot.add_cog(SteamCheckCommand(bot))
    bot.add_cog(MainLawCommand(bot))
    bot.add_cog(MyTownCommand(bot))
    bot.add_cog(SteamUpdateCommand(bot))
    bot.add_cog(EventCommands(bot))
    bot.add_cog(UserCommands(bot))
    bot.add_cog(SaveRickCommand(bot))
    bot.add_cog(HowToStoryCommand(bot))
    bot.add_cog(QuestCommand(bot))
    bot.add_cog(UserWalletCommand(bot))
    bot.add_cog(VerifyMemberCommand(bot))