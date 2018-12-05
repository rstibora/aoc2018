import datetime
import re

def first_star(input):
    def get_minutes(begin, end):
        return (end - begin).seconds // 60

    messages = get_chronological(input)
    guard_sleep = {}
    current_guard_id = None
    for idx, message in enumerate(messages):
        timestamp = message[0]
        action = message[1]
        date_only = datetime.date(timestamp.year, timestamp.month, timestamp.day)
        if action[:5] == "Guard":
            current_guard_id = int(re.search("#([0-9]+)", action).group(1))
            if current_guard_id not in guard_sleep:
                guard_sleep[current_guard_id] = {}
            guard_sleep[current_guard_id][date_only] = timestamp.minute * ["awake"]
        elif action[:5] == "wakes":
            number_of_minutes = get_minutes(messages[idx-1][0], timestamp)
            guard_sleep[current_guard_id][date_only] += number_of_minutes * ["asleep"]
        elif action[:5] == "falls":
            number_of_minutes = get_minutes(messages[idx-1][0], timestamp)
            guard_sleep[current_guard_id][date_only] += number_of_minutes * ["awake"]

    total_guard_sleep = {}
    for guard_id, sleep_data in guard_sleep.items():
        for data in sleep_data.values():
            minutes_of_sleep = len([state for state in data if state == "asleep"])
            if data[:-1] == "asleep":
                minutes_of_sleep += 60 - len(data)
            if not guard_id in total_guard_sleep:
                total_guard_sleep[guard_id] = 0
            total_guard_sleep[guard_id] += minutes_of_sleep

    guard_id_with_most_sleep = sorted(list(total_guard_sleep.items()), key=(lambda x: x[1]), reverse=True)[0][0]
    sleep_heatmap = 60 * [0]
    for sleep_in_day in guard_sleep[guard_id_with_most_sleep].values():
        for minute, state in enumerate(sleep_in_day):
            if state == "asleep":
                sleep_heatmap[minute] += 1
    most_sleepy_minute = sleep_heatmap.index(max(sleep_heatmap))

    return guard_id_with_most_sleep * most_sleepy_minute

def second_star(input):
    pass

def get_chronological(input):
    parsed_input = []
    for line in input:
        time = datetime.datetime.strptime(line.split("] ")[0][1:], "%Y-%m-%d %H:%M")
        if time.hour != 0:
            time += datetime.timedelta(1)
            time = time.replace(hour=0, minute=0)
        message = line.split("] ")[1]
        parsed_input.append((time, message))
    parsed_input.sort(key=(lambda x: x[1]))
    parsed_input.sort(key=(lambda x: x[0]))
    return parsed_input

def day_04():
    with open("day04/input.txt", "r") as input_file:
        input_data = input_file.readlines()
        print("Day 4")
        print("\tFirst star solution: {0}".format(first_star(input_data)))
        print("\tSecond star solution: {0}".format(second_star(input_data)))
        print()

if __name__ == "__main__":
    day_04()