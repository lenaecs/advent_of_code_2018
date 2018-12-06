import re

advent = open("Input/input_day_4.txt")

puzzle = []

for line in advent:
    line = line.strip()
    puzzle.append(line)

puzzle.sort()

def part1(puzzle):
    guard_dict = {}
    guard = None
    for line in range(len(puzzle)):
        if "begins" in puzzle[line]:
            guard = [int(s) for s in re.split('#| ', puzzle[line][18:]) if s.isdigit()][0]
            if guard not in guard_dict:
                guard_dict[guard] = [0] * 60
        if "asleep" in puzzle[line]:
            if "wakes" in puzzle[line + 1]:
                for minute in range(int(puzzle[line][15:17]), int(puzzle[line + 1][15:17])):
                    guard_dict[guard][minute] += 1
    max_guard = None
    max_minutes_asleep = 0
    for guard in guard_dict:
        if sum(guard_dict[guard]) > max_minutes_asleep:
            max_guard = guard
            max_minutes_asleep = sum(guard_dict[guard])
    asleep_min = -1
    max_minutes = 0
    for minute in range(len(guard_dict[max_guard])):
        if guard_dict[max_guard][minute] > max_minutes:
            asleep_min = minute
            max_minutes = guard_dict[max_guard][minute]
    return max_guard * asleep_min

print(part1(puzzle))

def part2(puzzle):
    guard_dict = {}
    guard = None
    for line in range(len(puzzle)):
        if "begins" in puzzle[line]:
            guard = [int(s) for s in re.split('#| ', puzzle[line][18:]) if s.isdigit()][0]
            if guard not in guard_dict:
                guard_dict[guard] = [0] * 60
        if "asleep" in puzzle[line]:
            if "wakes" in puzzle[line + 1]:
                for minute in range(int(puzzle[line][15:17]), int(puzzle[line + 1][15:17])):
                    guard_dict[guard][minute] += 1
    max_guard = None
    max_minutes = 0
    asleep_min = 0
    for guard in guard_dict:
        for minute in range(len(guard_dict[guard])):
            if guard_dict[guard][minute] > max_minutes:
                asleep_min = minute
                max_minutes = guard_dict[guard][minute]
                max_guard = guard
    return max_guard * asleep_min

print(part2(puzzle))