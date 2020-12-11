import sys
from collections import Counter
import pytest


def solve(input_s):
    counter = Counter()
    res = 0
    for group in input_s.split("\n\n"):
        group = group.replace("\n", "")
        counter = Counter(group)
        res += len(counter.keys())
    return res


INPUT_S = """\
abc

a
b
c

ab
ac

a
a
a
a

b
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 11),),
)
def test(input_s, expected):
    assert solve(input_s) == expected


def main():
    with open("input.txt") as f:
        print(solve(f.read()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
