import json


def ranking_(txt):
    with open('./json_file/rank.json', 'r', encoding='utf-8') as rank:
        data = json.load(rank)
        return data[txt]