import json


def ranking_(txt):
    with open('./json_file/rank.json', 'r', encoding='utf-8') as rank:
        data = json.load(rank)
        return data[txt]



def ranking_img(rank):
    if rank == 1:
        return ranking_(rank)