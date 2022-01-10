import sys
import pytest


def solve(input_s):
    return NotImplementedError(input_s)


INPUT_S = """\
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, ...),),
)
def test(input_s, expected):
    assert solve(input_s) == expected


def main():
    with open("input.txt") as f:
        print(solve(f.read()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
