def traverse(accum, index, steps):
    visited = []
    while index < len(steps):
        instr, num = steps[index]
        if (index, instr, num) in visited:
            break
        visited.append((index, instr, num))
        if instr == "acc":
            accum += num
            index += 1
        elif instr == "jmp":
            index += num
        elif instr == "nop":
            index += 1
            continue
    else:
        return accum
    return None


def __main__():
    with open("input.txt", "r") as f:
        steps = []
        accum = 0
        steps = []
        for line in f.readlines():
            instr, num = line.strip().split(" ")
            num = int(num)
            steps.append((instr, num))

        index = 0
        visited = []
        loop = []
        while True:
            instr, num = steps[index]
            if instr == "acc":
                accum += num
                index += 1
            elif instr == "jmp":
                res = traverse(accum, index + 1, steps)
                index += num
                if res is not None:
                    return res
            elif instr == "nop":
                res = traverse(accum, index + num, steps)
                index += 1
                if res is not None:
                    return res
                continue
    return accum


if __name__ == "__main__":
    print(__main__())
