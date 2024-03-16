def main() -> None:
    input: list[tuple[int, int, int, int]] = get_input_data(
        "Advent of Code 2022\Day 15\\input.txt"
    )

    max_line: int = 4_000_000
    total_ranges: list[list[list[int]]] = []

    for i in range(max_line + 1):
        interval: list[list[int]] = get_line_intervals(input, i)
        interval.sort()
        ranges: list[list[int]] = get_reserved_range(interval)
        total_ranges.append(ranges)

    # search for the gap in ranges
    for i, item in enumerate(total_ranges):
        if len(item) > 1:
            if item[0][1] + 1 > 4_000_000:
                continue
            elif i > 4_000_000:
                break
            else:
                print((item[0][1] + 1) * 4_000_000 + i)
                break


def get_line_intervals(
    input: list[tuple[int, int, int, int]], line: int
) -> list[list[int]]:
    interval: list[list[int]] = []
    for item in input:
        sx, sy, bx, by = item
        distance: int = abs(sx - bx) + abs(sy - by)

        offset: int = distance - abs(sy - line)
        if offset < 0:
            continue

        min_x: int = sx - offset
        max_x: int = sx + offset

        interval.append([min_x, max_x])

    return interval


def get_reserved_range(intervals: list[list[int]]) -> list[list[int]]:
    ranges: list[list[int]] = []
    for item in intervals:
        low, high = item
        if len(ranges) == 0:
            ranges.append([low, high])
            continue

        # if touching - exactly one more, it's ok to merge
        if low > ranges[-1][1] + 1:
            ranges.append([low, high])
        else:
            ranges[-1][1] = max(high, ranges[-1][1])

    return ranges


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
