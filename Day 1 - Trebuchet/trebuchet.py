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

    index: int = 0
    for i, character in enumerate(line):
        num: int | None = find_in_string(line, index, i + 1)
        numeric_char: bool = character.isnumeric()
        if numeric_char or num != None:
            if not started:
                if num != None:
                    start_num = str(num)
                if numeric_char:
                    start_num = character
                    index = i
                started = True

            if num != None:
                end_num = str(num)
            if numeric_char:
                end_num = character
                index = i

    return int(f"{start_num}{end_num}")


def find_in_string(string: str, start_index: int, end_index: int) -> int | None:
    nums: dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    current_num: int = 0
    index: int = -1
    find_index: int = -1
    for item in nums:
        find_index = string.rfind(item, start_index, end_index)
        if find_index != -1:
            if find_index > index:
                current_num = nums[item]
                index = find_index

    if current_num != 0:
        return current_num


if __name__ == "__main__":
    print(main())
