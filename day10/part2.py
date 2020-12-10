# pylint: disable=too-few-public-methods


def get_for_n(num):
    if num == 1:
        return 1
    if num == 2:
        return 2
    if num == 3:
        return 4
    return get_for_n(num - 1) + get_for_n(num - 2) + get_for_n(num - 3)


def __main__():
    with open("input.txt", "r") as f:
        numbers = []
        for line in f.readlines():
            num = int(line.strip())
            numbers.append(num)
        numbers = sorted(numbers)
        numbers.append(numbers[-1] + 3)
        diffs = []
        prev = 0
        for num in numbers:
            diffs.append(num - prev)
            prev = num
        res = 1
        counter = 0
        for diff in diffs:
            if diff == 1:
                counter += 1
            else:
                if counter:
                    res *= get_for_n(counter)
                counter = 0
        return res
    raise RuntimeError


if __name__ == "__main__":
    print(__main__())
