import sys
import pytest


def solve(input_s):
    seats = set()
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
        seats.add(count)
    seats = list(seats)
    prev = seats[0]
    for seat in seats[1:]:
        if seat - 1 != prev:
            return seat - 1
        prev = seat
    return NotImplementedError


INPUT_S = """\
FFFBBBFRLR
FFFBBBFRRL
FFFBBBFRRR
FFFBBBBLLR
FFFBBBBLRL
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 120),),
)
def test(input_s, expected):
    assert solve(input_s) == expected


def main():
    with open("input.txt") as f:
        print(solve(f.read()))
    return 0


if __name__ == "__main__":
    sys.exit(main())


def __main__():
    raise RuntimeError


if __name__ == "__main__":
    print(__main__())
