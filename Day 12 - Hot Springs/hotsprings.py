def main():
    input: list[str] = open("Day 12 - Hot Springs\input.txt").read().splitlines()

    total: int = 0
    for line in input:
        damaged_line: str = line.split()[0]
        combination = tuple(map(int, line.split()[1].split(",")))

        total += get_variation(damaged_line, combination)

    print(total)


def get_variation(damaged_line: str, combo: tuple) -> int:
    # early returns for recurrence

    if damaged_line == "":
        if combo == ():
            # valid combo
            return 1
        else:
            return 0

    if combo == ():
        if "#" not in damaged_line:
            # valid combo
            return 1
        else:
            return 0

    total_variations: int = 0

    # if it is either . or ?
    if damaged_line[0] in ".?":
        total_variations = get_variation(damaged_line[1:], combo)

    # if it is either # or ?
    if damaged_line[0] in "#?":
        # no valid options
        if len(damaged_line) < combo[0]:
            return total_variations

        # if there is splitter within combination - no valid option
        slice_for_check: str = damaged_line[: combo[0]]
        if "." in slice_for_check:
            return total_variations

        # last element shouldn't be "#"; it needs to be either "." or "?" to be valid/possible to split; Unless it is full length of line
        if combo[0] == len(damaged_line) or damaged_line[combo[0]] != "#":
            total_variations += get_variation(damaged_line[combo[0] + 1 :], combo[1:])

    return total_variations


if __name__ == "__main__":
    main()
