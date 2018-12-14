advent = open('Input/input_day_12.txt')

puzzle = []
for line in advent:
    line = line.strip()
    line = line.split()
    puzzle.append(line)

def part1(puzzle):
    next_state = puzzle.pop(0)[2]
    puzzle.pop(0)
    index_start = 0
    old_sum = 0
    for i in range(20):
        index_start -= 2
        current_state = '....' + next_state + '....'
        next_state = ''
        for letter in range(2, len(current_state) - 2):
            for pattern in puzzle:
                if pattern[0] == current_state[letter - 2:letter + 3]:
                    next_state = next_state + pattern[2]
        new_sum = 0
        current_index = index_start
        for i in next_state:
            if i == '#':
                new_sum += current_index
            current_index += 1
        print(old_sum - new_sum, new_sum)
        old_sum = new_sum


print(part1(puzzle))

print(13505 + (50000000000 - 200) * 63)