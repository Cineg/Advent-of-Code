def main() -> None:
    input: list[str] = open("Day 21 - Step Counter\input.txt").readlines()
    grid: list[list[str]] = convert_to_grid(input)
    start_pos: tuple[int, int] = find_start_position(grid)

    current_position_queue: list[tuple[int, int]] = [start_pos]
    new_queue: list[tuple[int, int]] = []
    steps: int = 0

    while steps < 64:
        while current_position_queue:
            row, col = current_position_queue[0]
            current_position_queue.pop(0)

            for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row: int = row + dir[0]
                new_col: int = col + dir[1]

                if (
                    new_row < 0
                    or new_row >= len(grid)
                    or new_col < 0
                    or new_col >= (len(grid[0]))
                ):
                    continue

                if grid[new_row][new_col] == "#":
                    continue

                if (new_row, new_col) not in new_queue:
                    new_queue.append((new_row, new_col))

        steps += 1
        current_position_queue = new_queue
        new_queue = []

    print(len(current_position_queue))


def convert_to_grid(input: list[str]) -> list[list[str]]:
    grid: list[list[str]] = []
    for line in input:
        row: list[str] = []
        for char in line:
            row.append(char)

        grid.append(row)

    return grid


def find_start_position(
    grid: list[list[str]], start_position_char: str = "S"
) -> tuple[int, int]:
    for row_index, row in enumerate(grid):
        for col_index, character in enumerate(row):
            if character == start_position_char:
                return (row_index, col_index)

    return (-1, -1)


if __name__ == "__main__":
    main()
