def main():
    input: str = open("Day 6 - Wait For It\input.txt").read()

    times: list[int] = list(map(int, input.splitlines()[0].split(":")[1].split()))
    distances: list[int] = list(map(int, input.splitlines()[1].split(":")[1].split()))
    possibilities: list[int] = [0] * len(times)
    result: int = 1

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


if __name__ == "__main__":
    main()
