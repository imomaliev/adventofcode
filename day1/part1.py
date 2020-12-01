def __main__():
    expenses = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            curr = int(line)
            for expense in expenses:
                if curr + expense == 2020:
                    return curr * expense
            expenses.append(curr)
    return None


if __name__ == "__main__":
    print(__main__())
