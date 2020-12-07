# light red bags contain 1 bright white bag, 2 muted yellow bags
from collections import defaultdict

def __main__():
    with open("input.txt", "r") as f:
        tree = defaultdict(list)
        for line in f.readlines():
            line = line.strip()
            parent, children = line.split(' contain ')
            parent = parent.replace(' bags', '')
            if 'no other bags' not in children:
                for child in children.split(','):
                    num, child = child.strip().split(' ', 1)
                    child = child.replace(' bags', '').replace(' bag', '').replace('.', '')
                    tree[child].append(parent)



        count = 0
        parents = tree['shiny gold']
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


if __name__ == "__main__":
    print(__main__())


