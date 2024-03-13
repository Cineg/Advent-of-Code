from heapq import heappop, heappush


def main() -> None:
    grid: list[list[str]] = get_grid("Advent of Code 2022\Day 12\\input.txt")
    start: tuple[int, int] = get_position(grid, "S")
    end: tuple[int, int] = get_position(grid, "E")

    # moves, (row, col)
    seen: set = {(0, 0)}
    queue: list[tuple] = [(0, start)]

    grid[start[0]][start[1]] = "a"
    grid[end[0]][end[1]] = "z"

    while queue:
        moves, coordinates = heappop(queue)

        x, y = coordinates
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            row: int = x + direction[0]
            col: int = y + direction[1]

            if (row, col) == end:
                print(moves + 1)
                return

            if row < 0 or col < 0:
                continue

            if row >= len(grid) or col >= len(grid[0]):
                continue

            if ord(grid[row][col]) - ord(grid[x][y]) > 1:
                continue

            if (row, col) in seen:
                continue

            heappush(queue, (moves + 1, (row, col)))
            seen.add((row, col))


def get_grid(file_path: str) -> list[list[str]]:
    grid: list[list[str]] = []
    for line in open(file_path).read().split("\n"):
        row: list[str] = []
        for letter in line:
            row.append(letter)

        grid.append(row)
    return grid


def get_position(grid: list[list[str]], letter: str) -> tuple[int, int]:
    for row, _ in enumerate(grid):
        for col, val in enumerate(_):
            if val == letter:
                return (row, col)

    return (-1, -1)


if __name__ == "__main__":
    main()
