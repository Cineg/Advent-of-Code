def main() -> None:
    input_path: str = "Advent of Code 2022\Day 14\\input.txt"
    grid: list[list[str]] = input_grid(input_path)
    min_column: int = _get_offset(input_path)[0]
    for i, letter in enumerate(grid[-1]):
        if grid[-1][i] == " ":
            grid[-1][i] = "_"

    sand_spawn: tuple[int, int] = (0, 500 - min_column)

    sand_out_of_bounds: bool = False
    while not sand_out_of_bounds:
        r, c = sand_spawn

        move_sand: bool = True
        while move_sand:
            r, c, move_sand = update_position(grid, r, c)
            if not move_sand:
                if (r, c) != (-1, -1):
                    grid[r][c] = "o"
                else:
                    sand_out_of_bounds = True

    total: int = 0
    for line in grid:
        for char in line:
            if char == "o":
                total += 1

    print(total)


def input_grid(input_path: str) -> list[list[str]]:
    input: list[str] = open(input_path).read().split("\n")
    min_column, max_column, last_row = _get_offset(input_path)
    grid: list[list[str]] = _create_grid(last_row, min_column, max_column)
    draw_rock(input, grid, min_column)

    return grid


def update_position(grid: list[list[str]], r: int, c: int) -> tuple[int, int, bool]:

    new_r: int = r + 1
    if new_r == -1 or new_r == len(grid) or c == -1 or c == len(grid[0]):
        return (-1, -1, False)

    if grid[new_r][c] == "_":
        return (-1, -1, False)

    if grid[new_r][c] == " ":
        grid[new_r][c] = "X"
        grid[new_r][c] = " "
        return (new_r, c, True)

    if grid[new_r][c] != " ":

        if grid[new_r][c - 1] == " ":
            grid[new_r][c - 1] = "X"
            grid[new_r][c - 1] = " "
            return (new_r, c - 1, True)
        elif grid[new_r][c + 1] == " ":
            grid[new_r][c + 1] = "X"
            grid[new_r][c + 1] = " "
            return (new_r, c + 1, True)
        else:
            if grid[new_r][c + 1] == "_" or grid[new_r][c - 1] == "_":
                return (-1, -1, False)
            return (r, c, False)


def out_of_bounds(grid: list[list[str]], r: int, c: int) -> bool:
    if len(grid[0]) - c == 0:
        return True

    if len(grid) - r == 0:
        return True

    return False


def draw_rock(input: list[str], grid: list[list[str]], column_offset: int) -> None:
    for line in input:
        moves: list[str] = line.split(" -> ")
        i: int = 0
        while i < len(moves) - 1:
            start_col, start_row = map(int, moves[i].split(","))
            end_col, end_row = map(int, moves[i + 1].split(","))

            if start_col - end_col != 0:
                start: int = start_col - column_offset
                end: int = end_col - column_offset
                for col in range(min(start, end), max(start, end) + 1):
                    grid[start_row][col] = "#"

            if start_row - end_row != 0:
                for row in range(min(start_row, end_row), max(start_row, end_row) + 1):
                    grid[row][start_col - column_offset] = "#"

            i += 1


def _get_offset(input_path: str) -> tuple[int, int, int]:
    input: list[str] = open(input_path).read().split("\n")
    """
    returns offset col
    [0] = minimum column
    [1] = maximum column
    [2] = last row
    """

    smallest_col: int = 9999
    largest_col: int = 0
    last_row: int = 0
    for line in input:
        moves: list[str] = line.split(" -> ")
        for move in moves:
            col, row = map(int, move.split(","))
            smallest_col = min(col, smallest_col)
            largest_col = max(col, largest_col)
            last_row = max(last_row, row)

    return smallest_col - 1, largest_col, last_row


def _create_grid(last_row: int, start_col: int, end_col: int) -> list[list[str]]:
    grid: list[list[str]] = []
    for row in range(last_row + 1):
        line: list[str] = []
        for _ in range(start_col, end_col + 2):
            line.append(" ")

        grid.append(line)
    return grid


if __name__ == "__main__":
    main()
