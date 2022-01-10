import sys
import pytest


# https://github.com/sophiebits/adventofcode/blob/main/2020/day14.py
def occupy(pos, mask):
    if not mask:
        yield 0
    else:
        for m in occupy(pos // 2, mask[1:]):
            if mask[0] == "0":
                yield 2 * m + pos % 2
            elif mask[0] == "1":
                yield 2 * m + 1
            elif mask[0] == "X":
                yield 2 * m + 0
                yield 2 * m + 1


def solve(input_s):
    mask = ""
    bits = {}
    for line in input_s.splitlines():
        op, value = line.split(" = ")
        if op == "mask":
            mask = value
        elif "mem" in op:
            bit = op.replace("mem[", "").replace("]", "")
            for m in occupy(int(bit), list(reversed(mask))):
                bits[m] = int(value)
        else:
            return ValueError
    return sum(bits.values())


INPUT_S = """\
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 208),),
)
def test(input_s, expected):
    assert solve(input_s) == expected


def main():
    with open("input.txt") as f:
        print(solve(f.read()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
