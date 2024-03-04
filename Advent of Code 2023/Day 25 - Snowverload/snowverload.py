def main() -> None:
    input: list[str] = open("Day 25 - Snowverload\input.txt").read().split("\n")

    connects: dict = {}
    connected_to: dict = {}

    for line in input:
        key: str = line.split(":")[0]
        values: list[str] = line.split(": ")[1].split(" ")
        connects[key] = values

        for item in values:
            if key in connected_to:
                connected_to[key].append(item)
            else:
                connected_to[key] = [item]

            if item in connected_to:
                connected_to[item].append(key)
            else:
                connected_to[item] = [key]

    print(connects)


if __name__ == "__main__":
    main()
