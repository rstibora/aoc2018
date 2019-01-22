from math import inf

def parse_serial_number(input):
    return int(input[0])

def get_power_for_cell(x, y, serial_number):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id
    as_string = str(power_level)
    if len(as_string) >= 3:
        power_level = int(as_string[len(as_string) - 3])
    else:
        power_level = 0
    power_level -= 5
    return power_level

def get_power_for_square(x, y, serial_number, size = 3, cache = None):
    if cache is not None:
        if (size, x, y) in cache:
            return cache[(size, x, y)]
    power = 0
    if size == 1:
        power = get_power_for_cell(x, y, serial_number)
    else:
        power = get_power_for_square(x, y, serial_number, size // 2, cache)
        power += get_power_for_square(x + size // 2, y, serial_number, size // 2, cache)
        power += get_power_for_square(x, y + size // 2, serial_number, size // 2, cache)
        if size % 2 == 0:
            power += get_power_for_square(x + size // 2, y + size // 2, serial_number, size // 2, cache)
        else:
            power += get_power_for_square(x + size // 2, y + size // 2, serial_number, (size + 1) // 2, cache)
            power += sum([get_power_for_square(line_idx, y + size - 1, serial_number, 1, cache) for line_idx in range(x, x + size // 2)])
            power += sum([get_power_for_square(x + size - 1, column_idx, serial_number, 1, cache) for column_idx in range(y, y + size // 2)])
    if cache is not None:
        cache[(size, x, y)] = power
    return power

def first_star(input):
    serial_number = parse_serial_number(input)
    maximum_power = -inf
    maximum_coords = None
    for x in range(1, 299):
        for y in range(1, 299):
            power = get_power_for_square(x, y, serial_number)
            if power > maximum_power:
                maximum_power = power
                maximum_coords = (x, y)
    return "{0},{1}".format(maximum_coords[0], maximum_coords[1])

def second_star(input):
    # TODO: slow.
    serial_number = parse_serial_number(input)
    cache = {}
    maximum_power = -inf
    maximum_square = (None, None)
    for size in range(1, 301):
        for x in range(1, 301 - size):
            for y in range(1, 301 - size):
                power = get_power_for_square(x, y, serial_number, size, cache)
                if power > maximum_power:
                    maximum_power = power
                    maximum_square = ((x, y), size)
    return "{0},{1},{2}".format(maximum_square[0][0], maximum_square[0][1], maximum_square[1])