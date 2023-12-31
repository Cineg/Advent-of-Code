from dataclasses import dataclass
import sys


@dataclass
class Cell:
    up: bool = False
    down: bool = False
    left: bool = False
    right: bool = False

    def add_direction(self, direction: tuple[int, int]) -> None:
        if direction == (-1, 0):
            self.up = True
        if direction == (1, 0):
            self.down = True
        if direction == (0, -1):
            self.left = True
        if direction == (0, 1):
            self.right = True

    def is_energized(self) -> bool:
        if self.up or self.down or self.right or self.left:
            return True
        return False

    def seen(self, direction) -> bool:
        if direction == (-1, 0) and self.up:
            return True
        if direction == (1, 0) and self.down:
            return True
        if direction == (0, -1) and self.left:
            return True
        if direction == (0, 1) and self.right:
            return True

        return False


def main() -> None:
    input: list[str] = (
        open("Day 16 - The Floor Will Be Lava\input.txt").read().splitlines()
    )
    input_grid: list[list[str]] = convert_to_2D(input)

    max_result: int = 0
    for row_index, _ in enumerate(input):
        # down
        energized_board: list[list[Cell]] = get_empty_grid(input)
        move(energized_board, input_grid, (0, row_index), (1, 0))
        max_result = max(max_result, calculate_energized(energized_board))

        # up
        energized_board: list[list[Cell]] = get_empty_grid(input)
        move(energized_board, input_grid, (len(input_grid) - 1, row_index), (-1, 0))
        max_result = max(max_result, calculate_energized(energized_board))

    for col_index, _ in enumerate(input[0]):
        # right
        energized_board: list[list[Cell]] = get_empty_grid(input)
        move(energized_board, input_grid, (col_index, 0), (0, 1))
        max_result = max(max_result, calculate_energized(energized_board))

        # left
        energized_board: list[list[Cell]] = get_empty_grid(input)
        move(energized_board, input_grid, (col_index, len(input_grid[0]) - 1), (0, -1))
        max_result = max(max_result, calculate_energized(energized_board))

    print(max_result)


def calculate_energized(energized_board: list[list[Cell]]) -> int:
    counter: int = 0
    for row in energized_board:
        for cell in row:
            if cell.is_energized():
                counter += 1

    return counter


def move(
    empty_board: list[list[Cell]],
    board: list[list[str]],
    current_position: tuple[int, int],
    direction: tuple[int, int],
) -> None:
    TOTAL_ROWS: int = len(board)
    TOTAL_COLS: int = len(board[1])

    run: bool = True

    while run:
        if empty_board[current_position[0]][current_position[1]].seen(direction):
            run = False
            break

        empty_board[current_position[0]][current_position[1]].add_direction(direction)
        next_position: tuple[int, int] = (
            current_position[0] + direction[0],
            current_position[1] + direction[1],
        )

        if not is_in_bounds(TOTAL_ROWS - 1, TOTAL_COLS - 1, next_position):
            run = False
            break

        direction = update_direction(
            direction, board[next_position[0]][next_position[1]]
        )

        if direction == (2, 0):
            move(empty_board, board, next_position, (-1, 0))
            move(empty_board, board, next_position, (1, 0))
            run = False
            break

        if direction == (0, 2):
            move(empty_board, board, next_position, (0, -1))
            move(empty_board, board, next_position, (0, 1))
            run = False
            break

        current_position = next_position


def convert_to_2D(input: list[str]) -> list[list[str]]:
    arr: list[list[str]] = []
    for row in input:
        line: list[str] = []
        for char in row:
            line.append(char)

        arr.append(line)

    return arr


def get_empty_grid(input: list[str]) -> list[list[Cell]]:
    arr: list[list[Cell]] = []
    for row in input:
        line: list[Cell] = []
        for _ in row:
            line.append(Cell())

        arr.append(line)

    return arr


def update_direction(direction: tuple[int, int], char: str) -> tuple[int, int]:
    if char == "-":
        if direction == (0, 1) or direction == (0, -1):
            return direction
        else:
            return (0, 2)

    if char == "|":
        if direction == (1, 0) or direction == (-1, 0):
            return direction
        else:
            return (2, 0)

    if char == "/":
        if direction == (0, 1):
            return (-1, 0)
        if direction == (1, 0):
            return (0, -1)
        if direction == (-1, 0):
            return (0, 1)
        if direction == (0, -1):
            return (1, 0)

    if char == "\\":
        if direction == (0, 1):
            return (1, 0)
        if direction == (1, 0):
            return (0, 1)
        if direction == (-1, 0):
            return (0, -1)
        if direction == (0, -1):
            return (-1, 0)

    return direction


def is_in_bounds(rows: int, cols: int, position: tuple[int, int]) -> bool:
    if position[0] < 0 or position[0] > rows:
        return False
    if position[1] < 0 or position[1] > cols:
        return False

    return True


if __name__ == "__main__":
    main()
