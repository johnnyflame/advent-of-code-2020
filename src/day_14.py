import itertools

from aocd import get_data


def apply_bit_mask(mask, number):
    """
    Takes a 36-bit bitmask and applies a to a value
    """
    print(f"applying bitmask {mask} to number: {number}")

    bin_number = list(format(number, "036b"))
    for i, bit in enumerate(mask):
        if bit == "X":
            continue
        bin_number[i] = bit

    return int("".join(bin_number), 2)


def apply_bit_mask_version_two(mask, number):
    bin_number = list(format(number, "036b"))
    for i, bit in enumerate(mask):
        if bit == "1" or bit == "X":
            bin_number[i] = bit

    output = []
    total_number_of_floats = itertools.product((0, 1), repeat=bin_number.count("X"))
    for item in total_number_of_floats:
        values = list(item)
        new_bin_number = [x for x in bin_number]
        for i, bit in enumerate(new_bin_number):
            if bit == "X":
                new_bin_number[i] = str(values.pop())
        output.append(new_bin_number)
    return [int("".join(bin_number), 2) for bin_number in output]


def decode(data, version=1):
    # use a dict to store the addresses
    mem_address = {}
    current_bit_mask = None
    for line in data.splitlines():
        if line[:4] == "mask":
            current_bit_mask = line.split()[2]
        elif line[:3] == "mem":
            key = int(line.split()[0][4:-1])
            original_value = int(line.split()[-1])
            if version == 1:
                mem_address[key] = apply_bit_mask(current_bit_mask, original_value)
            else:
                mem_addresses_to_update = apply_bit_mask_version_two(
                    current_bit_mask, key
                )
                for address in mem_addresses_to_update:
                    mem_address[address] = original_value
        else:
            raise ValueError("Input needs to be either mask or a mem address of values")
    return sum(mem_address.values())


# print(f"part 1: {decode(get_data(day=14))}")


print(f"part 2: {decode(get_data(day=14),version=2)}")
