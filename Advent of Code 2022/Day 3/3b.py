from collections import Counter


def main() -> None:
    input: list[str] = open("Advent of Code 2022\Day 3\input.txt").read().split("\n")

    result: int = 0
    index: int = 0

    while index < len(input):
        elf1: str = input[index]
        elf2: str = input[index + 1]
        elf3: str = input[index + 2]

        seen: dict = {}

        for letter in elf1:
            if letter not in seen:
                seen[letter] = 1

        for letter in elf2:
            if letter in seen and seen[letter] == 1:
                seen[letter] = 2

        for letter in elf3:
            if letter in seen and seen[letter] == 2:
                seen[letter] = 3

        for letter in seen:
            if seen[letter] == 3:
                if letter.isupper():
                    result += ord(letter.lower()) + 26 - 96
                else:
                    result += ord(letter) - 96

        index += 3

    print(result)


if __name__ == "__main__":
    main()
