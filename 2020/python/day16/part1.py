import sys
import pytest


def solve(input_s):
    rules = []

    rules_s, __, tickets_s = input_s.split("\n\n")
    for line in rules_s.splitlines():
        r1, r2 = line.split(": ", 1)[1].split(" or ")
        rules.append(
            (tuple(int(i) for i in r1.split("-")), tuple(int(i) for i in r2.split("-")))
        )

    numbers = []
    for line in tickets_s.replace("nearby tickets:\n", "").splitlines():
        check = {}
        for num in tuple(line.split(",")):
            num = int(num)
            check[num] = 0
            for rule in rules:
                if rule[0][0] <= num <= rule[0][1] or rule[1][0] <= num <= rule[1][1]:
                    check[num] += 1
        numbers.extend(k for k, v in check.items() if v == 0)
    return sum(numbers)


INPUT_S = """\
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 71),),
)
def test(input_s, expected):
    assert solve(input_s) == expected


def main():
    with open("input.txt") as f:
        print(solve(f.read()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
