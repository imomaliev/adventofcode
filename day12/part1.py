import sys
import pytest


def solve(input_s):
    current = 1
    directions = ("N", "E", "S", "W")
    man = {"N": 0, "E": 0, "S": 0, "W": 0}
    for line in input_s.splitlines():
        direction, num = line[0], line[1:]
        num = int(num)
        if direction == "F":
            man[directions[current]] += num
        elif direction in directions:
            man[direction] += num
        elif direction == "R":
            current = (current + num // 90) % 4
        elif direction == "L":
            current = (current - num // 90) % 4
    return abs(man["N"] - man["S"]) + abs(man["E"] - man["W"])


INPUT_S = """\
F10
N3
F7
R90
F11
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 25),),
)
def test(input_s, expected):
    assert solve(input_s) == expected


def main():
    with open("input.txt") as f:
        print(solve(f.read()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
