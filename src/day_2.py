from collections import Counter

from aocd import get_data


def check(s):
    # parse string and do some preprocessing
    occurance_range, val, data = s.split(" ")
    occurance_range = [int(x) for x in occurance_range.split("-")]
    data = data.rstrip()
    val = val.strip(":")

    lower, upper = occurance_range
    occurance_count = Counter(data)
    if lower <= occurance_count[val] <= upper:
        return True

    return False


def check_rule_2(s):
    # parse string and do some preprocessing
    occurance_range, target, data = s.split(" ")
    occurance_range = [int(x) for x in occurance_range.split("-")]
    data = data.strip("\n")
    target = target.strip(":")

    lower, upper = occurance_range
    # offset for zero index
    lower -= 1
    upper -= 1
    return data[lower] != data[upper] and (
        data[lower] == target or data[upper] == target
    )


def validate_passwords(input_data, line_validator):
    output = 0
    for line in input_data.splitlines():
        if line_validator(line):
            output += 1
    return output


data = get_data(day=2)
print(validate_passwords(data, check))
print(validate_passwords(data, check_rule_2))
