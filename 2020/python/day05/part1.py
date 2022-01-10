import sys
import pytest


def solve(input_s):
    maxseat = 0
    for line in input_s.splitlines():
        boarding_pass = line.strip()
        row, seat = boarding_pass[:7], boarding_pass[7:]
        count = 0
        for i, char in enumerate(reversed(row)):
            if char == "B":
                count += 2 ** i
        count *= 8
        for i, char in enumerate(reversed(seat)):
            if char == "R":
                count += 2 ** i
        if count > maxseat:
            maxseat = count
    return maxseat


INPUT_S = """\
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 820),),
)
def test(input_s, expected):
    assert solve(input_s) == expected


def main():
    with open("input.txt") as f:
        print(solve(f.read()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
