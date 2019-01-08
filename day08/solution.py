def parse_input(input):
    return [int(data) for data in input[0].split()]

def first_star(input):
    def sum_child_metadata(data_range):
        meta_length = data_range[1]
        header_length = 2
        num_of_children = data_range[0]

        total_sum = 0
        range_start = header_length
        for _ in range(num_of_children):
            child = sum_child_metadata(data_range[range_start:-meta_length])
            range_start += child[0]
            total_sum += child[1]
        total_sum += sum(data_range[range_start:(range_start+meta_length)])
        return (range_start + meta_length, total_sum)

    data = parse_input(input)
    return sum_child_metadata(data)[1]

def second_star(input):
    pass