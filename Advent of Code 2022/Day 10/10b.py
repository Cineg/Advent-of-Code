def main() -> None:
    input: list[str] = open("Advent of Code 2022\Day 10\\input.txt").read().split("\n")
    q: list[tuple] = create_queue(input)
    matrix: list[list[str]] = create_matrix()

    index: int = 0
    value: int = 1

    while q:
        val, time = q.pop(0)

        if index % 40 in [value - 1, value, value + 1]:
            row: int = int(index / 40)
            col: int = index % 40

            matrix[row][col] = "#"

        index += 1

        time -= 1

        if time == 0:
            value += val
        else:
            q.insert(0, (val, time))

    for r in matrix:
        print("".join(r))


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


def create_matrix() -> list[list[str]]:
    matrix: list[list[str]] = []
    for _ in range(6):
        row: list[str] = []
        for __ in range(40):
            row.append(".")

        matrix.append(row)
    return matrix


if __name__ == "__main__":
    main()
