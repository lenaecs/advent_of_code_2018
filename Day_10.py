import re

advent = open("Input/input_day_10.txt")

# advent = ['position=< 9,  1> velocity=< 0,  2>',
#           'position=< 7,  0> velocity=<-1,  0>',
#           'position=< 3, -2> velocity=<-1,  1>',
#           'position=< 6, 10> velocity=<-2, -1>',
#           'position=< 2, -4> velocity=< 2,  2>',
#           'position=<-6, 10> velocity=< 2, -2>',
#           'position=< 1,  8> velocity=< 1, -1>',
#           'position=< 1,  7> velocity=< 1,  0>',
#           'position=<-3, 11> velocity=< 1, -2>',
#           'position=< 7,  6> velocity=<-1, -1>',
#           'position=<-2,  3> velocity=< 1,  0>',
#           'position=<-4,  3> velocity=< 2,  0>',
#           'position=<10, -3> velocity=<-1,  1>',
#           'position=< 5, 11> velocity=< 1, -2>',
#           'position=< 4,  7> velocity=< 0, -1>',
#           'position=< 8, -2> velocity=< 0,  1>',
#           'position=<15,  0> velocity=<-2,  0>',
#           'position=< 1,  6> velocity=< 1,  0>',
#           'position=< 8,  9> velocity=< 0, -1>',
#           'position=< 3,  3> velocity=<-1,  1>',
#           'position=< 0,  5> velocity=< 0, -1>',
#           'position=<-2,  2> velocity=< 2,  0>',
#           'position=< 5, -2> velocity=< 1,  2>',
#           'position=< 1,  4> velocity=< 2,  1>',
#           'position=<-2,  7> velocity=< 2, -2>',
#           'position=< 3,  6> velocity=<-1, -1>',
#           'position=< 5,  0> velocity=< 1,  0>',
#           'position=<-6,  0> velocity=< 2,  0>',
#           'position=< 5,  9> velocity=< 1, -2>',
#           'position=<14,  7> velocity=<-2,  0>',
#           'position=<-3,  6> velocity=< 2, -1>']

puzzle = []

for line in advent:
    line = line.strip()
    line = re.split('<|>|,', line)
    puzzle.append([[int(line[1].strip()), int(line[2].strip())], [int(line[4].strip()), int(line[5].strip())]])

def part1(puzzle):
    itts = 0
    current_spread = float("inf")
    delta = -1
    while delta < 0:
        itts += 1
        max_x = float("-inf")
        min_x = float("inf")
        max_y = float("-inf")
        min_y = float("inf")
        for line in puzzle:
            x = line[0][0] + itts * line[1][0]
            y = line[0][1] + itts * line[1][1]
            if x > max_x:
                max_x = x
            if x < min_x:
                min_x = x
            if y > max_y:
                max_y = y
            if y < min_y:
                min_y = y
        spread = max_x - min_x + max_y - min_y
        delta = spread - current_spread
        current_spread = spread
    itts = itts - 1
    grid = []
    for x in range(max_y + 10):
        new_row = []
        for y in range(max_x + 10):
            new_row.append('.')
        grid.append(new_row)
    for line in puzzle:
        x = line[0][0] + itts * line[1][0]
        y = line[0][1] + itts * line[1][1]
        print(x, y)
        grid[y][x] = '#'
    for line in grid:
        string = ''
        for value in line:
            string += value
        print(string)
    print(itts)

part1(puzzle)