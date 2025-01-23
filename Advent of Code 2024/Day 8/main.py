from pathlib import Path

input_data: str = open(Path(Path(__file__).parent, "input.txt"), "r").read()


def part1() -> int:
    grid: list[list[str]] = _get_grid()
    nodes: dict[str, set[tuple[int, int]]] = _get_nodes(grid)

    antinodes = set()
    for node_list in nodes.values():
        antinodes.update(_get_antinodes(node_list))

    total: int = 0
    for antinode in antinodes:
        if (
            antinode[0] < 0
            or antinode[0] >= len(grid[0])
            or antinode[1] < 0
            or antinode[1] >= len(grid)
        ):
            continue

        total += 1

    return total


def _get_nodes(grid: list[list[str]]) -> dict[str, set[tuple[int, int]]]:
    data: dict[str, set[tuple[int, int]]] = {}
    for row_index, row in enumerate(grid):
        for col, value in enumerate(row):
            if value != ".":
                if value not in data:
                    data[value] = set()

                data[value].add((row_index, col))

    return data


def _get_antinodes(nodes: set[tuple[int, int]]) -> set[tuple[int, int]]:
    i: int = 0
    nodes_list = list(nodes)

    antinodes: set = set()

    while i < len(nodes):
        current: tuple[int, int] = nodes_list[i]
        for n in range(len(nodes)):
            if n == i:
                continue

            r_diff = abs(current[0] - nodes_list[n][0])
            c_diff = abs(current[1] - nodes_list[n][1])

            curr_r = r_diff if current[0] > nodes_list[n][0] else -r_diff
            curr_c = c_diff if current[1] > nodes_list[n][1] else -c_diff

            antinodes.add((current[0] + curr_r, current[1] + curr_c))
            antinodes.add((nodes_list[n][0] - curr_r, nodes_list[n][1] - curr_c))

        i += 1

    return antinodes


def _get_grid() -> list[list[str]]:
    grid: list[list[str]] = []
    for row in input_data.split("\n"):
        line: list[str] = []
        for char in row:
            line.append(char)

        grid.append(line)

    return grid


if __name__ == "__main__":
    print(part1())
