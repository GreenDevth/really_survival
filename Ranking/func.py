from db.Ranking import Ranking


def level_up(member, exp):
    try:
        old_exp = Ranking().ranking(member)[3]
        total = old_exp + exp

        if total >= 100000:
            Ranking().update_exp(member, total - 100000)
            old_level = Ranking().ranking(member)[2]
            total_level = old_level + 1
            Ranking().update_rank(member, total_level)
        else:
            pass
    except Exception as e:
        print(e)
        return False
    else:
        return True

