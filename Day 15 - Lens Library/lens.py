MULTIPLIER: int = 17
DIVIDER: int = 256


def main():
    input = open("Day 15 - Lens Library\input.txt").read().split(",")

    total: int = 0
    for item in input:
        item_total: int = 0
        for char in item:
            value: int = item_total
            value += ord(char)
            value *= MULTIPLIER
            value = value % DIVIDER
            item_total = value

        total += item_total

    print(total)


if __name__ == "__main__":
    main()
