from collections import Counter


def main():
    input = open("Day 18 - Lavaduct Lagoon\input.txt").read().splitlines()

    grid_dimensions = get_grid_dimensions(input)
    grid_y, grid_x, start_y, start_x = grid_dimensions
    grid: list[list[str]] = create_grid((grid_y, grid_x))

    fill_grid(grid, input, (start_y, start_x))

    fill_interior(grid, start_y - 1, start_x)

    # with open(
    #     "E:\Programming\Python\Advent of Code 2023\Day 18 - Lavaduct Lagoon\output.txt",
    #     "w",
    #     encoding="utf-8",
    # ) as output:
    #     for line in grid:
    #         for character in line:
    #             output.write(character)
    #         output.write("\n")

    counter: int = 0
    for line in grid:
        x = Counter(line)
        counter += x["#"] + x["."]

    print(counter)


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


def fill_interior(grid: list[list[str]], row: int, col: int):
    fill_char: str = "."
    queue: list = []
    queue.append((row, col))
    while queue:
        row, col = queue.pop(0)
        if (
            row < 0
            or row >= len(grid)
            or col < 0
            or col >= len(grid[0])
            or grid[row][col] in [fill_char, "#"]
        ):
            continue
        else:
            grid[row][col] = fill_char

            queue.append((row + 1, col))
            queue.append((row - 1, col))
            queue.append((row, col + 1))
            queue.append((row, col - 1))


if __name__ == "__main__":
    main()
