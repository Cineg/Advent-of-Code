from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Valve:
    name: str
    flow_rate: int
    tunnels: list


def main() -> None:
    input_path: str = "Advent of Code 2022\Day 16\\input.txt"
    data: dict[str, Valve] = get_data(input_path)
    valuable_paths: dict[str, dict[str, int]] = get_valuable_paths(data)

    max_value: int = 0
    # time, total released, current valve, seen
    queue: list[tuple[int, int, str, set[str]]] = [(0, 0, "AA", set())]
    while queue:
        time, released, valve, seen = queue.pop(0)
        moves: dict[str, int] = valuable_paths[valve]
        for v in moves:
            if v in seen:
                continue

            rate: int = data[v].flow_rate
            # current time + time to move + opening time
            t: int = time + moves[v] + 1

            if t >= 30:
                continue

            rel: int = released + ((30 - t) * rate)
            new_set: set[str] = seen.copy()
            new_set.add(v)

            max_value = max(max_value, rel)

            queue.append((t, rel, v, new_set))

    print(max_value)


def get_valuable_points(data: dict[str, Valve]) -> list[str]:
    valuable: list[str] = []
    for key in data:
        if data[key].flow_rate > 0:
            valuable.append(key)

    return valuable


def get_valuable_paths(data: dict[str, Valve]) -> dict[str, dict[str, int]]:
    points: list[str] = get_valuable_points(data)

    paths_dict: dict[str, dict[str, int]] = {}
    queue: list[tuple[int, str]] = [(0, "AA")]
    for item in points:
        queue.append((0, item))

    while queue:
        visited: set = set()
        distance, valve = queue.pop(0)
        visited.add(valve)

        paths: list[tuple[int, str]] = [(distance, valve)]
        valuable: dict[str, int] = {}
        while paths:
            d, v = paths.pop(0)
            d += 1

            for item in data[v].tunnels:
                if item in visited:
                    continue

                if item in points:
                    valuable[item] = d

                visited.add(item)

                paths.append((d, item))

        paths_dict[valve] = valuable

    return paths_dict


def get_data(input_path: str) -> dict[str, Valve]:
    input: list[str] = open(input_path).read().split("\n")
    valves: dict[str, Valve] = {}
    for line in input:
        name: str = line.split(" has ")[0].split(" ")[-1]
        rate: int = int(line.split(";")[0].split("=")[-1])
        tunnels: list[str] = line.split("valve")[-1].split(",")
        for index, item in enumerate(tunnels):
            cleaned_item: str = item.split(" ")[-1]
            tunnels[index] = cleaned_item

        valves[name] = Valve(name, rate, tunnels)
    return valves


if __name__ == "__main__":
    main()
