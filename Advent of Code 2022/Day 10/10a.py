def main() -> None:
    input: list[str] = open("Advent of Code 2022\Day 10\\input.txt").read().split("\n")
    q: list[tuple] = create_queue(input)
    index: int = 0
    value: int = 1

    ticks: list[int] = []
    tick_list: list[int] = [20, 60, 100, 140, 180, 220]

    while q:
        val, time = q.pop(0)

        for item in tick_list:
            if index < item <= index + time:
                ticks.append(value * item)

        index += time
        value += val

    print(sum(ticks))


def create_queue(input: list[str]) -> list[tuple]:
    q: list = []
    for item in input:
        try:
            val: int = int(item.split(" ")[1])
            time: int = 2
        except:
            val, time = 0, 1

        q.append((val, time))

    return q


if __name__ == "__main__":
    main()
