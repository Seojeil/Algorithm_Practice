# 달리기 경주


def solution(players, callings):
    player_dict = {player: idx for idx, player in enumerate(players)}

    for call in callings:
        r = player_dict[call]

        players[r - 1], players[r] = players[r], players[r - 1]
        player_dict[call] -= 1
        player_dict[players[r]] += 1

    return players
