from copy import copy, deepcopy


class Path:
    def __init__(self, current_path: set, row: int, col: int, value: int = 0):
        self.seen: set = current_path
        self.row: int = row
        self.col: int = col


def main():
    grid: list[list[str]] = create_grid(
        open("Day 23 - A Long Walk\input.txt").read().split("\n")
    )

    empty_grid: list[list[int]] = _get_empty_grid(grid)
    queue: list = []

    coordinates: tuple[int, int] = _get_coordinates(grid, 0)
    end_coordinates: tuple[int, int] = _get_coordinates(grid, len(grid) - 1)

    path: Path = Path(set(), coordinates[0], coordinates[1])

    queue.append(path)
    empty_grid[coordinates[0]][coordinates[1]] = 0
    paths = []
    vals = []

    while queue:
        path: Path = queue[0]
        queue.pop(0)
        path.seen.add((path.row, path.col))
        if path.row == end_coordinates[0] and path.col == end_coordinates[1]:
            paths.append(path)
            vals.append(len(path.seen) - 1)
            continue

        if grid[path.row][path.col] != "#":
            for dir in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                new_row: int = path.row + dir[0]
                new_col: int = path.col + dir[1]

                if not _is_in_bounds(new_row, new_col, grid):
                    continue

                if grid[new_row][new_col] != "#":
                    if not (new_row, new_col) in path.seen:
                        new_path: Path = Path(path.seen.copy(), new_row, new_col)
                        new_path.seen.add((new_row, new_col))
                        queue.append(new_path)

        # if (
        #     grid[path.row][path.col] == "^"
        #     and (path.row - 1, path.col) not in path.seen
        # ):
        #     path.row = -1
        #     queue.append(path)
        # if (
        #     grid[path.row][path.col] == ">"
        #     and (path.row, path.col + 1) not in path.seen
        # ):
        #     path.col += 1
        #     queue.append(path)

        # if (
        #     grid[path.row][path.col] == "v"
        #     and (path.row + 1, path.col) not in path.seen
        # ):
        #     path.row += 1
        #     queue.append(path)

        # if (
        #     grid[path.row][path.col] == "<"
        #     and (path.row, path.col - 1) not in path.seen
        # ):
        #     path.col -= 1
        #     queue.append(path)

    print(max(vals))


def create_grid(input: list[str]) -> list[list[str]]:
    grid: list[list[str]] = []
    for row in input:
        line: list[str] = []
        for char in row:
            line.append(char)

        grid.append(line)
    return grid


def _get_empty_grid(grid: list[list[str]]) -> list[list[int]]:
    empty_grid: list[list[int]] = []
    for row in grid:
        line: list[int] = []
        for _ in row:
            line.append(-1)

        empty_grid.append(line)
    return empty_grid


def _get_coordinates(grid: list[list[str]], row: int) -> tuple[int, int]:
    for index, char in enumerate(grid[row]):
        if char == ".":
            return (row, index)

    return (-1, -1)


def _is_in_bounds(row: int, col: int, grid: list[list[str]]) -> bool:
    if row < 0 or col < 0:
        return False

    if row >= len(grid) or col >= len(grid[0]):
        return False

    return True


if __name__ == "__main__":
    main()
