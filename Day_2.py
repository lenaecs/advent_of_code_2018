advent = open("Input/input_day_2")

puzzle = []

for line in advent:
    puzzle.append(line.strip())

def part1(puzzle):
    two_letters = 0
    three_letters = 0
    for line in puzzle:
        letter_dict = {}
        for letter in line:
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
        has_two_letters = False
        has_three_letters = False
        for letter in letter_dict:
            if letter_dict[letter] == 2:
                has_two_letters = True
            elif letter_dict[letter] == 3:
                has_three_letters = True
        if has_three_letters == True:
            three_letters += 1
        if has_two_letters == True:
            two_letters += 1
    return two_letters * three_letters

print(part1(puzzle))

def part2(puzzle):
    box_set = set([])
    for box in puzzle:
        for id in box_set:
            letter_mismatch = 0
            for pos in range(len(box)):
                if box[pos] != id[pos]:
                    letter_mismatch += 1
                    letter_pos = pos
            if letter_mismatch == 1:
                new_word = ''
                for pos in range(len(box)):
                    if pos != letter_pos:
                        new_word = new_word + box[pos]
                return new_word
        box_set.add(box)

print(part2(puzzle))
