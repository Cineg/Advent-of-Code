def main() -> None:
    input: list[str] = open("Advent of Code 2022\Day 9\\input.txt").read().split("\n")

    tail_seen: set = {(0, 0)}
    rope: list[list[int]] = create_rope()

    for line in input:
        direction, moves = line.split(" ")
        for _ in range(int(moves)):
            head: list[int] = rope[0]

            if direction == "R":
                head[0] += 1
            if direction == "L":
                head[0] -= 1
            if direction == "U":
                head[1] -= 1
            if direction == "D":
                head[1] += 1

            index: int = 0
            while True:
                if index == len(rope) - 1:
                    break

                mr, mc = move(rope[index], rope[index + 1])
                rope[index + 1][0] += mr
                rope[index + 1][1] += mc

                tail_seen.add(tuple(rope[-1]))
                index += 1

    print(len(tail_seen))


def move(head: list[int], tail: list[int]) -> tuple[int, int]:
    row: int = head[0] - tail[0]
    col: int = head[1] - tail[1]

    if abs(row) > 1 or abs(col) > 1:
        if row == 0:
            return (0, col // 2)
        if col == 0:
            return (row // 2, col)

        if row > 0:
            row = 1
        else:
            row = -1

        if col > 0:
            col = 1
        else:
            col = -1

        return (row, col)

    return (0, 0)


def create_rope(rope_len: int = 10) -> list[list[int]]:
    rope: list = []
    for _ in range(rope_len):
        knot: list[int] = [0, 0]
        rope.append(knot)

    return rope


if __name__ == "__main__":
    main()
