from copy import deepcopy

NUMBER_OF_GENERATIONS = 20

def parse_inital_state(input):
    return [char for char in input[0].split()[2]]

def parse_rules(input):
    rules = []
    for line in input[2:]:
        rules.append(([char for char in line.split()[0]], line.split()[2]))
    return rules

def pad_with_empty(state):
    three_empty = [".", ".", "."]
    added = [0, 0]
    if state[:3] != three_empty:
        state = three_empty + state
        added[0] = 3
    if state[-3:] != three_empty:
        state = state + three_empty
        added[1] = 3
    return (state, added)

def apply_rules(state, rules):
    new_state = deepcopy(state)
    for idx in range(2, len(state) - 2):
        for rule in rules:
            if rule[0] == state[(idx - 2):(idx + 3)]:
                new_state[idx] = rule[1]
    return new_state

def first_star(input):
    rules = parse_rules(input)
    state = parse_inital_state(input)
    negative_pots = 0

    for _ in range(NUMBER_OF_GENERATIONS):
        state, added_pots = pad_with_empty(state)
        negative_pots += added_pots[0]
        state = apply_rules(state, rules)
    return sum([idx - negative_pots for idx in range(len(state)) if state[idx] == "#"])

def second_star(input):
    pass

