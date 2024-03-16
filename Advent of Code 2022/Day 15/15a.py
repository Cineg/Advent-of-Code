def main() -> None:
    input: list[tuple[int, int, int, int]] = get_input_data(
        "Advent of Code 2022\Day 15\\input.txt"
    )
    seen: set = set()
    inline: set = set()
    find_line: int = 2_000_000

    for item in input:
        sx, sy, bx, by = item
        distance: int = abs(sx - bx) + abs(sy - by)

        offset: int = distance - abs(sy - find_line)
        if offset < 0:
            continue

        min_x: int = sx - offset
        max_x: int = sx + offset

        for x in range(min_x, max_x + 1):
            seen.add(x)

        if by == find_line:
            inline.add(bx)

    print(len(seen) - len(inline))


def get_input_data(input_path: str) -> list[tuple[int, int, int, int]]:
    input: list[str] = open(input_path).read().split("\n")

    sensors: list[tuple[int, int, int, int]] = []
    for line in input:
        sensor, beacon = line.split(":")
        sensor, beacon = sensor.split("at")[1], beacon.split("at")[1]
        s_x, s_y = int(sensor.split(",")[0].split("=")[1]), int(
            sensor.split(",")[1].split("=")[1]
        )
        b_x, b_y = int(beacon.split(",")[0].split("=")[1]), int(
            beacon.split(",")[1].split("=")[1]
        )

        sensors.append((s_x, s_y, b_x, b_y))

    return sensors


if __name__ == "__main__":
    main()
