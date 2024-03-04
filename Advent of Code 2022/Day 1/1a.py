def main():
    input: list[str] = open("Day 1\input.txt").read().split("\n\n")

    max_calorie: int = 0
    for item in input:
        val: int = 0
        for value in item.split("\n"):
            val += int(value)

        max_calorie = max(val, max_calorie)

    return max_calorie


if __name__ == "__main__":
    main()
