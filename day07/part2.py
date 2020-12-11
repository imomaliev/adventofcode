import sys
from collections import defaultdict
import pytest


def traverse(key, tree):
    if key not in tree:
        return 0
    count = 0
    for child, num in tree[key].items():
        count += num + num * traverse(child, tree)
    return count


def solve(input_s):
    tree = defaultdict(dict)

    for line in input_s.splitlines():
        line = line.strip()
        parent, children = line.split(" contain ")
        parent = parent.replace(" bags", "")
        if "no other bags" not in children:
            for child in children.split(","):
                num, child = child.strip().split(" ", 1)
                child = child.replace(" bags", "").replace(" bag", "").replace(".", "")
                tree[parent][child] = int(num)

    children = tree["shiny gold"]
    count = 0
    for child, num in children.items():
        count += num + num * traverse(child, tree)
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


INPUT_S2 = """\
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 32), (INPUT_S2, 126)),
)
def test(input_s, expected):
    assert solve(input_s) == expected


def main():
    with open("input.txt") as f:
        print(solve(f.read()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
