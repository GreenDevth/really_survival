import json
import os.path
from os.path import isfile, getsize
from datetime import datetime
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
    with open('./scripts/discord.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data["cooldown"]["time"]

# update cooldown
def update_cooldown(number):
    cooldown_file = open('./scripts/discord.json', 'r', encoding='utf-8')
    json_object = json.load(cooldown_file)
    cooldown_file.close()

    json_object["cooldown"]["time"] = int(number)
    cooldown_file = open('./scripts/discord.json', 'w', encoding='utf-8')
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