import sys
import pytest


def solve(input_s, limit):
    numbers = {}
    last = -1
    counter = 0
    for index, num in enumerate(input_s.strip().split(","), 1):
        num = int(num)
        numbers[num] = [index]
        last = num
        counter = index

    while counter < limit:
        counter += 1
        if last in numbers and len(numbers[last]) == 2:
            last = numbers[last][1] - numbers[last][0]
        else:
            last = 0
        try:
            numbers[last] = [numbers[last][-1], counter]
        except KeyError:
            numbers[last] = [counter]
    return last


@pytest.mark.parametrize(
    ("input_s", "limit", "expected"),
    (
        ("0,3,6", 4, 0),
        ("0,3,6", 5, 3),
        ("0,3,6", 6, 3),
        ("0,3,6", 7, 1),
        ("0,3,6", 8, 0),
        ("0,3,6", 9, 4),
        ("0,3,6", 10, 0),
        ("0,3,6", 2020, 436),
        ("1,3,2", 2020, 1),
        ("2,1,3", 2020, 10),
        ("1,2,3", 2020, 27),
        ("2,3,1", 2020, 78),
        ("3,2,1", 2020, 438),
        ("3,1,2", 2020, 1836),
        ("0,3,6", 30000000, 175594),
        ("0,3,6", 30000000, 2578),
        ("1,3,2", 30000000, 3544142),
        ("2,1,3", 30000000, 261214),
        ("1,2,3", 30000000, 6895259),
        ("2,3,1", 30000000, 18),
        ("3,2,1", 30000000, 362),
    ),
)
def test(input_s, limit, expected):
    assert solve(input_s, limit) == expected


def main():
    with open("input.txt") as f:
        print(solve(f.read(), 30000000))
    return 0


if __name__ == "__main__":
    sys.exit(main())
