def parse_input(input):
    return [int(data) for data in input[0].split()]

def first_star(input):
    def sum_child_metadata(data_range):
        total_sum = 0
        range_start = 2
        for _ in range(data_range[0]):
            child = sum_child_metadata(data_range[range_start:-data_range[1]])
            range_start += child[0]
            total_sum += child[1]
        total_sum += sum(data_range[range_start:(range_start+data_range[1])])
        return (range_start + data_range[1], total_sum)

    data = parse_input(input)
    return sum_child_metadata(data)[1]

def second_star(input):
    pass