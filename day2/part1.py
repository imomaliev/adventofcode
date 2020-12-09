from collections import Counter


def __main__():
    correct = 0
    with open("input.txt", "r") as f:
        for line in f.readlines():
            rule, password = line.split(": ")
            num, char = rule.split(" ")
            bot, top = [int(i) for i in num.split("-")]
            counter = Counter(password.strip())
            if bot <= counter[char] <= top:
                correct += 1
    return correct


if __name__ == "__main__":
    print(__main__())
