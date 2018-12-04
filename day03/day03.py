import re
import itertools

class Claim():
    def __init__(self, string_description):
        matches = re.search("#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)", string_description)
        self.id = int(matches.group(1))
        self.left = int(matches.group(2))
        self.top = int(matches.group(3))
        self.width = int(matches.group(4))
        self.height = int(matches.group(5))

def collect_claims(string_inputs):
    claims = {}
    for line in string_inputs:
        claim = Claim(line)
        for x in range(claim.left, claim.left + claim.width):
            for y in range(claim.top, claim.top + claim.height):
                if (x, y) not in claims:
                    claims[(x, y)] = set([claim.id])
                else:
                    claims[(x, y)].add(claim.id)
    return claims

def first_star(input):
    claims = collect_claims(input)
    return len([claim for claim in claims.values() if len(claim) > 1])

def second_star(input):
    claims = collect_claims(input)
    claim_ids = set(range(1, len(input)+1))
    for claim in claims.values():
        if len(claim) > 1:
            claim_ids -= claim
    return claim_ids.pop()

def day_03():
    with open("day03/input.txt", "r") as input_file:
        input_data = input_file.readlines()
        print("Day 3")
        print("\tFirst star solution: {0}".format(first_star(input_data)))
        print("\tSecond star solution: {0}".format(second_star(input_data)))
        print()

if __name__ == "__main__":
    day_03()