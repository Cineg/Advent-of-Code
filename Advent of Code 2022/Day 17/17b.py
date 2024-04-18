CAVE_WIDTH: int = 6  # <- 0 is inclusive


def main() -> None:
    rocks: list[list[str]] = get_rocks()
    jet_stream: str = open("Advent of Code 2022\\Day 17\\input.txt").read()

    jet: int = 0
    jet_len: int = len(jet_stream)

    rock: int = 0
    rock_len: int = len(rocks)

    highest_point: int = -1

    cycle_jet: list[int] = [0]
    rocks_per_cycle: list[int] = [0]

    iterations: int = 1000000000000
    iterations_left: int = iterations
    result_to_add: int = 0

    floor: set = {(-1, 0), (-1, 1), (-1, 2), (-1, 3), (-1, 4), (-1, 5), (-1, 6)}

    while rock < iterations_left:
        current_rock: list[str] = rocks[rock % rock_len]
        pos: list[tuple[int, int]] = create_spawn_point(current_rock, highest_point)

        while True:
            current_jet: str = jet_stream[jet]
            jet += 1
            jet %= jet_len

            if jet == 0:
                add_cycle(highest_point, cycle_jet, rock, rocks_per_cycle)
                c_j: int = check_cycle_exist(cycle_jet)
                if c_j != -1 and c_j == check_cycle_exist(rocks_per_cycle):
                    j, r = get_cycle_value(cycle_jet, rocks_per_cycle, c_j)

                    rocks_left: int = iterations - sum(rocks_per_cycle)
                    result_to_add = ((rocks_left // r) + 1) * j

                    iterations_left = rocks_left % r

                    rock_pos: int = rock % rock_len

                    iterations_left += rock_pos
                    rock = rock_pos - 1
                    break

            pos = apply_jet(current_jet, pos, floor)
            fall_pos: list[tuple[int, int]] = apply_gravity(pos)
            if check_collision(fall_pos, floor):
                added_highest: int = update_floor(pos, fall_pos, floor)
                highest_point = max(added_highest, highest_point)
                break

            pos = fall_pos

        rock += 1

    print(highest_point - 1 + result_to_add)


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


def add_cycle(
    current_highest: int,
    cycle_jet: list[int],
    current_rock: int,
    rocks_cycle: list[int],
) -> None:
    cycle: int = current_highest - sum(cycle_jet)
    rocks_cycle.append(current_rock - sum(rocks_cycle))

    cycle_jet.append(cycle)


def check_cycle_exist(cycle: list[int]) -> int:
    dic: dict = {}
    for item in cycle[1:]:
        if item not in dic:
            dic[item] = 1
        else:
            dic[item] += 1

    if dic[cycle[-1]] >= 3:
        # find 3 repetitions from the end
        cyc: tuple[int, ...] | None = repetition_len(cycle)
        if cyc != None:
            return len(cyc)

    return -1


def get_cycle_value(
    cycle_jet: list[int], cycle_rock: list[int], cycle_len: int
) -> tuple[int, int]:

    jet_sum: int = sum(cycle_jet[-1 - cycle_len : -1])
    rock_sum: int = sum(cycle_rock[-1 - cycle_len : -1])

    return jet_sum, rock_sum


def repetition_len(cycle: list[int]) -> tuple[int, ...] | None:
    repetitions: list[int] = []
    reverse_cycle: list[int] = cycle[::-1]
    val: int = reverse_cycle[0]
    for index, item in enumerate(reverse_cycle):
        if item == val:
            repetitions.append(index)

    seen: dict[tuple[int, ...], int] = {}
    left: int = 0
    while left < len(repetitions):
        right: int = left + 1
        while right < len(repetitions):
            current_slice = tuple(reverse_cycle[repetitions[left] : repetitions[right]])
            if current_slice not in seen:
                seen[current_slice] = 1
            else:
                seen[current_slice] += 1
                if seen[current_slice] == 3:
                    return current_slice[::-1]

            right += 1
        left += 1

    return


if __name__ == "__main__":
    main()

# 1600571428577
# 1595988538688
