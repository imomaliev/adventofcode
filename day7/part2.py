# light red bags contain 1 bright white bag, 2 muted yellow bags
from collections import defaultdict

def traverse(key, tree):
    if key not in tree:
        return 0
    count = 0
    for child, num in tree[key].items():
        count += num + num * traverse(child, tree)
    return count

def __main__():
    with open("input.txt", "r") as f:
        tree = defaultdict(dict)

        for line in f.readlines():
            line = line.strip()
            parent, children = line.split(' contain ')
            parent = parent.replace(' bags', '')
            if 'no other bags' not in children:
                for child in children.split(','):
                    num, child = child.strip().split(' ', 1)
                    child = child.replace(' bags', '').replace(' bag', '').replace('.', '')
                    tree[parent][child] = int(num)

        children = tree['shiny gold']
        count = 0
        for child, num in children.items():
            count += num + num * traverse(child, tree)
        return count


if __name__ == "__main__":
    print(__main__())


