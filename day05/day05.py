import string

def reduce_polymer(polymer):
    def valid_reduction_pair(a, b):
        if a.lower() == b and a == b.upper():
            return True
        elif b.lower() == a and b == a.upper():
            return True
        else:
            return False

    def one_pass_reduce(input):
        if len(input) == 1:
            return input
        for idx, _ in enumerate(input[:-1]):
            if valid_reduction_pair(input[idx], input[idx + 1]):
                input[idx] = "_"
                input[idx+1] = "_"
        return [poly for poly in input if poly != "_"]

    current_length = None
    while current_length != len(polymer):
        current_length = len(polymer)
        polymer = one_pass_reduce(polymer)
    return polymer

def filter_out_unit(target_unit, polymer):
    target_unit = target_unit.lower()
    return [unit for unit in polymer if unit.lower() != target_unit]

def first_star(input):
    polymer = [char for char in input]
    return len(reduce_polymer(polymer))

def second_star(input):
    polymer = [char for char in input]
    lengths = []
    for char in string.ascii_lowercase:
        filtered_polymer = filter_out_unit(char, polymer)
        lengths.append((char, len(reduce_polymer(filtered_polymer))))
    return sorted(lengths, key=lambda x: x[1])[0][1]

def day_05():
    with open("day05/input.txt", "r") as input_file:
        input_data = input_file.readline()[:-1]
        print("Day 5")
        print("\tFirst star solution: {0}".format(first_star(input_data)))
        print("\tSecond star solution: {0}".format(second_star(input_data)))
        print()

if __name__ == "__main__":
    day_05()