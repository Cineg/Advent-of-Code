def main():
    input: list[str] = (
        open("Day 14 - Parabolic Reflector Dish\input.txt").read().splitlines()
    )

    total: int = 0
    run: bool = True
    while run:
        run = move_items(input)

    index: int = 0
    while index < len(input):
        total += count_line(input[index]) * (len(input) - index)
        index += 1

    print(total)


def move_items(input: list[str]) -> bool:
    index: int = 1

    any_change: bool = False

    while index < len(input):
        temp_string_previous: list[str] = []
        temp_string_current: list[str] = []
        letter_index: int = 0
        while letter_index < len(input[index]):
            if (
                input[index - 1][letter_index] == "."
                and input[index][letter_index] == "O"
            ):
                temp_string_previous.append("O")
                temp_string_current.append(".")
                any_change = True
            else:
                temp_string_previous.append(input[index - 1][letter_index])
                temp_string_current.append(input[index][letter_index])

            letter_index += 1

        input[index - 1] = "".join(temp_string_previous)
        input[index] = "".join(temp_string_current)

        index += 1

    return any_change


def count_line(line: str) -> int:
    counter: int = 0
    for char in line:
        if char == "O":
            counter += 1

    return counter


if __name__ == "__main__":
    main()
