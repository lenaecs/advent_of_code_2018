advent = open("Input/input_day_7.txt")

puzzle = []

for line in advent:
    line = line.strip()
    line = line.split(' ')
    puzzle.append([line[1], line[7]])

def part1(puzzle):
    forward = dict()
    beginning = set([])
    ending = set([])
    backward = dict()
    for line in puzzle:
        if line[0] not in forward:
            forward[line[0]] = [line[1]]
        else:
            forward[line[0]].append(line[1])
        beginning.add(line[0])
        ending.add(line[1])
        if line[1] not in backward:
            backward[line[1]] = [line[0]]
        else:
            backward[line[1]].append(line[0])
    for line in puzzle:
        beginning.discard(line[1])
        ending.discard(line[0])
    end = None
    letters_ready = []
    for item in beginning:
        letters_ready.append(item)
    for item in ending:
        end = item
    letters_ready.sort()
    last_step = letters_ready.pop(0)
    solution = [last_step]
    while end not in solution:
        for letter in forward[last_step]:
            add_to_next = True
            for dependency in backward[letter]:
                if dependency not in solution:
                    add_to_next = False
            if add_to_next == True:
                letters_ready.append(letter)
        letters_ready.sort()
        last_step = letters_ready.pop(0)
        solution.append(last_step)
    solution_string = ''
    for letter in solution:
        solution_string = solution_string + letter
    return(solution_string)

print(part1(puzzle))