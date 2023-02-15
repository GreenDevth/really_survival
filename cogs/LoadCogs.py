from Class.ChangeCity import ChangeCityCommand
from Class.MainLaw import MainLawCommand
from Class.SteamCheck import SteamCheckCommand
from Class.SubPlayer import SubPlayerCommand
from Class.TeaserEvent import TeaserEvents
from Class.Intro import IntroEvent
from Class.Start import StartProject
from Class.Supporter import SupporterMembers
from Class.The_Police import ThePoliceCommand
from Class.VerifyPlayer import VerifyPlayerCommand


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