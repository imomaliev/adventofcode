NUM = 14144619


def __main__():
    with open("input.txt", "r") as f:
        numbers = []
        sub = []
        for line in f.readlines():
            num = int(line.strip())
            numbers.append(num)

        start, end = 0, 2
        while end < len(numbers):
            sub = numbers[start:end]
            if sum(sub) == NUM:
                return min(sub) + max(sub)
            elif sum(sub) < NUM:
                end += 1
            else:
                start += 1


if __name__ == "__main__":
    print(__main__())
