import sys
import pytest


def solve(input_s):
    expenses = []
    for line in input_s.splitlines():
        curr = int(line)
        for i, expense1 in enumerate(expenses):
            for j, expense2 in enumerate(expenses):
                if i != j:
                    if curr + expense1 + expense2 == 2020:
                        return curr * expense1 * expense2
        expenses.append(curr)
    return NotImplementedError


INPUT_S = """\
1721
979
366
299
675
1456
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 241861950),),
)
def test(input_s, expected):
    assert solve(input_s) == expected


def main():
    with open("input.txt") as f:
        print(solve(f.read()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
