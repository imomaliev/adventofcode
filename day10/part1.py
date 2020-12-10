from collections import Counter


def __main__():
    with open("input.txt", "r") as f:
        numbers = []
        for line in f.readlines():
            num = int(line.strip())
            numbers.append(num)
        numbers = sorted(numbers)
        counter = Counter()
        prev = 0
        counter[3] += 1
        for curr in numbers:
            counter[curr - prev] += 1
            prev = curr

        return counter[1] * counter[3]
    raise RuntimeError


if __name__ == "__main__":
    print(__main__())
