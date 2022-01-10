import sys
from collections import Counter
import pytest


def solve(input_s):
    res = 0
    for group in input_s.split("\n\n"):
        first, *rest = group.strip().split("\n")
        keys = set(first)
        for subgroup in rest:
            keys &= set(Counter(subgroup))
        res += len(keys)
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
    ((INPUT_S, 6),),
)
def test(input_s, expected):
    assert solve(input_s) == expected


def main():
    with open("input.txt") as f:
        print(solve(f.read()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
