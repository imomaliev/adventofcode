from collections import Counter


def __main__():
    with open("input.txt", "r") as f:
        input_file = f.read()
        counter = Counter()
        res = 0
        for group in input_file.split("\n\n"):
            group = group.replace("\n", "")
            counter = Counter(group)
            res += len(counter.keys())
        return res


if __name__ == "__main__":
    print(__main__())
