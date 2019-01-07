def first_star(ids):
    def count_chars(id):
        counts = {}
        for char in id:
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1
        return counts

    def exactly_n_same(char_counts, n):
        for count in char_counts.values():
            if count == n:
                return True
        return False

    exactly_two_same = 0
    exactly_three_same = 0

    for id in ids:
        char_counts = count_chars(id)
        if exactly_n_same(char_counts, 2):
            exactly_two_same += 1
        if exactly_n_same(char_counts, 3):
            exactly_three_same += 1
    return exactly_two_same * exactly_three_same

def second_star(ids):
    def compare_ids(id_a, id_b):
        num_diffs = 0
        same_string = []
        for (char_a, char_b) in zip(id_a, id_b):
            if char_a == char_b:
                same_string.append(char_a)
            else:
                num_diffs += 1
        return (num_diffs, same_string)

    for id_a in ids:
        for id_b in ids:
            num_diffs, same_string = compare_ids(id_a, id_b)
            if num_diffs == 1:
                return "".join(same_string)
