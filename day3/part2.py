def count_slopes(right, down, mapp):
    i = 0
    counter = 0
    mod = len(mapp[0])
    while i < len(mapp) and i*down < len(mapp):
        r = i * right % mod
        try:
            if mapp[i * down][r] == '#':
                counter +=1 
        except:
            breakpoint()
        i += 1
    return counter


def __main__():
    with open("input.txt", "r") as f:
        mapp = []
        for line in f.readlines():
            mapp.append(list(line.strip()))
        right = 3
        down = 1
        return count_slopes(1, 1, mapp) * 173 * count_slopes(5, 1, mapp) * count_slopes(7, 1, mapp) * count_slopes(1, 2, mapp)


if __name__ == "__main__":
    print(__main__())
