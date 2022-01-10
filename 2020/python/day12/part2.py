import sys
import pytest


def solve(input_s):
    directions = ("N", "E", "S", "W")
    directions_map = dict(zip(("N", "E", "S", "W"), range(4)))
    waypoint = {"N": 1, "E": 10, "S": 0, "W": 0}
    man = {"N": 0, "E": 0, "S": 0, "W": 0}
    for line in input_s.splitlines():
        direction, num = line[0], line[1:]
        num = int(num)
        if direction in directions:
            waypoint[direction] += num
        elif direction == "F":
            for d, value in waypoint.items():
                man[d] += value * num
        elif direction == "R":
            diff = num // 90
            rotated = {}
            for d, value in waypoint.items():
                rotated[directions[(directions_map[d] + diff) % 4]] = value
            waypoint = rotated
        elif direction == "L":
            diff = num // 90
            rotated = {}
            for d, value in waypoint.items():
                rotated[directions[(directions_map[d] - diff) % 4]] = value
            waypoint = rotated
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
    ((INPUT_S, 286),),
)
def test(input_s, expected):
    assert solve(input_s) == expected


def main():
    with open("input.txt") as f:
        print(solve(f.read()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
