import re


def main():
    input_data: str = open("Advent of Code 2022\Day 5\input.txt").read()

    crates: list[list[str]] = get_crates(input_data.split("\n\n")[0].split("\n"))
    directions: list[str] = input_data.split("\n\n")[1].split("\n")

    for direction in directions:
        data: list[int] = list(map(int, re.findall("\\d+", direction)))
        items: int = data[0]
        fr: int = data[1] - 1
        to: int = data[2] - 1

        load: list[str] = crates[fr][0:items]
        crates[fr] = crates[fr][items:]
        crates[to] = load + crates[to]

    result: str = ""
    for item in crates:
        if len(item) > 0:
            result += item[0]

    print(result)
    return result


def get_crates(crates_rows: list[str]) -> list[list[str]]:
    crates: list[list[str]] = []

    crate_items: int = len(crates_rows[-1].replace(" ", ""))
    for item in range(crate_items):
        crates.append([])

    for row in crates_rows:
        index: int = 1
        while index < len(row):
            if row[index] == "]":
                crates[int((index) / 4)].append(row[index - 1])
            index += 1

    return crates


if __name__ == "__main__":
    main()
