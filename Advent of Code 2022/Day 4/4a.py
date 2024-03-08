def main() -> None:
    input: list[str] = open("Advent of Code 2022\Day 4\input.txt").read().split("\n")

    total: int = 0
    for item in input:
        a, b = item.split(",")
        elf_a = list(map(int, a.split("-")))
        elf_b = list(map(int, b.split("-")))

        if (
            elf_a[0] <= elf_b[0] <= elf_b[1] <= elf_a[1]
            or elf_b[0] <= elf_a[0] <= elf_a[1] <= elf_b[1]
        ):
            total += 1

    print(total)


if __name__ == "__main__":
    main()
