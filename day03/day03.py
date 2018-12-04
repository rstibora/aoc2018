import re
import itertools


class Rectangle():
    def __init__(self, string_description):
        matches = re.search("#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)", string_description)
        self.left = int(matches.group(2))
        self.top = int(matches.group(3))
        self.width = int(matches.group(4))
        self.height = int(matches.group(5))

def first_star(input):
    claims = {}
    for line in input:
        rectangle = Rectangle(line)
        for x in range(rectangle.left, rectangle.left + rectangle.width):
            for y in range(rectangle.top, rectangle.top + rectangle.height):
                if (x, y) not in claims:
                    claims[(x, y)] = 1
                else:
                    claims[(x, y)] += 1
    return len([claim for claim in claims.values() if claim > 1])

def second_star(input):
    pass

def day_03():
    with open("day03/input.txt", "r") as input_file:
        input_data = input_file.readlines()
        print("Day 3")
        print("\tFirst star solution: {0}".format(first_star(input_data)))
        print("\tSecond star solution: {0}".format(second_star(input_data)))
        print()

if __name__ == "__main__":
    day_03()