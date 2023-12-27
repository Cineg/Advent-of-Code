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

        if top_part == bottom_part:
            reflection_point = i

    return reflection_point


if __name__ == "__main__":
    main()
