import sys
import pytest


def solve(input_s):
    mask = ""
    bits = {}
    for line in input_s.splitlines():
        op, value = line.split(" = ")
        if op == "mask":
            mask = value
        elif "mem" in op:
            bit = op.replace("mem[", "").replace("]", "")
            value = list(format(int(value), "b").zfill(36))
            for index, b in enumerate(mask):
                if b != "X":
                    value[index] = b
            bits[bit] = int("".join(value), base=2)
        else:
            return ValueError
    return sum(bits.values())


INPUT_S = """\
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 165),),
)
def test(input_s, expected):
    assert solve(input_s) == expected


def main():
    with open("input.txt") as f:
        print(solve(f.read()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
