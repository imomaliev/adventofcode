import sys
import pytest


def count_slopes(right, down, mapp):
    i = 0
    counter = 0
    mod = len(mapp[0])
    while i < len(mapp) and i * down < len(mapp):
        r_index = i * right % mod
        if mapp[i * down][r_index] == "#":
            counter += 1
        i += 1
    return counter


def solve(input_s):
    mapp = []
    for line in input_s.splitlines():
        mapp.append(list(line.strip()))
    return (
        count_slopes(1, 1, mapp)
        * count_slopes(3, 1, mapp)
        * count_slopes(5, 1, mapp)
        * count_slopes(7, 1, mapp)
        * count_slopes(1, 2, mapp)
    )


INPUT_S = """\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 336),),
)
def test(input_s, expected):
    assert solve(input_s) == expected


def main():
    with open("input.txt") as f:
        print(solve(f.read()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
