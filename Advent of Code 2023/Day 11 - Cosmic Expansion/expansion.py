VALUE = 1000000


def main():
    input: list[str] = open("Day 11 - Cosmic Expansion\input.txt").read().splitlines()

    cosmic_map: list[list[str]] = _create_cosmic_map(input)
    cosmic_map = _update_cosmic_map(cosmic_map)
    galaxies_position: list[tuple[int, int]] = _get_galaxies_position(cosmic_map)

    total_distance: int = 0

    left_index: int = 0
    right_index: int = 0

    while left_index < len(galaxies_position) - 1:
        right_index = left_index + 1
        while right_index < len(galaxies_position):
            start_point: tuple[int, int] = galaxies_position[left_index]
            end_point: tuple[int, int] = galaxies_position[right_index]

            total_distance += distance_vertical(
                cosmic_map, start_point[1], start_point[0], end_point[0]
            )
            total_distance += distance_horizontal(
                cosmic_map, start_point[0], start_point[1], end_point[1]
            )

            right_index += 1

        left_index += 1

    print(total_distance)


def distance_vertical(
    map: list[list[str]], column: int, row_start: int, row_end: int
) -> int:
    if row_end < row_start:
        row_end, row_start = row_start, row_end

    value: int = 0
    for row in range(row_start, row_end):
        if map[row][column] == "X":
            value += VALUE
        else:
            value += 1

    return value


def distance_horizontal(
    map: list[list[str]], row: int, col_start: int, col_end: int
) -> int:
    if col_end < col_start:
        col_start, col_end = col_end, col_start

    value: int = 0
    for col in range(col_start, col_end):
        if map[row][col] == "X":
            value += VALUE
        else:
            value += 1

    return value


def _create_cosmic_map(input: list[str]) -> list[list[str]]:
    cosmic_map: list[list[str]] = []
    for row in input:
        cosmic_row: list[str] = []
        for item in row:
            cosmic_row.append(item)

        cosmic_map.append(cosmic_row)

    return cosmic_map


def _update_cosmic_map(cosmic_map: list[list[str]]) -> list[list[str]]:
    temp_arr: list[list[str]] = []
    is_galaxy: bool = False
    # add rows
    for row in cosmic_map:
        is_galaxy = False
        for item in row:
            if item == "#":
                is_galaxy = True
                break

        if not is_galaxy:
            i: int = 0
            while i < len(row):
                row[i] = "X"
                i += 1

        temp_arr.append(row)

    # add columns
    column: int = 0
    while column < len(temp_arr[0]):
        is_galaxy = False
        for row in temp_arr:
            if row[column] == "#":
                is_galaxy = True
                break

        if not is_galaxy:
            i: int = 0
            while i < len(temp_arr):
                temp_arr[i][column] = "X"
                i += 1

        column += 1

    return temp_arr


def _get_galaxies_position(cosmic_map: list[list[str]]) -> list[tuple[int, int]]:
    galaxies_position: list[tuple[int, int]] = []
    for row, _ in enumerate(cosmic_map):
        for col, value in enumerate(_):
            if value == "#":
                galaxies_position.append((row, col))

    return galaxies_position


if __name__ == "__main__":
    main()
