import argparse
from collections import Counter

parser = argparse.ArgumentParser()

parser.add_argument(
    "input_file",
    help="input file to the program",
)

cfg = parser.parse_args()


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
    occurance_range, val, data = s.split(" ")
    occurance_range = [int(x) for x in occurance_range.split("-")]
    data = data.strip("\n")
    val = val.strip(":")

    lower, upper = occurance_range
    # offset for zero index
    lower -= 1
    upper -= 1
    return data[lower] != data[upper] and (data[lower] == val or data[upper] == val)

    # if data[lower] == val or data[upper] == val:
    #     return data[lower] != data[upper]


def validate_passwords(input_file, line_validator):
    output = 0
    with open(input_file) as file:
        for line in file:
            if line_validator(line):
                output += 1
    return output


# print(validate_passwords(cfg.input_file, check))
print(validate_passwords(cfg.input_file, check_rule_2))
