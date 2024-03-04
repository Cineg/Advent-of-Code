from enum import Enum


class Direction(Enum):
    North = (-1, 0)
    South = (1, 0)
    West = (0, -1)
    East = (0, 1)


def main():
    input: list[str] = (
        open("Day 14 - Parabolic Reflector Dish\input.txt").read().splitlines()
    )
    matrix: list[list[str]] = [list(line) for line in input]

    total: int = 0
    run: bool = True
    cycle: int = 0

    seen_matrixes: set[tuple] = {()}
    result_matrixes: list = []
    last_array_index: int = -1

    while cycle < 1000000000:
        hashed_matrix = hashable_matrix(matrix)
        if hashed_matrix not in seen_matrixes:
            seen_matrixes.add(hashed_matrix)
            result_matrixes.append(hashed_matrix)
        else:
            first_iteration: int = result_matrixes.index(hashed_matrix)
            remaining: int = 1000000000 - first_iteration

            last_array_index = remaining % (cycle - first_iteration) + first_iteration

        if last_array_index != -1:
            break

        run: bool = True
        while run:
            run = move_items(matrix, Direction.North)

        run = True
        while run:
            run = move_items(matrix, Direction.West)

        run = True
        while run:
            run = move_items(matrix, Direction.South)

        run = True
        while run:
            run = move_items(matrix, Direction.East)

        cycle += 1

    index: int = 0
    while index < len(result_matrixes[last_array_index]):
        total += count_line(result_matrixes[last_array_index][index]) * (
            len(result_matrixes[last_array_index]) - index
        )
        index += 1

    print(total)


def move_items(input: list[list[str]], direction: Direction) -> bool:
    any_change: bool = False

    index: int = 0
    if direction == Direction.North:
        index = 1

    max_index: int = len(input)
    if direction == Direction.South:
        max_index = len(input) - 1

    while index < max_index:
        letter_index: int = 0
        if direction == Direction.West:
            letter_index = 1

        max_letter_index: int = len(input[index])
        if direction == Direction.East:
            max_letter_index = len(input[index]) - 1

        while letter_index < max_letter_index:
            if (
                input[index + direction.value[0]][letter_index + direction.value[1]]
                == "."
                and input[index][letter_index] == "O"
            ):
                input[index + direction.value[0]][
                    letter_index + direction.value[1]
                ] = "O"
                input[index][letter_index] = "."
                any_change = True

            letter_index += 1

        index += 1

    return any_change


def count_line(line: str) -> int:
    counter: int = 0
    for char in line:
        if char == "O":
            counter += 1

    return counter


def hashable_matrix(matrix) -> tuple:
    final = []
    for line in matrix:
        row = tuple(line)
        final.append(row)

    return tuple(final)


if __name__ == "__main__":
    main()
