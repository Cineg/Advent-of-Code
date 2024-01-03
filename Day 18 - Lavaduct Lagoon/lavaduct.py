def main():
    input = open("Day 18 - Lavaduct Lagoon\input.txt").read().splitlines()

    grid_dimensions = get_grid_dimensions(input)
    grid_y, grid_x, start_y, start_x = grid_dimensions
    grid: list[list[str]] = create_grid((grid_y, grid_x))

    fill_grid(grid, input, (start_y, start_x))

    print(count_grid(grid))


def get_grid_dimensions(input: list[str]) -> tuple[int, int, int, int]:
    grid_x: int = 0
    grid_y: int = 0

    peak_x: int = 0
    peak_y: int = 0

    minimum_x: int = 0
    minimum_y: int = 0

    for line in input:
        direction, moves, _ = line.split()

        if direction == "R":
            grid_x += int(moves)

        if direction == "L":
            grid_x -= int(moves)

        if direction == "U":
            grid_y -= int(moves)
        if direction == "D":
            grid_y += int(moves)

        peak_x = max(peak_x, grid_x)
        peak_y = max(peak_y, grid_y)

        minimum_x = min(minimum_x, grid_x)
        minimum_y = min(minimum_y, grid_y)

    return (
        -minimum_y + peak_y + 1,
        -minimum_x + peak_x + 1,
        abs(minimum_y),
        abs(minimum_x),
    )


def create_grid(dimensions: tuple[int, int]) -> list[list[str]]:
    grid: list[list[str]] = []
    for _ in range(0, dimensions[0]):
        row: list[str] = []
        for __ in range(0, dimensions[1]):
            row.append(" ")

        grid.append(row)

    return grid


def fill_grid(grid: list[list[str]], input: list[str], start_pos: tuple[int, int]):
    current_x = start_pos[1]
    current_y = start_pos[0]

    for line in input:
        direction, moves, color = line.split()

        next_x = current_x
        next_y = current_y

        if direction == "R":
            next_x += int(moves)
        if direction == "L":
            next_x -= int(moves)

        if direction == "D":
            next_y += int(moves)
        if direction == "U":
            next_y -= int(moves)

        for col in range(min(current_x, next_x), max(current_x, next_x) + 1):
            grid[current_y][col] = "#"

        for row in range(min(current_y, next_y), max(current_y, next_y) + 1):
            grid[row][current_x] = "#"

        current_x = next_x
        current_y = next_y


def count_grid(grid: list[list[str]]):
    count: int = 0
    for row, line in enumerate(grid):
        in_bounds: bool = False

        for col, value in enumerate(line):
            if not in_bounds and value == "#":
                in_bounds = True
            elif in_bounds and value == "#":
                if col + 1 < len(grid[0]) and col - 1 >= 0:
                    if grid[row][col + 1] != "#" and grid[row][col - 1] != "#":
                        in_bounds = False
                        count += 1

            if in_bounds:
                count += 1

    return count


if __name__ == "__main__":
    main()
