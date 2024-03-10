def main() -> None:
    input: list[str] = open("Advent of Code 2022\Day 8\input.txt").read().split("\n")

    max_scenic_score: int = 0
    for row, _ in enumerate(input):
        for col, __ in enumerate(_):
            max_scenic_score = max(
                max_scenic_score, calculate_scenic_score(input, row, col)
            )

    print(max_scenic_score)


def calculate_scenic_score(input: list[str], row: int, col: int) -> int:
    top: int = 0
    bot: int = 0
    left: int = 0
    right: int = 0

    if out_of_bounds(input, row, col):
        return 0

    tree_size: int = int(input[row][col])

    # left
    index: int = 1
    while not out_of_bounds(input, row - index, col):
        tree: int = int(input[row - index][col])
        left += 1

        if tree >= tree_size:
            break
        index += 1

    # right
    index: int = 1
    while not out_of_bounds(input, row + index, col):
        tree: int = int(input[row + index][col])
        right += 1

        if tree >= tree_size:
            break
        index += 1

    # top
    index: int = 1
    while not out_of_bounds(input, row, col - index):
        tree: int = int(input[row][col - index])
        top += 1

        if tree >= tree_size:
            break
        index += 1

    # bot
    index: int = 1
    while not out_of_bounds(input, row, col + index):
        tree: int = int(input[row][col + index])
        bot += 1

        if tree >= tree_size:
            break
        index += 1

    return top * bot * left * right


def out_of_bounds(input: list[str], row: int, col: int) -> bool:
    if row < 0 or col < 0:
        return True

    if row == len(input) or col == len(input[0]):
        return True

    return False


if __name__ == "__main__":
    main()
