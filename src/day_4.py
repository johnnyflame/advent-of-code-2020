from aocd import get_data


def validate_header(
    passport_entry,
    required_fields={"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"},
):
    return set(passport_entry.keys()) == required_fields or required_fields.difference(
        passport_entry.keys()
    ) == {"cid"}


def create_record_collection(string_input):
    # parse the data in the string into a collection of dictionaries
    collection = []
    passport_entry = {}
    data = string_input.splitlines()
    for line in data:
        if line == "":
            collection.append(passport_entry)
            passport_entry = {}
            continue
        for entry in line.split():
            passport_entry[entry.split(":")[0]] = entry.split(":")[1]
    collection.append(passport_entry)
    return collection


def is_in_range(val, lower, upper):
    return lower <= val <= upper


def validate_content(passport_entry):
    for key, val in passport_entry.items():
        if key == "byr" and not is_in_range(int(val), lower=1920, upper=2002):
            return False
        elif key == "iyr" and not is_in_range(int(val), 2010, 2020):
            return False
        elif key == "eyr" and not is_in_range(int(val), 2020, 2030):
            return False
        elif key == "hgt":
            if len(val) < 2 or val[-2:] not in {"cm", "in"}:
                return False
            height, unit = int(val[:-2]), val[-2:]
            if unit == "cm":
                if not is_in_range(height, 150, 193):
                    return False
            elif unit == "in":
                if not is_in_range(height, 59, 76):
                    return False
            else:
                return False
        elif key == "hcl":
            header, content = val[0], val[1:]
            valid_set = {
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "a",
                "b",
                "c",
                "d",
                "e",
                "f",
            }
            if header != "#":
                return False
            if len(content) != 6 or set(content) - valid_set != set():
                return False
        elif key == "ecl":
            if val not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
                return False
        elif key == "pid":
            if len(val) != 9 or not val.isnumeric():
                return False
        else:
            continue

    return True


def count_valid_entries(string_input):
    records = create_record_collection(string_input)
    count = 0
    for record in records:
        if validate_header(record) and validate_content(record):
            count += 1
    return count


def test_valid_headers():
    input = """
    ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    byr:1937 iyr:2017 cid:147 hgt:183cm

    iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
    hcl:#cfa07d byr:1929

    hcl:#ae17e1 iyr:2013
    eyr:2024
    ecl:brn pid:760753108 byr:1931
    hgt:179cm

    hcl:#cfa07d eyr:2025 pid:166559648
    iyr:2011 ecl:brn hgt:59in
    """

    records = create_record_collection(input)
    validity = [validate_header(record) for record in records]

    assert validity.count(True) == 2


def test_all_invalid():
    input = """eyr:1972 cid:100
    hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

    iyr:2019
    hcl:#602927 eyr:1967 hgt:170cm
    ecl:grn pid:012533040 byr:1946

    hcl:dab227 iyr:2012
    ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

    hgt:59cm ecl:zzz
    eyr:2038 hcl:74454a iyr:2023
    pid:3556412378 byr:2007

    byr:2003
    """

    invalid_records = create_record_collection(input)
    validity = [validate_content(record) for record in invalid_records]

    assert not any(validity)


def test_all_valid():
    input = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
    hcl:#623a2f

    eyr:2029 ecl:blu cid:129 byr:1989
    iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

    hcl:#888785
    hgt:164cm byr:2001 iyr:2015 cid:88
    pid:545766238 ecl:hzl
    eyr:2022

    iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
    """

    valid_records = create_record_collection(input)
    validity = [validate_content(record) for record in valid_records]
    assert all(validity)


test_valid_headers()
test_all_invalid()
test_all_valid()


day_4_input = get_data(day=4)
print(f"Day 4's answer {count_valid_entries(day_4_input)}")
