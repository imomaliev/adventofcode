"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)

"""
def __main__():
    valid = 0
    with open("input.txt", "r") as f:
        data = set()
        keys = set([
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        'cid',
        ])
        keys2 = set([
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        ])
        ff = f.read()
        for parts in ff.split('\n\n'):
            data = set()
            parts = parts.split()
            for part in parts:
                key, value = part.split(':')
                data.add(key)
            if data >= keys2:
                valid += 1
        return valid

if __name__ == "__main__":
    print(__main__())

