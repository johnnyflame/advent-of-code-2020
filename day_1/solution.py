import argparse


class ArgParser(argparse.ArgumentParser):
    def __init__(self, **kwargs):
        # full_help = kwargs.pop("description").strip()
        # kwargs["description"], kwargs["epilog"] = full_help.split("\n\n", 1)
        super().__init__(**kwargs)


parser = ArgParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
)

parser.add_argument(
    "input_file",
    help="input file to the program",
)

cfg = parser.parse_args()


def two_sum(input, target_sum):
    lookup = set()
    for val in input:
        if target_sum - val in lookup:
            return val, target_sum - val
        else:
            lookup.add(val)
    return None


def three_sum(input, target_sum):
    input = set(input)
    for val in input:
        new_target_sum = target_sum - val
        lookup = set()
        for other in input - {val}:
            if new_target_sum - other in lookup:
                return val, other, new_target_sum - other
            else:
                lookup.add(other)
    return None


def read_input(input_file):
    output = []
    with open(input_file) as file:
        for line in file:
            output.append(int(line))
    return output


if __name__ == "__main__":
    input_values = read_input(cfg.input_file)

    num_1, num_2 = two_sum(input_values, 2020)
    print(num_1 * num_2)

    num_1, num_2, num_3 = three_sum(input_values, 2020)
    print(num_1 * num_2 * num_3)
