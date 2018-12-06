advent = open("Input/input_day_5.txt")

puzzle = ''
for line in advent:
    puzzle = line.strip()

def part1(puzzle):
    polymers = []
    for letter in puzzle:
        polymers.append(letter)
    moves = 1
    while moves > 0:
        moves = 0
        to_delete = []
        for poly in range(len(polymers) - 1):
            if polymers[poly] != polymers[poly + 1] and polymers[poly].lower() == polymers[poly + 1].lower():
                if poly not in to_delete:
                    to_delete.append(poly)
                    to_delete.append(poly + 1)
                moves += 1
        for i in reversed(to_delete):
            polymers.pop(i)
    return len(polymers)

# 12056 is too high
#print(part1('dabAcCaCBAcCcaDA'))
print(part1(puzzle))

def part2(puzzle):
    min_set = float('inf')
    for alpha in 'abcdefghijklmnopqrstuvwxyz':
        polymers = []
        for letter in puzzle:
            if letter.lower() != alpha:
                polymers.append(letter)
        moves = 1
        while moves > 0:
            moves = 0
            to_delete = []
            for poly in range(len(polymers) - 1):
                if polymers[poly] != polymers[poly + 1] and polymers[poly].lower() == polymers[poly + 1].lower():
                    if poly not in to_delete:
                        to_delete.append(poly)
                        to_delete.append(poly + 1)
                    moves += 1
            for i in reversed(to_delete):
                polymers.pop(i)
        if len(polymers) < min_set:
            min_set = len(polymers)
        print(alpha, len(polymers))
    return min_set

print(part2(puzzle))