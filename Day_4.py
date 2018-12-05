import re

advent = open("Input/input_day_4.txt")

puzzle = []

for line in advent:
    line = line.strip()
    puzzle.append(line)

puzzle.sort()

def part1(puzzle):
    guard_dict = {}
    asleep = False
    for line in puzzle:
        guard = None
        if "begins" in line:
            guard = [int(s) for s in re.split('#| ', line[18:]) if s.isdigit()][0]
        if guard not in guard_dict:
            guard_dict[guard] = [0] * 60
        if "asleep" in line:
            a


part1(puzzle)