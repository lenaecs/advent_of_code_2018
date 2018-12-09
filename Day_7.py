advent = open("Input/input_day_7.txt")

test = ['Step C must be finished before step A can begin.',
        'Step C must be finished before step F can begin.',
        'Step A must be finished before step B can begin.',
        'Step A must be finished before step D can begin.',
        'Step B must be finished before step E can begin.',
        'Step D must be finished before step E can begin.',
        'Step F must be finished before step E can begin.']

puzzle = []

for line in advent:
    line = line.strip()
    line = line.split(' ')
    puzzle.append([line[1].lower(), line[7].lower()])

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

def part2(puzzle, base_time, workers):
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
    solution = ''
    work_queue = []
    empty_workers = []
    for i in range(workers):
        if len(letters_ready) != 0:
            current_letter = letters_ready.pop(0)
            work_queue.append([current_letter, base_time + ord(current_letter) - 96 + 1])
        else:
            work_queue.append(['', -1])
            empty_workers.append(i)
    seconds = 0
    forward[end] = []
    while end not in solution:
        current_letters = []
        for worker in range(len(work_queue)):
            if work_queue[worker][1] == 1:
                current_letters.append(work_queue[worker][0])
                solution = solution + work_queue[worker][0]
                empty_workers.append(worker)
            work_queue[worker][1] -= 1
        for current_letter in current_letters:
            for letter in forward[current_letter]:
                add_to_next = True
                for dependency in backward[letter]:
                    if dependency not in solution:
                        add_to_next = False
                if add_to_next == True:
                    letters_ready.append(letter)
        letters_ready.sort()
        while len(empty_workers) > 0 and len(letters_ready) > 0:
            next_letter = letters_ready.pop(0)
            next_worker = empty_workers.pop()
            work_queue[next_worker][0] = next_letter
            work_queue[next_worker][1] = base_time + ord(next_letter) - 96
        seconds += 1
    return seconds - 1

print(part2(puzzle, 60, 5))

#271 is too low
#1360 is too high