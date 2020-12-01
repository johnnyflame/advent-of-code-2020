import argparse


class ArgParser(argparse.ArgumentParser):
    def __init__(self, **kwargs):
        # full_help = kwargs.pop("description").strip()
        # kwargs["description"], kwargs["epilog"] = full_help.split("\n\n", 1)
        super().__init__(**kwargs)

    def add_simple_option(self, name, type=None, default=None, help=None):
        help_text = str(help)
        if default is not None:
            help_text += f" (default {default})"
        return self.add_argument(
            f"--{name}",
            dest=name.replace("-", "_"),
            type=type,
            default=default,
            help=help_text,
        )


parser = ArgParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
)

parser.add_argument(
    "input",
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


if __name__ == "__main__":
    input_file = cfg.input
    input_values = []
    with open(input_file) as file:
        for line in file:
            input_values.append(int(line))

    num_1, num_2 = two_sum(input_values, 2020)
    print(num_1 * num_2)
