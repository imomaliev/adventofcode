import sys
import pytest


def solve(input_s):
    time, buses = input_s.splitlines()
    time = int(time)
    buses = {
        ((time // int(bus) + 1) * int(bus)) - time: int(bus)
        for bus in buses.split(",")
        if bus != "x"
    }
    bus = min(buses)
    return bus * buses[bus]


INPUT_S = """\
939
7,13,x,x,59,x,31,19
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 295),),
)
def test(input_s, expected):
    assert solve(input_s) == expected


def main():
    with open("input.txt") as f:
        print(solve(f.read()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
