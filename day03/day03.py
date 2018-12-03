import re
import itertools

class Claim():
    def __init__(self, string_description):
        matches = re.search("#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)", string_description)
        self.id = int(matches.group(1))
        self.rectangle = Rectangle(int(matches.group(2)), int(matches.group(3)), int(matches.group(4)), int(matches.group(5)))

class Rectangle():
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

def first_star(input):
    def claim_overlap(claim_a, claim_b):
        if claim_a.id == claim_b.id:
            return None

        leftmost_claim = claim_a if claim_a.rectangle.left < claim_b.rectangle.left else claim_b
        rightmost_claim = claim_a if claim_a.id != leftmost_claim.id else claim_b
        horizontal_intersection = max(leftmost_claim.rectangle.left + leftmost_claim.rectangle.width - rightmost_claim.rectangle.left, 0)

        topmost_claim = claim_a if claim_a.rectangle.top < claim_b.rectangle.top else claim_b
        bottommost_claim = claim_a if claim_a.id != topmost_claim.id else claim_b
        vertical_intersection = max(topmost_claim.rectangle.top + topmost_claim.rectangle.height - bottommost_claim.rectangle.top, 0)

        if horizontal_intersection * vertical_intersection > 0:
            return Rectangle(rightmost_claim.rectangle.left, bottommost_claim.rectangle.top, horizontal_intersection, vertical_intersection)
        else:
            return None

    claims = []
    for line in input:
        claims.append(Claim(line))

    overlaps = set()
    possible_overlaps = itertools.permutations(claims, 2)
    for possible_overlap in possible_overlaps:
        overlap = claim_overlap(possible_overlap[0], possible_overlap[1])
        if not overlap:
            continue
        for x in range(overlap.left, overlap.left + overlap.width):
            for y in range(overlap.top, overlap.top + overlap.height):
                overlaps.add((x, y))
    return len(overlaps)

def second_star(input):
    pass

def day_03():
    with open("day03/test_input.txt", "r") as input_file:
        input_data = input_file.readlines()
        print("Day 3")
        print("\tFirst star solution: {0}".format(first_star(input_data)))
        print("\tSecond star solution: {0}".format(second_star(input_data)))
        print()

if __name__ == "__main__":
    day_03()