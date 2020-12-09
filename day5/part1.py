def __main__():
    maxseat = 0
    with open("input.txt", "r") as f:
        for line in f.readlines():
            boarding_pass = line.strip()
            row, seat = boarding_pass[:7], boarding_pass[7:]
            count = 0
            for i, char in enumerate(reversed(row)):
                if char == "B":
                    count += 2 ** i
            count *= 8
            for i, char in enumerate(reversed(seat)):
                if char == "R":
                    count += 2 ** i
            if count > maxseat:
                maxseat = count
    return maxseat


if __name__ == "__main__":
    print(__main__())
