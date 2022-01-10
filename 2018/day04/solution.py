from datetime import datetime
import numpy as np
import parse


def get_input():
    notes = []
    matcher = '[{year:d}-{month:d}-{day:d} {hour:d}:{minute:d}] {text}'
    with open('input') as file:
        puzzle_input = file.read().splitlines()
    for line in puzzle_input:
        r = parse.parse(matcher, line)
        # Create datetime object
        date_time = datetime(r['year'], r['month'], r['day'], r['hour'], r['minute'])
        # Add pair in list - datetime and text
        notes.append([(date_time, r['text'])])
    # Sort list by chronological
    notes.sort(key=lambda entry: entry[0])
    return notes


def part01(notes):
    # Matcher for finding guard id
    matcher = 'Guard #{id:d} begins shift'
    # Initialize guards dictionary
    guards = {}
    # Create guard activity information
    for note in notes:
        date_time, text = note[0]
        # Find if we have new shift information
        if 'begins shift' in text:
            guard_id = parse.parse(matcher, text)['id']
            # Add guard if not present
            if guard_id not in guards:
                # Add guard
                guards[guard_id] = np.zeros((365, 60), dtype=np.int)
        else:
            day_of_year = date_time.timetuple().tm_yday
            guards[guard_id][day_of_year - 1, date_time.minute:] = int('falls asleep' in text)
    id_of_max, max_sleep_hours = 0, 0
    for guard_id, schedule in guards.items():
        sleep_hours = schedule.sum()
        if max_sleep_hours < sleep_hours:
            id_of_max = guard_id
            max_sleep_hours = sleep_hours
    print(id_of_max)
    sum_every_minute = guards[id_of_max].sum(axis=0)
    minute_with_max = np.argmax(sum_every_minute)
    print(minute_with_max)
    print(id_of_max * minute_with_max)

def part02(notes):
    # Matcher for finding guard id
    matcher = 'Guard #{id:d} begins shift'
    # Initialize guards dictionary
    guards = {}
    # Create guard activity information
    for note in notes:
        date_time, text = note[0]
        # Find if we have new shift information
        if 'begins shift' in text:
            guard_id = parse.parse(matcher, text)['id']
            # Add guard if not present
            if guard_id not in guards:
                # Add guard
                guards[guard_id] = np.zeros((365, 60), dtype=np.int)
        else:
            day_of_year = date_time.timetuple().tm_yday
            guards[guard_id][day_of_year - 1, date_time.minute:] = int('falls asleep' in text)
    id_of_max, same_minute_max, that_minute = 0, 0, 0
    for guard_id, schedule in guards.items():
        sum_every_minute = schedule.sum(axis=0)
        loc_same_minute_max = np.argmax(sum_every_minute)
        if sum_every_minute[loc_same_minute_max] > same_minute_max:
            id_of_max = guard_id
            same_minute_max = sum_every_minute[loc_same_minute_max]
            that_minute = loc_same_minute_max
    print(id_of_max * that_minute)


if __name__ == '__main__':
    notes = get_input()
    part01(notes)
    part02(notes)