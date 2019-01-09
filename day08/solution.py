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
    def sum_child_metadata(data_range):
        # Calculate values of children nodes.
        range_start = 2
        children = []
        for _ in range(data_range[0]):
            children.append(sum_child_metadata(data_range[range_start:-data_range[1]]))
            range_start += children[-1][0]
        # Caclulate value of this node.
        total_sum = 0
        if not len(children):
            total_sum = sum(data_range[range_start:(range_start + data_range[1])])
        else:
            # To prevent off by one error since indices in meta data start from 1.
            meta_indices = map(lambda x: x - 1, data_range[range_start:(range_start + data_range[1])])
            for meta_idx in meta_indices:
                try:
                    total_sum += children[meta_idx][1]
                except:
                    pass
        return (range_start + data_range[1], total_sum)
    data = parse_input(input)
    return sum_child_metadata(data)[1]