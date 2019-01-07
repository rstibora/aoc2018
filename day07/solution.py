def parse_rules(input):
    rules = []
    for line in input:
        rule_pair = (line.split()[1], line.split()[7])
        rules.append(rule_pair)
    return rules

def find_ready_steps(rules, done_steps, in_progress_steps=[]):
    ready_steps = set()
    for rule in rules:
        ready_steps.add(rule[0])
        ready_steps.add(rule[1])
    for step in done_steps + in_progress_steps:
        ready_steps.remove(step)
    for rule in rules:
        if rule[0] not in done_steps and rule[1] in ready_steps:
            ready_steps.remove(rule[1])
    return ready_steps

def first_star(input):
    rules = parse_rules(input)
    done_steps = []
    ready_steps = find_ready_steps(rules, done_steps)
    while ready_steps:
        done_steps.append(min(ready_steps))
        ready_steps = find_ready_steps(rules, done_steps)
    return "".join(done_steps)

def second_star(input):
    def convert_step_to_duration(step):
        return 60 + ord(step.lower()[0]) - 96

    rules = parse_rules(input)
    done_steps = []
    time_elapsed = 0
    ready_steps = find_ready_steps(rules, done_steps)
    steps_in_progress = []
    while ready_steps or steps_in_progress:
        # Split the work among free workers.
        while len(steps_in_progress) < 5 and ready_steps:
            next_step = min(ready_steps)
            steps_in_progress.append([next_step, convert_step_to_duration(next_step)])
            ready_steps.remove(next_step)
        # Elapse time until some step is finished.
        timespan = min(steps_in_progress, key=lambda x: x[1])[1]
        for step_data in steps_in_progress:
            step_data[1] -= timespan
            if step_data[1] == 0:
                done_steps.append(step_data[0])
        steps_in_progress = [step for step in steps_in_progress if step[1] > 0]
        ready_steps = find_ready_steps(rules, done_steps, [step[0] for step in steps_in_progress])
        time_elapsed += timespan

    return time_elapsed
