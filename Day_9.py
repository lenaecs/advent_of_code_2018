from collections import deque

def part1(last_marble, players):
    game = deque([0])
    player_scores = [0] * players
    player = 0
    marble = 0
    while marble < last_marble:
        marble += 1
        player = (player + 1) % players
        if marble % 23 != 0:
            game.rotate(-1)
            game.append(marble)
        else:
            game.rotate(7)
            player_scores[player] += game.pop() + marble
            game.rotate(-1)
    return max(player_scores)

print(part1(7124000, 478))


