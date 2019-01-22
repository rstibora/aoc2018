from math import inf

def parse_serial_number(input):
    return int(input[0])

def first_star(input):
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

    def get_power_for_square(x, y, serial_number):
        power = 0
        for square_x in range(x, x + 3):
            for square_y in range(y, y + 3):
                power += get_power_for_cell(square_x, square_y, serial_number)
        return power

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
    pass