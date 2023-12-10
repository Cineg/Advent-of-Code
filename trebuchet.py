from input import INPUT


def main() -> int:
    input_arr: list[str] = INPUT.splitlines()
    total: int = 0
    for line in input_arr:
        total += get_value_from_line(line)

    return total


def get_value_from_line(line: str) -> int:
    started: bool = False
    start_num: str = ""
    end_num: str = ""

    for character in line:
        if character.isnumeric():
            if not started:
                start_num = character
                started = True
            end_num = character

    return int(f"{start_num}{end_num}")


if __name__ == "__main__":
    print(main())
