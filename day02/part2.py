def __main__():
    correct = 0
    with open("input.txt", "r") as f:
        for line in f.readlines():
            rule, password = line.split(": ")
            num, char = rule.split(" ")
            bot, top = [int(i) - 1 for i in num.split("-")]
            password = password.strip()
            if (password[top] == char and password[bot] != char) or (
                password[bot] == char and password[top] != char
            ):
                correct += 1
    return correct


if __name__ == "__main__":
    print(__main__())
