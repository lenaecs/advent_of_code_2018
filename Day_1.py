advent = open("Input/input_day_1")

puzzle = []

for line in advent:
    puzzle.append(line.strip())

def part_1(puzzle):
    tot = 0
    for number in puzzle:
        if number[0] == '+':
            tot += int(number[1:])
        else:
            tot -= int(number[1:])
    return tot

print(part_1(puzzle))

def part_2(puzzle):
    frequencies = set([])
    number = 0
    placement = 0
    while number not in frequencies:
        frequencies.add(number)
        if puzzle[placement][0] == '+':
            number += int(puzzle[placement][1:])
        else:
            number -= int(puzzle[placement][1:])
        placement = (placement + 1) % len(puzzle)
    return number

print(part_2(puzzle))