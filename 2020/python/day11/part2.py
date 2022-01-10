from copy import deepcopy
import sys
import pytest


def get_coords(i, j, area):  # pylint: disable=too-many-branches
    nmax, mmax = len(area), len(area[0])
    coords = []
    # top
    for k in range(i + 1, nmax):
        if area[k][j] != ".":
            coords.append((k, j))
            break
    # bot
    for k in range(i - 1, -1, -1):
        if area[k][j] != ".":
            coords.append((k, j))
            break
    # left
    for k in range(j + 1, mmax):
        if area[i][k] != ".":
            coords.append((i, k))
            break
    # right
    for k in range(j - 1, -1, -1):
        if area[i][k] != ".":
            coords.append((i, k))
            break
    # top right
    counter = 0
    for k in range(i + 1, nmax):
        if j + counter < mmax - 1:
            counter += 1
        else:
            break
        if area[k][j + counter] != ".":
            coords.append((k, j + counter))
            break
    # top left
    counter = 0
    for k in range(i + 1, nmax):
        if j + counter - 1 >= 0:
            counter -= 1
        else:
            break
        if area[k][j + counter] != ".":
            coords.append((k, j + counter))
            break
    # bot right
    counter = 0
    for k in range(i - 1, -1, -1):
        if j + counter < mmax - 1:
            counter += 1
        else:
            break
        if area[k][j + counter] != ".":
            coords.append((k, j + counter))
            break
    # bot left
    counter = 0
    for k in range(i - 1, -1, -1):
        if j + counter - 1 >= 0:
            counter -= 1
        else:
            break
        if area[k][j + counter] != ".":
            coords.append((k, j + counter))
            break

    return coords


def check_1(i, j, area):
    coords = get_coords(i, j, area)
    return all(area[i][j] != "#" for i, j in coords)


def check_2(i, j, area):
    coords = get_coords(i, j, area)
    return len(list(filter(None, [area[i][j] == "#" for i, j in coords]))) >= 5


def transform(area):
    new_area = deepcopy(area)
    for i, __ in enumerate(area):
        for j, __ in enumerate(area[0]):
            if area[i][j] == "L" and check_1(i, j, area):
                new_area[i][j] = "#"
            elif area[i][j] == "#" and check_2(i, j, area):
                new_area[i][j] = "L"
            else:
                new_area[i][j] = area[i][j]
    return new_area


def solve(input_s):
    area = []
    for row in input_s.splitlines():
        new_row = []
        area.append(new_row)
        for place in row:
            new_row.append(place)

    new_area = transform(area)
    while area != new_area:
        area = new_area
        new_area = transform(area)

    counter = 0
    for row in new_area:
        for place in row:
            if place == "#":
                counter += 1
    return counter


INPUT_S = """\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 26),),
)
def test(input_s, expected):
    assert solve(input_s) == expected


def main():
    with open("input.txt") as f:
        print(solve(f.read()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
