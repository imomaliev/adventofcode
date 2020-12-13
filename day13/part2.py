import sys
import pytest


def crt(pairs):
    """https://en.wikipedia.org/wiki/Chinese_remainder_theorem"""
    M = 1
    for x, mx in pairs:
        M *= mx
    total = 0
    for x, mx in pairs:
        breakpoint()
        b = M // mx
        total += x * b * pow(b, mx - 2, mx)
        total %= M
    return total


def solve(input_s):
    __, buses_s = input_s.splitlines()
    pairs = []
    for i, n in enumerate(buses_s.split(",")):
        if n == "x":
            continue
        n = int(n)
        pairs.append((n - i, n))
    return crt(pairs)


def solve_slow(input_s):  # pylint: disable=too-many-locals,too-many-branches
    __, buses_s = input_s.splitlines()
    counter = 0
    buses = {}
    all_buses = buses_s.split(",")
    n = len(all_buses) - 1
    for bus in all_buses:
        if bus == "x":
            counter += 1
        else:
            buses[int(bus)] = counter
            counter = 0
    k = 1
    buses = list(buses.items())
    mbus = max(buses, key=lambda i: i[0])
    first = buses[0][0]
    last = buses[-1][0]
    k = (mbus[0] // first) + 1
    while True:
        step = first * k
        if (step + n) % last == 0:
            break
        k += 1
    k = 1
    while True:
        two = step * 2 + k
        if two % first == 0 and (two + n) % last == 0:
            break
        k += 1
    substep = two % step
    dk = two // step - 1
    k = 1 + dk
    while True:
        if dk == 1:
            earliest = curr = step * k + substep * (k - 1)
        else:
            earliest = curr = step * k + substep * (k // dk)
        for bus, diff in buses[1:]:
            curr += diff + 1
            if curr % bus != 0:
                break
        else:
            return earliest
        k += dk

    return buses


INPUT_S = """\
939
7,13,x,x,59,x,31,19
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    (
        (INPUT_S, 1068781),
        ("\n17,x,13,19", 3417),
        ("\n67,7,59,61", 754018),
        ("\n67,x,7,59,61", 779210),
        ("\n67,7,x,59,61", 1261476),
        ("\n1789,37,47,1889", 1202161486),
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
