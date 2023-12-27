def main() -> None:
    input: list[str] = (
        open("Day 13 - Point of Incidence\input.txt").read().split("\n\n")
    )

    total: int = 0
    for item in input:
        pattern: list[str] = item.splitlines()

        total += find_reflection(pattern) * 100

        # transpose
        total += find_reflection(list(zip(*pattern)))

    print(total)


def find_reflection(pattern: list[str]) -> int:
    reflection_point: int = 0
    for i in range(1, len(pattern)):
        top_part: list[str] = pattern[:i][::-1]
        bottom_part: list[str] = pattern[i:]

        # need to adjust to same length
        top_part = top_part[: len(bottom_part)]
        bottom_part = bottom_part[: len(top_part)]

        if is_smudged(top_part, bottom_part):
            reflection_point = i

        # if top_part == bottom_part:
        #     reflection_point = i

    return reflection_point


def is_smudged(top_part: list[str], bottom_part: list[str]) -> bool:
    differences: int = 0
    line_length: int = len(top_part[0])
    for i in range(0, len(top_part)):
        for char in range(0, line_length):
            if top_part[i][char] != bottom_part[i][char]:
                differences += 1

            if differences > 1:
                break
        if differences > 1:
            break

    if differences == 1:
        return True

    return False


if __name__ == "__main__":
    main()
