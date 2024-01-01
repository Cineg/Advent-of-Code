from math import inf


def main() -> None:
    grid: list[list[int]] = get_grid()
    grid_values: list[list[float]] = get_inf_grid(grid)
    grid_values[0][0] = 0

    # value, (row, column), (row direction, column direction), number of moves in direction
    queue: list = [(0, (0, 0), (0, 0), 0)]
    seen_nodes = set()

    min_value: float = inf

    while queue:
        for node in queue:
            node_to_be_seen = (node[1], node[2], node[3])
            queue.pop(queue.index(node))

            # skip if seen
            if node_to_be_seen in seen_nodes:
                continue

            seen_nodes.add(node_to_be_seen)

            value, cell, direction, moves = node

            if value > min_value:
                continue

            if len(grid) - 1 == cell[0] and len(grid[0]) - 1 == cell[1]:
                min_value = min(min_value, value)

            if moves < 3 and direction != (0, 0):
                new_cell = cell[0] + direction[0], cell[1] + direction[1]
                if check_for_bounds(new_cell, grid):
                    new_value = value + grid[new_cell[0]][new_cell[1]]
                    queue.append((new_value, new_cell, direction, moves + 1))

                    grid_values[new_cell[0]][new_cell[1]] = min(
                        new_value, grid_values[new_cell[0]][new_cell[1]]
                    )

            for new_direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                # cant be the same direction
                if new_direction == direction:
                    continue

                # cant move backwards
                if (
                    new_direction[0] == -direction[0]
                    and new_direction[1] == -direction[1]
                ):
                    continue

                new_cell = cell[0] + new_direction[0], cell[1] + new_direction[1]

                # check for out of bonds
                if check_for_bounds(new_cell, grid):
                    new_value = value + grid[new_cell[0]][new_cell[1]]
                    queue.append((new_value, new_cell, new_direction, 1))

                    grid_values[new_cell[0]][new_cell[1]] = min(
                        new_value, grid_values[new_cell[0]][new_cell[1]]
                    )

    print(min_value)


def check_for_bounds(new_cell, grid) -> bool:
    return 0 <= new_cell[0] < len(grid) and 0 <= new_cell[1] < len(grid[0])


def get_grid() -> list[list[int]]:
    input: list[str] = (
        open("Day 17 - Clumsy Crucible\input_test.txt").read().splitlines()
    )

    grid: list[list[int]] = []
    for line in input:
        grid_line: list[int] = []
        for char in line:
            grid_line.append(int(char))

        grid.append(grid_line)

    return grid


def get_inf_grid(grid: list[list[int]]) -> list[list[float]]:
    new_grid: list[list[float]] = []

    for _ in grid:
        line: list[float] = []
        for __ in _:
            line.append(inf)

        new_grid.append(line)

    return new_grid


if __name__ == "__main__":
    main()
