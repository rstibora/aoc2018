def first_star(input):
    def parse_input(input):
        return int(input[0])

    score_board = [3, 7]
    current_recipes = [0, 1]
    recipes_created = 2
    num_required = parse_input(input) + 10
    while recipes_created < num_required:
        new_recipe = score_board[current_recipes[0]] + score_board[current_recipes[1]]
        score_board.append(int(str(new_recipe)[0]))
        recipes_created += 1
        if new_recipe >= 10:
            score_board.append(int(str(new_recipe)[1]))
            recipes_created += 1
        current_recipes[0] += score_board[current_recipes[0]] + 1
        current_recipes[0] %= len(score_board)
        current_recipes[1] += score_board[current_recipes[1]] + 1
        current_recipes[1] %= len(score_board)
    return "".join([str(x) for x in score_board[-10:]])
def second_star(input):
    pass
