from pathlib import Path


def day1() -> int:
    tiles: list[list[str]] = read_map()
    start_pos: tuple[int, int] = get_start_position(tiles)

    directions: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    seen = set()
    seen.add(start_pos)

    current_pos: tuple[int, int] = start_pos
    direction: int = 0

    while True:
        next: tuple[int, int] = (
            current_pos[0] + directions[direction][0],
            current_pos[1] + directions[direction][1],
        )
        if not (
            next[0] >= 0
            and next[0] < len(tiles)
            and next[1] >= 0
            and next[1] < len(tiles[0])
        ):
            break

        if tiles[next[0]][next[1]] == "#":
            direction += 1
            direction %= 4
            continue

        current_pos = next
        seen.add(next)

    return len(seen)


def day2() -> int:
    tiles: list[list[str]] = read_map()
    start_pos: tuple[int, int] = get_start_position(tiles)

    obstacle: int = 0
    for r in range(len(tiles)):
        for c in range(len(tiles[0])):
            if tiles[r][c] != ".":
                continue

            tiles[r][c] = "#"
            if loops(tiles, start_pos):
                obstacle += 1

            tiles[r][c] = "."

    return obstacle


def read_map() -> list[list[str]]:
    input: str = open(Path(Path(__file__).parent, "input.txt"), "r").read()
    path: list[str] = input.split("\n")
    return_arr = []
    for line in path:
        return_arr.append([i for i in line])

    return return_arr


def get_start_position(tiles: list[list[str]]) -> tuple[int, int]:
    for r, row in enumerate(tiles):
        for c, i in enumerate(row):
            if i == "^":
                return (r, c)

    return (-1, -1)


def loops(tiles: list[list[str]], position: tuple[int, int]) -> bool:
    seen = set()

    directions: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction: int = 0

    while True:
        seen.add((position, direction))
        next: tuple[int, int] = (
            position[0] + directions[direction][0],
            position[1] + directions[direction][1],
        )

        if not (
            next[0] >= 0
            and next[0] < len(tiles)
            and next[1] >= 0
            and next[1] < len(tiles[0])
        ):
            return False

        if tiles[next[0]][next[1]] == "#":
            direction += 1
            direction %= 4
            continue

        if (next, direction) in seen:
            return True

        position = next


if __name__ == "__main__":
    print(day1())
    print(day2())
