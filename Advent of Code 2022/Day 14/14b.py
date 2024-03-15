def main() -> None:
    input_path: str = "Advent of Code 2022\Day 14\\input.txt"
    floor: int = _get_floor(input_path)
    walls: set[tuple[int, int]] = create_walls_set(input_path)
    seen: set[tuple[int, int]] = {(-1, -1)}
    sand_spawn: tuple[int, int] = (0, 500)

    sand_out_of_bounds: bool = False
    while not sand_out_of_bounds:
        r, c = sand_spawn

        move_sand: bool = True
        while move_sand:
            r, c, move_sand = update_position(walls, seen, floor, r, c)
            if not move_sand:
                if (r, c) != (-1, -1):
                    seen.add((r, c))
                else:
                    sand_out_of_bounds = True

    print(len(seen))


def create_walls_set(input_path: str) -> set[tuple[int, int]]:
    input: list[str] = open(input_path).read().split("\n")
    rocks: set[tuple[int, int]] = get_rocks(input)
    return rocks


def update_position(
    walls: set[tuple[int, int]], seen: set[tuple[int, int]], floor: int, r: int, c: int
) -> tuple[int, int, bool]:
    new_r: int = r + 1
    if new_r == floor:
        return (r, c, False)

    if (new_r, c) not in seen and (new_r, c) not in walls:
        return (new_r, c, True)

    if (new_r, c) in seen or (new_r, c) in walls:
        if (new_r, c - 1) not in seen and (new_r, c - 1) not in walls:
            return (new_r, c - 1, True)
        if (new_r, c + 1) not in seen and (new_r, c + 1) not in walls:
            return (new_r, c + 1, True)

    if (1, 500) in seen and (1, 499) in seen and (1, 501) in seen:
        return (-1, -1, False)
    return (r, c, False)


def get_rocks(input: list[str]) -> set[tuple[int, int]]:
    rocks_set: set = {(-1, -1)}

    for line in input:
        moves: list[str] = line.split(" -> ")
        i: int = 0
        while i < len(moves) - 1:
            start_col, start_row = map(int, moves[i].split(","))
            end_col, end_row = map(int, moves[i + 1].split(","))

            if start_col - end_col != 0:
                start: int = start_col
                end: int = end_col
                for col in range(min(start, end), max(start, end) + 1):
                    rocks_set.add((start_row, col))

            if start_row - end_row != 0:
                for row in range(min(start_row, end_row), max(start_row, end_row) + 1):
                    rocks_set.add((row, start_col))

            i += 1

    rocks_set.remove((-1, -1))
    return rocks_set


def _get_floor(input_path: str) -> int:
    input: list[str] = open(input_path).read().split("\n")

    last_row: int = 0
    for line in input:
        moves: list[str] = line.split(" -> ")
        for move in moves:
            row: int = int(move.split(",")[1])
            last_row = max(last_row, row + 2)

    return last_row


if __name__ == "__main__":
    main()
