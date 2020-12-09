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


def check_hgt(value):
    match = re.match(r"(\d+)(in|cm)", value)
    if match:
        length, unit = match[1], match[2]
        if (unit == "cm" and 150 <= int(length) <= 193) or (
            unit == "in" and 59 <= int(length) <= 76
        ):
            return True
    raise RuntimeError


def check_hcl(value):
    match = re.match(r"^#([a-f0-9]{6})$", value)
    if match:
        return True
    raise RuntimeError


def check_pid(value):
    match = re.match(r"^(\d{9})$", value)
    if match:
        return True
    raise RuntimeError


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


def __main__():
    valid = 0
    with open("input.txt", "r") as f:
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
        input_file = f.read()
        for parts in input_file.split("\n\n"):
            data = set()
            parts = parts.split()
            for part in parts:
                key, value = part.split(":")
                if checks[key](value):
                    data.add(key)

            if data >= keys:
                valid += 1
        return valid


if __name__ == "__main__":
    print(__main__())
