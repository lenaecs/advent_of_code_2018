# advent = ['/->-\         ',
#           '|   |  /----\ ',
#           '| /-+--+-\  | ',
#           '| | |  | v  | ',
#           '\-+-/  \-+--/ ',
#           '  \------/    ']

advent = open('Input/input_day_13.txt')

puzzle = []
for line in advent:
    row = []
    for char in line:
        if char != '\n':
            row.append(char)
    puzzle.append(row)

class Cart:
    def __init__(self, position, symbol):
        self.position = position
        if symbol == '^':
            self.direction = (0, -1)
        elif symbol == 'v':
            self.direction = (0, 1)
        elif symbol == '<':
            self.direction = (-1, 0)
        elif symbol == '>':
            self.direction = (1, 0)
        self.next_turn = 'left'

    def intersection(self):
        if self.next_turn == 'left':
            if self.direction == (0, -1):
                self.direction = (-1, 0)
            elif self.direction == (0, 1):
                self.direction = (1, 0)
            elif self.direction == (1, 0):
                self.direction = (0, -1)
            else:
                self.direction = (0, 1)
            self.next_turn = 'straight'
        elif self.next_turn == 'straight':
            self.next_turn = 'right'
        elif self.next_turn == 'right':
            if self.direction == (0, -1):
                self.direction = (1, 0)
            elif self.direction == (0, 1):
                self.direction = (-1, 0)
            elif self.direction == (1, 0):
                self.direction = (0, 1)
            else:
                self.direction = (0, -1)
            self.next_turn = 'left'

    def turn(self, symbol):
        if symbol == '\\':
            if self.direction == (0, -1):
                self.direction = (-1, 0)
            elif self.direction == (0, 1):
                self.direction = (1, 0)
            elif self.direction == (1, 0):
                self.direction = (0, 1)
            else:
                self.direction = (0, -1)
        elif symbol == '/':
            if self.direction == (0, -1):
                self.direction = (1, 0)
            elif self.direction == (0, 1):
                self.direction = (-1, 0)
            elif self.direction == (1, 0):
                self.direction = (0, -1)
            else:
                self.direction = (0, 1)

    def move(self):
        self.position[0] += self.direction[0]
        self.position[1] += self.direction[1]

    def get_pos(self):
        return (self.position[0], self.position[1])

def part1(puzzle):
    carts = []
    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            if puzzle[y][x] in ['<', 'v', '>', '^']:
                carts.append(Cart([x, y], puzzle[y][x]))
    while 1 > 0:
        carts.sort(key=lambda c: c.position)
        position_list = []
        for cart in carts:
            position_list.append(cart.get_pos())
        for cart in range(len(carts)):
            carts[cart].move()
            pos = carts[cart].get_pos()
            position_list[cart] = pos
            if len(position_list) != len(set(position_list)):
                return pos
            if puzzle[pos[1]][pos[0]] in ['\\', '/']:
                carts[cart].turn(puzzle[pos[1]][pos[0]])
            elif puzzle[pos[1]][pos[0]] == '+':
                carts[cart].intersection()

print(part1(puzzle))

def part2(puzzle):
    carts = []
    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            if puzzle[y][x] in ['<', 'v', '>', '^']:
                carts.append(Cart([x, y], puzzle[y][x]))
    while 1 > 0:
        carts.sort(key=lambda c: c.position)
        position_list = []
        for cart in carts:
            position_list.append(cart.get_pos())
        to_delete = []
        for cart in range(len(carts)):
            carts[cart].move()
            pos = carts[cart].get_pos()
            if pos in position_list:
                pos_index = position_list.index(pos)
                to_delete.append(pos_index)
                to_delete.append(cart)
            position_list[cart] = pos
            if puzzle[pos[1]][pos[0]] in ['\\', '/']:
                carts[cart].turn(puzzle[pos[1]][pos[0]])
            elif puzzle[pos[1]][pos[0]] == '+':
                carts[cart].intersection()
            if len(carts) == 1:
                return position_list
            print(position_list)
        to_delete.sort(reverse=True)
        for item in to_delete:
            position_list.pop(item)
            carts.pop(item)

#45, 137 is wrong
print(part2(puzzle))