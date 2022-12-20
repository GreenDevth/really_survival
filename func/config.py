import json
import os.path
from datetime import datetime

import requests

from db.users import Users

from dateutil import tz


def current_time(args):
    # "%H:%M:%S"
    local_zone = tz.tzlocal()
    now = datetime.now()
    local_dt = now.astimezone(local_zone)
    return local_dt.strftime(args)

def config_():
    with open('./json_file/config.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data


def img_(txt):
    with open('./json_file/image.json', 'r', encoding='utf-8') as img:
        data = json.load(img)
        return data[txt]

def get_cooldown_time():
    with open('./json_file/discord.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data["cooldown"]["time"]

# update cooldown
def update_cooldown(number):
    cooldown_file = open('./json_file/discord.json', 'r', encoding='utf-8')
    json_object = json.load(cooldown_file)
    cooldown_file.close()

    json_object["cooldown"]["time"] = int(number)
    cooldown_file = open('./json_file/discord.json', 'w', encoding='utf-8')
    json.dump(json_object, cooldown_file, ensure_ascii=False, indent=4)
    cooldown_file.close()

def database_check(filename):
    if os.path.isfile(filename):
        return True
    else:
        return False

def steam_check(steam):
    my_variable = steam
    if my_variable.isdigit() and len(my_variable) == 17:
        return True
    else:
        return False


def save_to_db(discord_id, steam_id):
    d_id = discord_id
    s_id = steam_id
    join_date = current_time("%d/%m/%Y")
    return Users().new_player(d_id, s_id, join_date)


auth = config_()["battle_token"]
head = {'Authorization': 'Brarer' + auth}

def battle_info():
    res = requests.get(config_()["server_url"], headers=head)
    return res.json()

def server_status():
    jsonObj = battle_info()
    result = f"```\nServer: {jsonObj['data']['attributes']['name']}" \
             f"\n======================================" \
             f"\nIP: {jsonObj['data']['attributes']['ip']}:{jsonObj['data']['attributes']['port']}" \
             f"\nStatus: {jsonObj['data']['attributes']['status']}" \
             f"\nTime in Game: {jsonObj['data']['attributes']['details']['time']}" \
             f"\nPlayers: {jsonObj['data']['attributes']['players']}/{jsonObj['data']['attributes']['maxPlayers']}" \
             f"\nRanking: #{jsonObj['data']['attributes']['rank']}" \
             f"\nGame version: {jsonObj['data']['attributes']['details']['version']}\n" \
             f"\nServer Restarts Every 6 hours" \
             f"\nDay 3.8 hours, Night 1 hours" \
             f"\n======================================" \
             f"\n14Studio, Copyright © 1983 - 2023```"
    return result.strip()