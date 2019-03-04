def parse_input(input):
    return int(input[0])

def generate_recipes(score_board, current_recipes):
    recipes_generated = 1
    new_recipe = score_board[current_recipes[0]] + score_board[current_recipes[1]]
    score_board.append(int(str(new_recipe)[0]))
    if new_recipe >= 10:
        score_board.append(int(str(new_recipe)[1]))
        recipes_generated = 2
    for elf in range(2):
        current_recipes[elf] += score_board[current_recipes[elf]] + 1
        current_recipes[elf] %= len(score_board)
    return recipes_generated

def first_star(input):
    score_board = [3, 7]
    current_recipes = [0, 1]
    recipes_created = 2
    num_required = parse_input(input) + 10
    while recipes_created < num_required:
        recipes_created += generate_recipes(score_board, current_recipes)
    return "".join([str(x) for x in score_board[-10:]])

def second_star(input):
    score_board = [3, 7]
    current_recipes = [0, 1]
    pattern = [int(x) for x in str(parse_input(input))]
    pattern_length = len(pattern)
    while score_board[-pattern_length:] != pattern:
        generate_recipes(score_board, current_recipes)
    return len(score_board) - len(pattern)
