def main() -> None:
    input: list[str] = open("Day 10 - Pipe Maze\input.txt").read().splitlines()
    starting_point: tuple[int, int] | None = _get_starting_point(input)

    loop: list[tuple[int, int]] = []
    loop.append(starting_point)

    result: list[tuple[int, int]] = []

    result = _get_loop(input, starting_point, (0, 1))
    if result == []:
        result = _get_loop(input, starting_point, (0, -1))
    if result == []:
        result = _get_loop(input, starting_point, (-1, 0))
    if result == []:
        result = _get_loop(input, starting_point, (1, 0))

    loop = result

    used_points: dict = {}

    index = 1
    max_value: int = 0
    while index < len(loop):
        value: tuple[int, int] = loop[index]
        value_backwards: tuple[int, int]

        if value in used_points:
            if used_points[value] > index:
                used_points[value] = index
        else:
            used_points[value] = index

        value_backwards = loop[-index]
        if value_backwards in used_points:
            break

        index += 1

    for item in used_points:
        if used_points[item] > max_value:
            max_value = used_points[item]

    print(max_value)


def _get_starting_point(
    input: list[str], starting_point: str = "S"
) -> tuple[int, int] | None:
    for index, line in enumerate(input):
        if "S" in line:
            return index, line.find("S")


def _get_loop(
    input: list[str], starting_point: tuple[int, int], direction: tuple[int, int]
) -> list[tuple[int, int]]:
    run: bool = True
    current_point: tuple[int, int] = starting_point
    current_direction: tuple[int, int] = direction
    loop: list[tuple[int, int]] = []

    while run:
        next_direction: tuple[int, int] = _get_next_maze_direction(
            input, current_point, current_direction
        )

        current_point = (
            current_point[0] + current_direction[0],
            current_point[1] + current_direction[1],
        )

        current_direction = next_direction

        if next_direction == (-999, -999):
            run = False
            loop = []
            break

        if next_direction == (999, 999):
            run = False
            break

        loop.append(current_point)

    return loop


def _get_next_maze_direction(
    input: list[str], point: tuple[int, int], direction: tuple[int, int]
) -> tuple[int, int]:
    next_point_coords: tuple[int, int] = (
        point[0] + direction[0],
        point[1] + direction[1],
    )
    next_point: str = input[next_point_coords[0]][next_point_coords[1]]

    # all cases
    if next_point == ".":
        return (-999, -999)

    if next_point == "-":
        if direction[0] != 0:
            return (-999, -999)
        else:
            return direction

    if next_point == "|":
        if direction[1] != 0:
            return (-999, -999)
        else:
            return direction

    if next_point == "L":
        if direction == (1, 0):
            return (0, 1)
        elif direction == (0, -1):
            return (-1, 0)
        else:
            return (-999, -999)

    if next_point == "J":
        if direction == (1, 0):
            return (0, -1)
        elif direction == (0, 1):
            return (-1, 0)
        else:
            return (-999, -999)

    if next_point == "7":
        if direction == (-1, 0):
            return (0, -1)
        elif direction == (0, 1):
            return (1, 0)
        else:
            return (-999, -999)

    if next_point == "F":
        if direction == (-1, 0):
            return (0, 1)
        elif direction == (0, -1):
            return (1, 0)
        else:
            return (-999, -999)

    if next_point == "S":
        return (999, 999)


if __name__ == "__main__":
    main()
