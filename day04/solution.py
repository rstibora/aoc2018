import datetime
import re

from collections import namedtuple
from operator import itemgetter, attrgetter

STATE_ASLEEP = "asleep"
STATE_AWAKE = "awake"

Record = namedtuple("Record", ["timestamp", "message"])

def get_sleep_data(records):
    """Returns a list of per-minute records of sleep data grouped by guard id and date."""
    def get_minutes(begin, end):
        """Get length of [begin, end] interval in minutes."""
        return (end - begin).seconds // 60

    records = sorted(records, key=attrgetter("message"))
    records.sort(key=attrgetter("timestamp"))

    guard_sleep = {}
    current_guard_id = None
    for idx, record in enumerate(records):
        date_only = datetime.date(record.timestamp.year, record.timestamp.month, record.timestamp.day)
        if record.message[:5] == "Guard":
            current_guard_id = int(re.search("#([0-9]+)", record.message).group(1))
            if current_guard_id not in guard_sleep:
                guard_sleep[current_guard_id] = {}
            guard_sleep[current_guard_id][date_only] = record.timestamp.minute * [STATE_AWAKE]
        elif record.message[:5] == "wakes":
            number_of_minutes = get_minutes(records[idx-1].timestamp, record.timestamp)
            guard_sleep[current_guard_id][date_only] += number_of_minutes * [STATE_ASLEEP]
        elif record.message[:5] == "falls":
            number_of_minutes = get_minutes(records[idx-1].timestamp, record.timestamp)
            guard_sleep[current_guard_id][date_only] += number_of_minutes * [STATE_AWAKE]
    return guard_sleep

def get_per_minute_sleep_data(sleep_data):
    """Returns a dictionary of per-minute total sleep (accross all days) data for each guard."""
    per_minute_sleep = {}
    for guard_id in sleep_data.keys():
        per_minute_sleep[guard_id] = 60 * [0]
        for sleep_in_day in sleep_data[guard_id].values():
            for minute, state in enumerate(sleep_in_day):
                if state == STATE_ASLEEP:
                    per_minute_sleep[guard_id][minute] += 1
    return per_minute_sleep

def parse_input(input):
    """Returns a list of sleep records."""
    parsed_input = []
    for line in input:
        time = datetime.datetime.strptime(line.split("] ")[0][1:], "%Y-%m-%d %H:%M")
        if time.hour != 0:
            time += datetime.timedelta(1)
            time = time.replace(hour=0, minute=0)
        message = line.split("] ")[1]
        parsed_input.append(Record(time, message))
    return parsed_input

def first_star(input):
    sleep_records = parse_input(input)
    guard_sleep = get_sleep_data(sleep_records)
    sleep_heatmap = get_per_minute_sleep_data(guard_sleep)
    total_guard_sleep = {guard_id: sum(sleep_heatmap[guard_id]) for guard_id in guard_sleep.keys()}

    guard_id_with_most_sleep = max(total_guard_sleep.items(), key=itemgetter(1))[0]
    most_sleepy_minute = sleep_heatmap[guard_id_with_most_sleep].index(max(sleep_heatmap[guard_id_with_most_sleep]))
    return guard_id_with_most_sleep * most_sleepy_minute

def second_star(input):
    sleep_records = parse_input(input)
    guard_sleep = get_sleep_data(sleep_records)
    sleep_heatmap = get_per_minute_sleep_data(guard_sleep)

    most_regular_minute_per_guard = {guard_id: max(enumerate(sleep_heatmap[guard_id]), key=itemgetter(1)) for guard_id in guard_sleep.keys()}
    most_regular_sleeper = max(most_regular_minute_per_guard.items(), key=lambda x: x[1][1])[0]
    most_regular_minute = most_regular_minute_per_guard[most_regular_sleeper][0]
    return most_regular_sleeper * most_regular_minute
