import discord
from db.users import Users


def user_info(discord_id):
    data = Users().player(discord_id)
    return data
