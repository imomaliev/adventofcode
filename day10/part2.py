# pylint: disable=too-few-public-methods
class Node:
    def __init__(self, val, left, mid=None, right=None):
        self.val = val
        self.left = left
        self.mid = mid
        self.right = right

    def __repr__(self):
        return f"<Node({self.val})>"


def fill_tree(node, index, numbers):
    if index >= len(numbers):
        return
    node.left = Node(numbers[index], None, None, None)
    fill_tree(node.left, index + 1, numbers)
    if numbers[index] - node.val < 3:
        if (
            (index + 2 < len(numbers))
            and (numbers[index + 1] - node.val <= 3)
            and (numbers[index + 2] - numbers[index + 1] <= 3)
        ):
            node.mid = Node(numbers[index + 1], None, None, None)
            fill_tree(node.mid, index + 2, numbers)

        if (index + 3 < len(numbers)) and (numbers[index + 2] - node.val <= 3):
            node.right = Node(numbers[index + 3], None, None, None)
            fill_tree(node.right, index + 4, numbers)
    return


def __main__():
    with open("input2.txt", "r") as f:
        numbers = []
        for line in f.readlines():
            num = int(line.strip())
            numbers.append(num)
        numbers = sorted(numbers)
        numbers.append(numbers[-1] + 3)
        root = curr = Node(0, None, None, None)
        fill_tree(root, 0, numbers)
        nodes = [curr]
        counter = 0
        while nodes:
            node = nodes.pop(0)
            if node.left:
                nodes.append(node.left)
            if node.mid:
                nodes.append(node.mid)
            if node.right:
                nodes.append(node.right)
            if node.left is None and node.mid is None and node.right is None:
                counter += 1
        return counter
    raise RuntimeError


if __name__ == "__main__":
    print(__main__())
