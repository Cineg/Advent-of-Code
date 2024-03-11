def main() -> None:
    input: list[str] = open("Advent of Code 2022\Day 9\\input.txt").read().split("\n")

    tail_seen: set = {(0, 0)}
    tail: list[int] = [0, 0]
    head: list[int] = [0, 0]

    for line in input:
        direction, moves = line.split(" ")
        for _ in range(int(moves)):
            r, c = head
            if direction == "R":
                head[0] += 1
            if direction == "L":
                head[0] -= 1
            if direction == "U":
                head[1] -= 1
            if direction == "D":
                head[1] += 1

            if move_tail(head, tail):
                tail = [r, c]
                if (r, c) not in tail_seen:
                    tail_seen.add((r, c))

    print(len(tail_seen))


def move_tail(head: list[int], tail: list[int]) -> bool:
    row: int = head[0] - tail[0]
    col: int = head[1] - tail[1]

    if abs(row) > 1 or abs(col) > 1:
        return True

    return False


if __name__ == "__main__":
    main()
