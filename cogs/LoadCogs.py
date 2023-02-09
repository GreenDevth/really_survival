from Class.TeaserEvent import TeaserEvents
from Class.Intro import IntroEvent


def setup(bot):
    bot.add_cog(TeaserEvents(bot))
    bot.add_cog(IntroEvent(bot))