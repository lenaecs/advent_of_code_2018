


def part1(puzzle, length, width):
    grid = []
    for y in range(length + 1):
        row = []
        for x in range(width + 1):
            rack_id = x + 10
            power_level = rack_id * y
            power_level += puzzle
            power_level = power_level * rack_id
            power_level = power_level // 10**2 % 10
            power_level -= 5
            row.append(power_level)
        grid.append(row)
    max_region = float('-inf')
    max_x = -1
    max_y = -1
    for y in range(1, length - 2):
        for x in range(1, width - 2):
            region_sum = 0
            for region_y in range(y, y + 3):
                for region_x in range(x, x + 3):
                    region_sum += grid[region_y][region_x]
            if region_sum > max_region:
                max_region = region_sum
                max_x = x
                max_y = y
    return max_x, max_y, max_region

print(part1(7689, 300, 300))

def part2(puzzle, length, width):
    grid = []
    for y in range(length + 1):
        row = []
        for x in range(width + 1):
            rack_id = x + 10
            power_level = rack_id * y
            power_level += puzzle
            power_level = power_level * rack_id
            power_level = power_level // 10**2 % 10
            power_level -= 5
            row.append(power_level)
        grid.append(row)
    max_region = float('-inf')
    max_x = -1
    max_y = -1
    max_size = 0
    for y in range(1, length + 1):
        for x in range(1, width + 1):
            region_sum = 0
            for size in range(min(width - x, length - y) + 1):
                for region_y in range(y, y + size):
                    region_sum += grid[region_y][x + size - 1]
                for region_x in range(x, x + size - 1):
                    region_sum += grid[y + size - 1][region_x]
                if region_sum > max_region:
                    max_region = region_sum
                    max_x = x
                    max_y = y
                    max_size = size
        print(y)
    return max_x, max_y, max_size, max_region

print(part2(7689, 300, 300))