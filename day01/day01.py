from utilities import list_utils

def first_star(frequency_offsets):
    total_offset = 0
    for offset in frequency_offsets:
        total_offset += offset
    return total_offset

def second_star(frequency_offsets):
    infinite_list = list_utils.InfiniteList(frequency_offsets)
    seen_frequencies = set()
    total_offset = 0
    for offset in infinite_list:
        total_offset += offset
        if total_offset in seen_frequencies:
            return total_offset
        else:
            seen_frequencies.add(total_offset)

def day_01():
    with open("day01/input.txt", "r") as input_file:
        frequency_offsets = [int(x) for x in input_file]
        print("First star solution: {0}".format(first_star(frequency_offsets)))
        print("Second star solution: {0}".format(second_star(frequency_offsets)))
