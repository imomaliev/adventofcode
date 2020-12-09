from itertools import combinations


def __main__():
    with open("input.txt", "r") as f:
        numbers = []
        sub = []
        NUM = num = 14144619
        for line in f.readlines():
            num = int(line.strip())
            numbers.append(num)

        checked = set()
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

