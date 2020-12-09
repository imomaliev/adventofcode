def __main__():
    seats = set()
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
            seats.add(count)
    seats = list(seats)
    prev = seats[0]
    for seat in seats[1:]:
        if seat - 1 != prev:
            return seat - 1
        prev = seat


if __name__ == "__main__":
    print(__main__())
