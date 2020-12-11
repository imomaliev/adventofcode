import sys
from collections import Counter
import pytest


def solve(input_s):
    numbers = []
    for line in input_s.splitlines():
        num = int(line.strip())
        numbers.append(num)
    numbers = sorted(numbers)
    counter = Counter()
    prev = 0
    counter[3] += 1
    for curr in numbers:
        counter[curr - prev] += 1
        prev = curr

    return counter[1] * counter[3]


INPUT_S = """\
16
10
15
5
1
11
7
19
6
12
4
"""


INPUT_S2 = """\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    (
        (INPUT_S, 35),
        (INPUT_S2, 220),
    ),
)
def test(input_s, expected):
    assert solve(input_s) == expected


def main():
    with open("input.txt") as f:
        print(solve(f.read()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
