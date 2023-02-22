import json

def img_(txt):
    with open('./Quests/json/img.json', 'r', encoding='utf-8') as img:
        data = json.load(img)
        return data[txt]