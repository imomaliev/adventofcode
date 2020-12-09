def __main__():
    with open("input.txt", "r") as f:
        mapp = []
        for line in f.readlines():
            mapp.append(list(line.strip()))
        right = 3
        down = 1
        i = 0
        counter = 0
        mod = len(mapp[0])
        while i < len(mapp):
            r = i * right % mod
            if mapp[i * down][r] == "#":
                counter += 1
            i += 1

    return counter


if __name__ == "__main__":
    print(__main__())
