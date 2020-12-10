import sys
import pytest


def solve(input_s):
    correct = 0
    for line in input_s.splitlines():
        rule, password = line.split(": ")
        num, char = rule.split(" ")
        bot, top = [int(i) - 1 for i in num.split("-")]
        password = password.strip()
        if (password[top] == char and password[bot] != char) or (
            password[bot] == char and password[top] != char
        ):
            correct += 1
    return correct


INPUT_S = """\
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 1),),
)
def test(input_s, expected):
    assert solve(input_s) == expected


def main():
    with open("input.txt") as f:
        print(solve(f.read()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
