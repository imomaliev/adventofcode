"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)

byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""

import re
import sys
import pytest


def check_hgt(value):
    match = re.match(r"(\d+)(in|cm)", value)
    if match:
        length, unit = match[1], match[2]
        if (unit == "cm" and 150 <= int(length) <= 193) or (
            unit == "in" and 59 <= int(length) <= 76
        ):
            return True
    return False


def check_hcl(value):
    match = re.match(r"^#([a-f0-9]{6})$", value)
    if match:
        return True
    return False


def check_pid(value):
    match = re.match(r"^(\d{9})$", value)
    if match:
        return True
    return False


checks = {
    "byr": lambda value: 1920 <= int(value) <= 2002,
    "iyr": lambda value: 2010 <= int(value) <= 2020,
    "eyr": lambda value: 2020 <= int(value) <= 2030,
    "hgt": check_hgt,
    "hcl": check_hcl,
    "ecl": lambda value: value in set("amb blu brn gry grn hzl oth".split()),
    "pid": check_pid,
    "cid": lambda value: True,
}


def solve(input_s):
    valid = 0
    keys = set(
        [
            "byr",
            "iyr",
            "eyr",
            "hgt",
            "hcl",
            "ecl",
            "pid",
        ]
    )
    for parts in input_s.split("\n\n"):
        data = set()
        parts = parts.split()
        for part in parts:
            key, value = part.split(":")
            if checks[key](value):
                data.add(key)

        if data >= keys:
            valid += 1
    return valid


INPUT_S = """\
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

INPUT_S2 = """\
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
"""

INPUT_S3 = """\
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    (
        (INPUT_S, 2),
        (INPUT_S2, 0),
        (INPUT_S3, 4),
    ),
)
def test(input_s, expected):
    assert solve(input_s) == expected


def main():
    with open("input.txt") as f:
        print(solve(f.read()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
