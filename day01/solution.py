from utilities import list_utils, framework

def first_star(input):
    frequency_offsets = [int(x) for x in input]
    total_offset = 0
    for offset in frequency_offsets:
        total_offset += offset
    return total_offset

def second_star(input):
    frequency_offsets = [int(x) for x in input]
    infinite_list = list_utils.infinitize(frequency_offsets)
    seen_frequencies = set()
    total_offset = 0
    for offset in infinite_list:
        total_offset += offset
        if total_offset in seen_frequencies:
            return total_offset
        else:
            seen_frequencies.add(total_offset)

def main():
    return framework.day_main(1, first_star, second_star)
