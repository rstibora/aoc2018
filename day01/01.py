class InfiniteList():
    def __init__(self, non_infinite_list):
        self.list = non_infinite_list

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index == len(self.list):
            self.index = 0
        output = self.list[self.index]
        self.index += 1
        return output

def first_star(frequency_offsets):
    total_offset = 0
    for offset in frequency_offsets:
        total_offset += offset
    return total_offset

def second_star(frequency_offsets):
    infinite_list = InfiniteList(frequency_offsets)
    seen_frequencies = set()
    total_offset = 0
    for offset in infinite_list:
        total_offset += offset
        if total_offset in seen_frequencies:
            return total_offset
        else:
            seen_frequencies.add(total_offset)

def main():
    with open("day01/input.txt", "r") as input_file:
        frequency_offsets = [int(x) for x in input_file]
        print("First star solution: {0}".format(first_star(frequency_offsets)))
        print("Second star solution: {0}".format(second_star(frequency_offsets)))

if __name__ == "__main__":
    main()