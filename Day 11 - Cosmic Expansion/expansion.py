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

            distance_rows: int = abs(start_point[0] - end_point[0])
            distance_columns: int = abs(start_point[1] - end_point[1])

            total_distance += distance_rows + distance_columns
            right_index += 1

        left_index += 1

    print(total_distance)


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

        temp_arr.append(row)
        if not is_galaxy:
            temp_arr.append(row)

    # add columns
    columns: int = 0

    while columns < len(temp_arr[0]):
        is_galaxy = False
        for row in temp_arr:
            if row[-1 + columns] == "#":
                is_galaxy = True
                break

        if not is_galaxy:
            for row in temp_arr:
                row.insert((-1 + columns), ".")
            columns += 1

        columns += 1

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
