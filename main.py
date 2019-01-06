import argparse

from day01 import solution as day01_solution
from day02 import solution as day02_solution
from day03 import solution as day03_solution
from day04 import solution as day04_solution
from day05 import solution as day05_solution
from day06 import solution as day06_solution
from day07 import solution as day07_solution

def get_solution_for_day(day):
    if day == 1:
        return day01_solution.main
    elif day == 2:
        return day02_solution.main
    elif day == 3:
        return day03_solution.main
    elif day == 4:
        return day04_solution.main
    elif day == 5:
        return day05_solution.main
    elif day == 6:
        return day06_solution.main
    elif day == 7:
        return day07_solution.main
    else:
        raise Exception("Solution for day {0} does not exist".format(day))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Advent of Code 2018')
    parser.add_argument("-d", "--day", type=int, help="solve only for a specific day", default=None)
    # parser.add_argument("-i", "--input_file", type=string, help="use this file as an input for solver", default="input.txt")
    args = parser.parse_args()

    if args.day is not None:
        get_solution_for_day(args.day)()
    else:
        for day in range(1, 26):
            get_solution_for_day(day)()

