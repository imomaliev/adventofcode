import sys
from collections import defaultdict
import pytest


def solve(input_s):
    tree = defaultdict(list)
    for line in input_s.splitlines():
        line = line.strip()
        parent, children = line.split(" contain ")
        parent = parent.replace(" bags", "")
        if "no other bags" not in children:
            for child in children.split(","):
                num, child = child.strip().split(" ", 1)
                child = child.replace(" bags", "").replace(" bag", "").replace(".", "")
                tree[child].append(parent)

    count = 0
    parents = tree["shiny gold"]
    visited = []
    while parents:
        parent = parents.pop()
        if parent not in visited:
            count += 1
            visited.append(parent)
            for sparent in tree[parent]:
                if sparent not in visited:
                    parents.append(sparent)

    return count


INPUT_S = """\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 4),),
)
def test(input_s, expected):
    assert solve(input_s) == expected


def main():
    with open("input.txt") as f:
        print(solve(f.read()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
