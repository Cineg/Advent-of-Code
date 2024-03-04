def main():
    input: list[str] = open("Day 9 - Mirage Maintenance\input.txt").read().splitlines()
    total_left: int = 0
    total_right: int = 0

    for line in input:
        row: list[int] = list(map(int, line.split()))
        total_triangle: list[list[int]] = list_triangle(row)
        total_left += get_triangle_extrapolated_value_first(total_triangle)
        total_right += get_triangle_extrapolated_value(total_triangle)

    print(total_left, total_right)


def list_triangle(row: list[int]) -> list[list[int]]:
    total_triangle: list[list[int]] = []
    total_triangle.append(row)

    new_row: list[int] = []

    run: bool = is_list_zero(row)
    while not run:
        run = is_list_zero(row)
        if run:
            break

        index = 0
        while index < len(row) - 1:
            new_row.append(row[-1 - index] - row[-2 - index])
            index += 1
        new_row.reverse()

        total_triangle.append(new_row)
        row = new_row
        new_row = []

    return total_triangle


def get_triangle_extrapolated_value(triangle: list[list[int]]) -> int:
    index: int = 0

    while index < len(triangle) - 1:
        value: int = triangle[-1 - index][-1] + triangle[-2 - index][-1]
        triangle[-2 - index].append(value)
        index += 1

    return triangle[0][-1]


def get_triangle_extrapolated_value_first(triangle: list[list[int]]):
    index: int = 0

    while index < len(triangle) - 1:
        value: int = triangle[-1 - index][0] - triangle[-2 - index][0]
        triangle[-2 - index].insert(0, -value)
        index += 1

    return triangle[0][0]


def is_list_zero(row: list[int]) -> bool:
    for item in row:
        if item != 0:
            return False

    return True


if __name__ == "__main__":
    main()
