import asyncio
import json
import os
from abc import ABC

import discord
from discord.ext import commands
from func.config import config_

guild_id = config_()["guild"]
owner_id = config_()["owner"]


class Really_survival(commands.Bot, ABC):
    def __init__(self, *agrs, **kwagrs):
        super().__init__(command_prefix=commands.when_mentioned_or("!"), *agrs, **kwagrs, intents=discord.Intents.all())
        self.token = config_()["token"]


bot = Really_survival(owner_id=owner_id, case_insensitive=True)


@bot.event
async def on_ready():
    print(bot.user.name, " is Ready")
    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 1
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(
            type=discord.ActivityType.watching, name=f"{members} Discord Members")
    )


@bot.command()
@commands.is_owner()
async def clear(ctx, amount):
    if amount == 'all':
        return await ctx.channel.purge()
    elif amount.isdigit:
        amounts = int(amount)
        await ctx.send(f'**{amounts}** Message has been deleted.')
        await asyncio.sleep(1)
        return await ctx.channel.purge(limit=amounts + 1)


@bot.command()
@commands.is_owner()
async def export_channel(ctx):
    guild = bot.get_guild(guild_id)
    try:

        list_channel = []
        for channel in guild.channels:
            list_channel.append(channel.name)

        data = list_channel

        channels = {
            "channel": data
        }

        with open('json_file/channels.json', 'w', encoding='utf-8') as ch:
            json.dump(channels, ch, ensure_ascii=False, indent=4)

    except Exception as e:
        print(e)
    await ctx.send("ok")


if __name__ == '__main__':
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py') and filename != "__init__.py":
            bot.load_extension('cogs.{}'.format(filename[:-3]))

    bot.run(bot.token)
