import re

advent = open("Input/input_day_3.txt")

puzzle = []

for line in advent:
    line = line.strip()
    line = line.strip('#')
    split_line = re.split(' @ |,|: |x', line)
    split_line = list(map(int, split_line))
    puzzle.append(split_line)

test1 = [[123, 3, 2, 5, 4]]

def part_1(puzzle, height, width):
    cloth = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(0)
        cloth.append(row)
    for row in puzzle:
        for y in range(row[2], row[2] + row[4]):
            for x in range(row[1], row[1] + row[3]):
                cloth[y][x] += 1
    double_booked = 0
    for row in cloth:
        for inch in row:
            if inch > 1:
                double_booked += 1
    return double_booked

# for line in part_1(test1, 11, 9):
#     print(line)


print(part_1(puzzle, 1000, 1000))

def part_2(puzzle, height, width):
    cloth = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(set([]))
        cloth.append(row)
    not_eliminated = set([])
    for row in puzzle:
        not_eliminated.add(row[0])
    for row in puzzle:
        for y in range(row[2], row[2] + row[4]):
            for x in range(row[1], row[1] + row[3]):
                if len(cloth[y][x]) == 0:
                    cloth[y][x].add(row[0])
                else:
                    cloth[y][x].add(row[0])
                    for id in cloth[y][x]:
                        not_eliminated.discard(id)
    return not_eliminated

print(part_2(puzzle, 1000, 1000))