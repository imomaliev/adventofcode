import sys
import pytest


def traverse(accum, index, steps):
    visited = []
    while index < len(steps):
        instr, num = steps[index]
        if (index, instr, num) in visited:
            break
        visited.append((index, instr, num))
        if instr == "acc":
            accum += num
            index += 1
        elif instr == "jmp":
            index += num
        elif instr == "nop":
            index += 1
            continue
    else:
        return accum
    return None


def solve(input_s):
    steps = []
    accum = 0
    steps = []
    for line in input_s.splitlines():
        instr, num = line.strip().split(" ")
        num = int(num)
        steps.append((instr, num))

    index = 0
    while True:
        instr, num = steps[index]
        if instr == "acc":
            accum += num
            index += 1
        elif instr == "jmp":
            res = traverse(accum, index + 1, steps)
            index += num
            if res is not None:
                return res
        elif instr == "nop":
            res = traverse(accum, index + num, steps)
            index += 1
            if res is not None:
                return res
            continue
    return accum


INPUT_S = """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 8),),
)
def test(input_s, expected):
    assert solve(input_s) == expected


def main():
    with open("input.txt") as f:
        print(solve(f.read()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
