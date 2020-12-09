from itertools import combinations


def __main__():
    with open("input.txt", "r") as f:
        numbers = []
        sub = []
        for line in f.readlines():
            num = int(line.strip())
            numbers.append(num)
            if len(sub) < 25:
                sub.append(num)
            else:
                for i, j in combinations(sub, 2):
                    if i + j == num:
                        sub.pop(0)
                        sub.append(num)
                        break
                else:
                    return num


if __name__ == "__main__":
    print(__main__())

