import json

import discord


def secrets_data():
    with open('./json_file/config.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def guild_data():
    with open('./scripts/guild_id.json', 'r', encoding='utf-8') as g:
        data = json.load(g)
        return data


def owner_data():
    with open('./scripts/owner_id.json', 'r', encoding='utf-8') as o:
        data = json.load(o)
        return data


def category():
    with open('./scripts/channels.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data["category"]


def channels():
    with open('./scripts/channels.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data["channel"]


def separate_channles():
    with open('./scripts/channels.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data["separate"]


def discord_roles():
    with open('./scripts/roles.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data["roles"]

def roles_colour(r):
    if r == discord_roles()[0]:
        color = discord.Colour.from_rgb(102, 0, 102)
        return color
    if r == discord_roles()[1]:
        color = discord.Colour.from_rgb(51, 153, 204)
        return color
    if r == discord_roles()[2]:
        color = discord.Colour.from_rgb(0, 153, 102)
        return color
    if r == discord_roles()[3]:
        color = discord.Colour.from_rgb(0, 153, 255)
        return color
    if r == discord_roles()[4]:
        color = discord.Colour.from_rgb(255, 153, 51)
        return color
    if r == discord_roles()[5]:
        color = discord.Colour.from_rgb(102, 153, 153)
        return color
    if r == discord_roles()[6]:
        color = discord.Colour.from_rgb(204, 153, 51)
        return color
    if r == discord_roles()[7]:
        color = discord.Colour.from_rgb(255, 204, 51)
        return color
    if r == discord_roles()[8]:
        color = discord.Colour.from_rgb(0, 153, 51)
        return color
    if r == discord_roles()[9]:
        color = discord.Colour.from_rgb(0, 102, 102)
        return color
    if r == discord_roles()[10]:
        color = discord.Colour.from_rgb(0, 102, 153)
        return color
    if r == discord_roles()[11]:
        color = discord.Colour.from_rgb(153, 153, 102)
        return color
    if r == discord_roles()[12]:
        color = discord.Colour.from_rgb(255, 102, 0)
        return color
    if r == discord_roles()[13]:
        color = discord.Colour.from_rgb(255, 255, 255)
        return color


# update cooldown
def update_cooldown(number):
    cooldown_file = open('./scripts/cooldown.json', 'r', encoding='utf-8')
    json_object = json.load(cooldown_file)
    cooldown_file.close()

    json_object["cooldown"]["time"] = int(number)
    cooldown_file = open('./scripts/cooldown.json', 'w', encoding='utf-8')
    json.dump(json_object, cooldown_file, ensure_ascii=False, indent=4)
    cooldown_file.close()


# get cooldown
def get_cooldown_time():
    with open('./scripts/cooldown.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data["cooldown"]["time"]

def scum_uri():
    with open(f'./scripts/scum_server.json') as config:
        data = json.load(config)
        return data


def roles_lists():
    role_lists = ["Administrator", "All", "Read Only"]
    for role in discord_roles():
        role_lists.append(role)
    return role_lists

def Occupation():
    with open('./scripts/occupation.json', 'r', encoding='utf-8') as o:
        data = json.load(o)
        return data