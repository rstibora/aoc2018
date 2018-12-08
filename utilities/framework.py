def day_main(day_number, first_star_solver, secon_star_solver):
    with open("day{:02}/input.txt".format(day_number), "r") as input_file:
        input = input_file.readlines()
        print("\nSolution for day {0}".format(day_number))
        print("\tFirst star: {0}".format(first_star_solver(input)))
        print("\tSecond star: {0}".format(secon_star_solver(input)))