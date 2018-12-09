advent = open("Input/input_day_8.txt")

# test = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
# line = test.split()
# puzzle = list(map(int, line))

for line in advent:
    line = line.strip()
    line = line.split(' ')
    puzzle = list(map(int, line))

def part1(puzzle, position):
    children = puzzle[position]
    meta_entries = puzzle[position + 1]
    if children == 0:
        meta_data = 0
        for i in range(meta_entries):
            meta_data += puzzle[position + 2 + i]
        return meta_data, position + 2 + meta_entries
    else:
        meta_data = 0
        new_position = position + 2
        for child in range(children):
            temp_meta, new_position = part1(puzzle, new_position)
            meta_data += temp_meta
        for entry in range(meta_entries):
            meta_data += puzzle[new_position]
            new_position += 1
        return meta_data, new_position

print(part1(puzzle, 0))

def part2(puzzle, position):
    children = puzzle[position]
    meta_entries = puzzle[position + 1]
    if children == 0:
        meta_data = 0
        for i in range(meta_entries):
            meta_data += puzzle[position + 2 + i]
        return meta_data, position + 2 + meta_entries
    else:
        child_points = []
        new_position = position + 2
        meta_data = 0
        for child in range(children):
            temp_meta, new_position = part2(puzzle, new_position)
            child_points.append(temp_meta)
        for entry in range(meta_entries):
            if 0 < puzzle[new_position] and puzzle[new_position] <= len(child_points):
                meta_data += child_points[puzzle[new_position] - 1]
            new_position += 1
        return(meta_data, new_position)

print(part2(puzzle, 0))
# 63136 is too high