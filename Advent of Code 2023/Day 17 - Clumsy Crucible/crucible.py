from math import inf
from heapq import heappop, heappush


class Path:
    def __init__(self, row: int, col: int, value: int, path: list, dir: list) -> None:
        self.row: int = row
        self.col: int = col
        self.value: int = value
        self.path: list[tuple] = path
        self.directions: list[tuple] = dir

    def __lt__(self, _):
        return (self.value, self.row, self.col)

    def is_direction_change_required(self) -> tuple:
        ### returns (0,0) if path is valid
        ### otherwise returns invalid path direction
        last_steps: list[tuple] = self.directions[-3:]
        if len(last_steps) != 3:
            return (0, 0)

        if last_steps[0] == last_steps[1] == last_steps[2]:
            return last_steps[0]

        return (0, 0)

    def no_backward(self) -> tuple:
        row, col = self.directions[-1]
        row = -row
        col = -col

        return (row, col)


def main() -> None:
    grid: list[list[int]] = get_grid()

    queue: list[Path] = [Path(0, 0, 0, [(0, 0)], [(0, 0)])]

    end_path_items: list[Path] = []
    min_value: float = inf

    values: dict = {}

    while queue:
        current_path: Path = heappop(queue)

        if current_path.value > min_value:
            continue

        path_check = tuple(current_path.path[-3:])
        if path_check in values:
            if values[path_check] < current_path.value:
                continue
            else:
                values[path_check] = current_path.value
        else:
            values[path_check] = current_path.value

        forbidden_direction: tuple = current_path.is_direction_change_required()
        for direction in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            if (
                forbidden_direction == direction
                and direction != current_path.no_backward()
            ):
                continue

            row: int = current_path.row + direction[0]
            col: int = current_path.col + direction[1]

            if (
                not check_for_bounds((row, col), grid)
                or (row, col) in current_path.path
            ):
                continue

            path_so_far: list[tuple] = current_path.path.copy()
            direction_so_far: list[tuple] = current_path.directions.copy()
            path_so_far.append((row, col))
            direction_so_far.append(direction)

            new_path: Path = Path(
                row,
                col,
                current_path.value + grid[row][col],
                path_so_far,
                direction_so_far,
            )

            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                end_path_items.append(new_path)
                min_value = min(min_value, new_path.value)

            else:
                heappush(queue, new_path)

    print(min_value)


def check_for_bounds(new_cell, grid) -> bool:
    return 0 <= new_cell[0] < len(grid) and 0 <= new_cell[1] < len(grid[0])


def get_grid() -> list[list[int]]:
    input: list[str] = open("Day 17 - Clumsy Crucible\input.txt").read().splitlines()

    grid: list[list[int]] = []
    for line in input:
        grid_line: list[int] = []
        for char in line:
            grid_line.append(int(char))

        grid.append(grid_line)

    return grid


if __name__ == "__main__":
    main()
