from collections import Counter


def main():
    input: str = open("Advent of Code 2022\Day 6\input.txt").read()
    index: int = 0
    while index < len(input) - 4:
        cnt: Counter = Counter(input[index : index + 4])
        if len(cnt) == 4:
            print(index + 4)
            return
        index += 1


if __name__ == "__main__":
    main()
