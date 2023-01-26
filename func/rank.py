import json



def ranking_(txt):
    with open('./json_file/rank.json', 'r', encoding='utf-8') as rank:
        data = json.load(rank)
        return data[txt]



def ranking_img(rank):
    if rank == 1:
        return ranking_("b_1")
    if rank == 2:
        return ranking_("b_2")
    if rank == 3:
        return ranking_("b_3")
    if rank == 4:
        return ranking_("b_4")
    if rank == 5:
        return ranking_("b_5")
    if rank == 6:
        return ranking_("s_1")
    if rank == 7:
        return ranking_("s_2")
    if rank == 8:
        return ranking_("s_3")
    if rank == 9:
        return ranking_("s_4")
    if rank == 10:
        return ranking_("s_5")
    if rank == 11:
        return ranking_("g_1")
    if rank == 12:
        return ranking_("g_2")
    if rank == 13:
        return ranking_("g_3")
    if rank == 14:
        return ranking_("g_4")
    if rank == 15:
        return ranking_("g_5")
