import sys
from itertools import combinations
import pytest


def solve(input_s, preamble=25):
    numbers = []
    sub = []
    for line in input_s.splitlines():
        num = int(line.strip())
        numbers.append(num)
        if len(sub) < preamble:
            sub.append(num)
        else:
            for i, j in combinations(sub, 2):
                if i + j == num:
                    sub.pop(0)
                    sub.append(num)
                    break
            else:
                return num
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
    ((INPUT_S, 127),),
)
def test(input_s, expected):
    assert solve(input_s, 5) == expected


def main():
    with open("input.txt") as f:
        print(solve(f.read()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
