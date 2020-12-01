def __main__():
    expenses = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            curr = int(line)
            for i1, expense1 in enumerate(expenses):
                for i2, expense2 in enumerate(expenses):
                    if i1 != i2:
                        if curr + expense1 + expense2 == 2020:
                            return curr * expense1 * expense2
            expenses.append(curr)
    return None


if __name__ == "__main__":
    print(__main__())
