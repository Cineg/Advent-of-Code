def main() -> None:
    input: list[str] = open("Advent of Code 2022\Day 8\input.txt").read().split("\n")

    seen: set = {(0, 0)}

    get_borders(seen, input)
    get_rows(seen, input)
    get_columns(seen, input)
    print(len(seen))


def get_borders(seen: set, input: list[str]) -> None:
    for row, line in enumerate(input):
        for col, _ in enumerate(line):
            if col == 0 or row == 0 or row == len(line) - 1 or col == len(input) - 1:
                if (row, col) not in seen:
                    seen.add((row, col))
                    continue


def get_rows(seen: set, input: list[str]) -> None:
    row: int = 1
    row_len: int = len(input[row])
    while row < len(input) - 1:
        max_left: int = int(input[row][0])
        max_right: int = int(input[row][-1])

        col: int = 1
        while col < row_len - 1:
            right_index: int = row_len - col - 1
            current_left: int = int(input[row][col])
            current_right: int = int(input[row][right_index])

            if current_left > max_left:
                max_left = current_left
                if (row, col) not in seen:
                    seen.add((row, col))

            if current_right > max_right:
                max_right = current_right
                if (row, right_index) not in seen:
                    seen.add((row, right_index))

            col += 1

        row += 1


def get_columns(seen: set, input: list[str]) -> None:
    col: int = 1
    col_len: int = len(input)

    while col < len(input[0]):
        max_top: int = int(input[0][col])
        max_bot: int = int(input[-1][col])

        row: int = 1
        while row < col_len - 1:
            bot_index: int = col_len - row - 1
            current_top: int = int(input[row][col])
            current_bot: int = int(input[bot_index][col])

            if current_top > max_top:
                max_top = current_top
                if (row, col) not in seen:
                    seen.add((row, col))

            if current_bot > max_bot:
                max_bot = current_bot
                if (bot_index, col) not in seen:
                    seen.add((bot_index, col))

            row += 1
        col += 1


if __name__ == "__main__":
    main()
