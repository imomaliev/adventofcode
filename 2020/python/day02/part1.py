import sys
from collections import Counter
import pytest


def solve(input_s):
    correct = 0
    for line in input_s.splitlines():
        rule, password = line.split(": ")
        num, char = rule.split(" ")
        bot, top = [int(i) for i in num.split("-")]
        counter = Counter(password.strip())
        if bot <= counter[char] <= top:
            correct += 1
    return correct


INPUT_S = """\
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 2),),
)
def test(input_s, expected):
    assert solve(input_s) == expected


def main():
    with open("input.txt") as f:
        print(solve(f.read()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
