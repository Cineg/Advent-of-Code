def main():
    input: str = open("Day 6 - Wait For It\input.txt").read()

    times: list[int] = list(map(int, input.splitlines()[0].split(":")[1].split()))
    distances: list[int] = list(map(int, input.splitlines()[1].split(":")[1].split()))
    possibilities: list[int] = [0] * len(times)
    result: int = 1

    print(total_time(input))

    for race in range(0, len(times)):
        current_speed: int = 0
        remaining_time: int = times[race]
        while remaining_time > 0:
            if current_speed * remaining_time >= distances[race]:
                possibilities[race] += 1

            current_speed += 1
            remaining_time -= 1

    for possibility in possibilities:
        result *= possibility

    print(result)


def total_time(input: str):
    times: list[int] = list(map(int, input.splitlines()[0].split(":")[1].split()))
    distances: list[int] = list(map(int, input.splitlines()[1].split(":")[1].split()))

    time: int = int("".join(map(str, times)))
    distance: int = int("".join(map(str, distances)))

    first_winnable_event: int = 0
    last_winnable_event: int = 0

    current_speed: int = 0
    remaining_time: int = time

    while remaining_time > 0:
        if current_speed * remaining_time >= distance:
            first_winnable_event = current_speed
            break

        current_speed += 1
        remaining_time -= 1

    current_speed = time
    remaining_time = 0
    while remaining_time < time:
        if current_speed * remaining_time >= distance:
            last_winnable_event = current_speed
            break

        current_speed -= 1
        remaining_time += 1

    return last_winnable_event - first_winnable_event + 1


if __name__ == "__main__":
    main()
