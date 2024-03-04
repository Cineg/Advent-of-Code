from input import INPUT


def main() -> None:
    data: list[str] = INPUT.split("\n\n")

    seeds: list[int] = list(map(int, data[0].split(":")[-1].split()))

    for data_map in data[1:]:
        data_chunk: list[str] = data_map.splitlines()[1:]
        data_range: list[list[int]] = []
        for line in data_chunk:
            data_range.append(list(map(int, line.split())))

        next_source_positions: list[int] = []
        for seed in seeds:
            flag: bool = False
            for range_start, source_range_start, range_length in data_range:
                if source_range_start <= seed < source_range_start + range_length:
                    next_source_positions.append(
                        seed - source_range_start + range_start
                    )
                    flag = True
                    break

            if not flag:
                next_source_positions.append(seed)

        seeds = next_source_positions

    print(min(seeds))


if __name__ == "__main__":
    main()
