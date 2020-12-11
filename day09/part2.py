import sys
import pytest


def solve(input_s, cnum=14144619):
    numbers = []
    sub = []
    for line in input_s.splitlines():
        num = int(line.strip())
        numbers.append(num)

    start, end = 0, 2
    while end < len(numbers):
        sub = numbers[start:end]
        if sum(sub) == cnum:
            return min(sub) + max(sub)
        elif sum(sub) < cnum:
            end += 1
        else:
            start += 1
    raise NotImplementedError


INPUT_S = """\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 62),),
)
def test(input_s, expected):
    assert solve(input_s, 127) == expected


def main():
    with open("input.txt") as f:
        print(solve(f.read()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
