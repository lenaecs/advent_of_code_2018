advent = open("Input/input_day_6.txt")

puzzle = []

for line in advent:
    line = line.strip()
    line = line.split(', ')
    line = list(map(int, line))
    puzzle.append(line)

print(len(puzzle))

def part1(puzzle, height, width):
    grid = []
    for y in range(height):
        grid.append(['.'] * width)
    for y in range(height):
        for x in range(width):
            distances = [-1] * len(puzzle)
            for coordinate in range(len(puzzle)):
                distances[coordinate] = abs(x - puzzle[coordinate][0]) + abs(y - puzzle[coordinate][1])
            min_distance = min(distances)
            if distances.count(min_distance) > 1:
                grid[y][x] = '.'
            else:
                grid[y][x] = distances.index(min_distance)
    edge_set = set([])
    for y in range(height):
        edge_set.add(grid[y][0])
        edge_set.add(grid[y][width - 1])
    for x in range(width):
        edge_set.add(grid[0][x])
        edge_set.add(grid[height - 1][x])
    results = [0] * len(puzzle)
    for y in grid:
        for x in y:
            if x != '.':
                results[x] += 1
    for area in edge_set:
        if area != '.':
            results[area] = -1
    return max(results)

# print(part1(puzzle, 500, 500))

def part2(puzzle, width, height):
    grid = []
    for y in range(height):
        grid.append(['.'] * width)
    region = 0
    for y in range(height):
        for x in range(width):
            distances = 0
            for coordinate in range(len(puzzle)):
                distances += abs(x - puzzle[coordinate][0]) + abs(y - puzzle[coordinate][1])
            if distances < 10000:
                region += 1
    return region

print(part2(puzzle, 500, 500))