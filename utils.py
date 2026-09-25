def update_score(result, score):
    if result == "You Win!":
        score["player"] += 1
    elif result == "Computer Wins!":
        score["computer"] += 1

    return score


def reset_score(score):
    score["player"] = 0
    score["computer"] = 0