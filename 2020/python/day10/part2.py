import sys
import pytest


def get_for_n(num):
    if num == 1:
        return 1
    if num == 2:
        return 2
    if num == 3:
        return 4
    return get_for_n(num - 1) + get_for_n(num - 2) + get_for_n(num - 3)


def solve(input_s):
    numbers = []
    for line in input_s.splitlines():
        num = int(line.strip())
        numbers.append(num)
    numbers = sorted(numbers)
    numbers.append(numbers[-1] + 3)
    diffs = []
    prev = 0
    for num in numbers:
        diffs.append(num - prev)
        prev = num
    res = 1
    counter = 0
    for diff in diffs:
        if diff == 1:
            counter += 1
        else:
            if counter:
                res *= get_for_n(counter)
            counter = 0
    return res


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
        (INPUT_S, 8),
        (INPUT_S2, 19208),
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
