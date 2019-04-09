from itertools import cycle

def first_star(input):
    return sum(int(line) for line in input)

def second_star(input):
    seen_frequencies = set()
    total_offset = 0
    for offset in cycle(int(line) for line in input):
        total_offset += offset
        if total_offset in seen_frequencies:
            return total_offset
        seen_frequencies.add(total_offset)
