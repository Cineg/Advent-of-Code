from collections import Counter


def main() -> None:
    input: list[str] = open("Advent of Code 2022\Day 3\input.txt").read().split("\n")

    result: int = 0
    for item in input:
        half: int = int(len(item) / 2)
        a: str = item[0:half]
        b: str = item[half : len(item)]

        count_a: Counter = Counter(a)
        seen: dict = {}
        for letter in b:
            if letter in count_a and letter not in seen:
                seen[letter] = ""

        for letter in seen:
            if letter.isupper():
                result += ord(letter.lower()) + 26 - 96
            else:
                result += ord(letter) - 96

    print(result)


if __name__ == "__main__":
    main()
