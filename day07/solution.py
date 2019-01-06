from utilities import framework

def first_star(input):
    def parse_rules(input):
        rules = []
        for line in input:
            rule_pair = (line.split()[1], line.split()[7])
            rules.append(rule_pair)
        return rules

    def find_ready_steps(rules, done_steps):
        ready_steps = set()
        for rule in rules:
            ready_steps.add(rule[0])
            ready_steps.add(rule[1])
        for step in done_steps:
            ready_steps.remove(step)
        for rule in rules:
            if rule[0] not in done_steps and rule[1] in ready_steps:
                ready_steps.remove(rule[1])
        return ready_steps

    rules = parse_rules(input)
    done_steps = []
    ready_steps = find_ready_steps(rules, done_steps)
    while ready_steps:
        done_steps.append(min(ready_steps))
        ready_steps = find_ready_steps(rules, done_steps)
    return done_steps

def second_star(input):
    pass

def main():
    framework.day_main(7, first_star, second_star)