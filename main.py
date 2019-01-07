import argparse
import importlib

def day_main(day_number, input, first_star_solver, secon_star_solver):
    with open("day{:02}/{input}".format(day_number, input=input), "r") as input_file:
        input = input_file.readlines()
        print("\nSolution for day {0}".format(day_number))
        print("\tFirst star: {0}".format(first_star_solver(input)))
        print("\tSecond star: {0}".format(secon_star_solver(input)))

def get_solution_for_day(day, input_file):
    solution = importlib.import_module("day{:02}.solution".format(day))
    day_main(day, input_file, solution.first_star, solution.second_star)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Advent of Code 2018')
    parser.add_argument("-d", "--day", type=int, help="solve only for a specific day", default=None)
    parser.add_argument("-i", "--input_file", help="use this file as an input for solver", default="input.txt")
    args = parser.parse_args()

    if args.day is not None:
        get_solution_for_day(args.day, args.input_file)
    else:
        for day in range(1, 26):
            get_solution_for_day(day, args.input_file)

