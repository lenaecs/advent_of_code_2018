advent = ['/->-\         ',
          '|   |  /----\ ',
          '| /-+--+-\  | ',
          '| | |  | v  | ',
          '\-+-/  \-+--/ ',
          '\------/      ']

puzzle = []
for line in advent:
    row = []
    for char in line:
        if char != '\n':
            row.append(char)
    puzzle.append(row)

class cart:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        

def part1(puzzle):
    for
