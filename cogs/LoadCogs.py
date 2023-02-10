from Class.TeaserEvent import TeaserEvents
from Class.Intro import IntroEvent
from Class.Start import StartProject
from Class.Supporter import SupporterMembers


def setup(bot):
    bot.add_cog(TeaserEvents(bot))
    bot.add_cog(IntroEvent(bot))
    bot.add_cog(StartProject(bot))
    bot.add_cog(SupporterMembers(bot))