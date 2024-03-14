def main() -> None:
    input: list[list] = create_input("Advent of Code 2022\Day 13\\input.txt")
    total: int = 0

    for pair_pos, pair in enumerate(input):
        res: bool | None = compare_arr(pair[0], pair[1])

        if res == True:
            total += pair_pos + 1

    print(total)


def compare_arr(left: list, right: list) -> bool | None:
    index: int = 0
    success: bool | None = None

    while index < len(left):
        if success != None:
            return success

        if index >= len(right):
            return False

        if type(left[index]) == type(right[index]):
            if type(left[index]) == list:
                success = compare_arr(left[index], right[index])
            elif type(left[index]) == int:
                if left[index] < right[index]:
                    return True
                if left[index] > right[index]:
                    return False

        else:
            if type(left[index]) == list:
                success = compare_arr(left[index], [right[index]])
            else:
                success = compare_arr([left[index]], right[index])

        index += 1

    if success == None:
        if len(left) < len(right):
            return True
        if len(left) > len(right):
            return False

        return None

    return success


def create_input(path: str) -> list[list]:
    input: list[str] = open(path).read().split("\n\n")
    res: list[list] = []
    for line in input:
        left, right = line.split("\n")
        l_arr = _convert_to_list(left)
        r_arr = _convert_to_list(right)

        res.append([l_arr, r_arr])

    return res


def _convert_to_list(line: str, index: int = 0) -> tuple[list, int] | list:
    arr: list = []
    token: str = ""
    while index < len(line):
        if line[index] == "[":
            res, ind = _convert_to_list(line, index + 1)
            arr.append(res)
            index = ind

        elif line[index] == "]":
            if token != "":
                arr.append(int(token))
            return (arr, index)
        elif line[index] == ",":
            if token == "":
                pass
            else:
                arr.append(int(token))
            token = ""
        else:
            token += line[index]

        index += 1

    return arr[0]


if __name__ == "__main__":
    main()
