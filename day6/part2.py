from collections import Counter


def __main__():
    with open("input.txt", "r") as f:
        ff = f.read()
        counter = Counter()
        res = 0
        for group in ff.split("\n\n"):
            first, *rest = group.split("\n")
            keys = set(first)
            for subgroup in rest:
                keys &= set(Counter(subgroup))
            res += len(keys)
        return res


if __name__ == "__main__":
    print(__main__())
