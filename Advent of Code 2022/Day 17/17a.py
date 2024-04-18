CAVE_WIDTH: int = 6  # <- 0 is inclusive


def main() -> None:
    rocks: list[list[str]] = get_rocks()
    jet_stream: str = open("Advent of Code 2022\\Day 17\\input.txt").read()

    jet: int = 0
    jet_len: int = len(jet_stream)

    rock: int = 0
    rock_len: int = len(rocks)

    highest_point: int = -1

    floor: set = {(-1, 0), (-1, 1), (-1, 2), (-1, 3), (-1, 4), (-1, 5), (-1, 6)}

    while rock < 2023:
        current_rock: list[str] = rocks[rock % rock_len]
        pos: list[tuple[int, int]] = create_spawn_point(current_rock, highest_point)

        while True:
            current_jet: str = jet_stream[jet]
            jet += 1
            jet %= jet_len

            pos = apply_jet(current_jet, pos, floor)
            fall_pos: list[tuple[int, int]] = apply_gravity(pos)
            if check_collision(fall_pos, floor):
                added_highest: int = update_floor(pos, fall_pos, floor)
                highest_point = max(added_highest, highest_point)
                break

            pos = fall_pos

        rock += 1

    print(highest_point - 1)


def get_rocks() -> list[list[str]]:
    rocks: list[str] = (
        open("Advent of Code 2022\\Day 17\\rocks.txt").read().split("\n\n")
    )
    ret: list[list[str]] = []
    for rock in rocks:
        r: list[str] = rock.split("\n")
        ret.append(r)

    return ret


def create_spawn_point(rock: list[str], highest_point: int) -> list[tuple[int, int]]:
    bottom_pos: int = highest_point + 3

    rock_height: int = len(rock)

    position: list[tuple[int, int]] = []
    for r_i, r in enumerate(rock):
        for c_i, c in enumerate(r):
            if c == ".":
                continue

            row_pos: int = rock_height - r_i + bottom_pos
            position.append((row_pos, c_i + 2))

    return position


def apply_jet(
    jet: str, rock: list[tuple[int, int]], floor: set
) -> list[tuple[int, int]]:
    direction: int = 0
    if jet == ">":
        direction = 1
    else:
        direction = -1

    for coordinate in rock:
        bounds_check: int = direction + coordinate[1]
        if bounds_check < 0 or bounds_check > CAVE_WIDTH:
            return rock

    new_pos: list[tuple[int, int]] = []
    for x, y in rock:
        if (x, y + direction) in floor:
            return rock

        new_pos.append((x, y + direction))

    return new_pos


def apply_gravity(rock: list[tuple[int, int]]) -> list[tuple[int, int]]:
    new_coordinates: list[tuple[int, int]] = []
    for x, y in rock:
        new_coordinates.append((x - 1, y))

    return new_coordinates


def check_collision(fall_position: list[tuple[int, int]], floor: set) -> bool:
    for item in fall_position:
        if item in floor:
            return True

    return False


def update_floor(
    rock_pos: list[tuple[int, int]], fall_pos: list[tuple[int, int]], floor: set
) -> int:
    floor_remove = []

    highest_position: int = -1

    for item in enumerate(fall_pos):
        if item in floor:
            floor_remove.append(item)

    for item in floor_remove:
        floor.remove(item)

    for item in rock_pos:
        floor.add(item)
        if item[0] > highest_position:
            highest_position = item[0]

    return highest_position


if __name__ == "__main__":
    main()
