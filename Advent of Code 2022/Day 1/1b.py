import heapq


def main():
    input: list[str] = open("Advent of Code 2022\Day 1\input.txt").read().split("\n\n")

    items: list[int] = [0, 0, 0]
    for item in input:
        val: int = 0
        for value in item.split("\n"):
            val += int(value)

        heapq.heappushpop(items, val)

    print(sum(items))
    return sum(items)


if __name__ == "__main__":
    main()
