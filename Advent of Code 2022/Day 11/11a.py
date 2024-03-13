from dataclasses import dataclass
from heapq import heappushpop


@dataclass
class Monkey:
    items: list[int]
    operation: tuple[str, str]
    division_test: int
    division_true: int
    division_false: int

    inspection_count: int = 0

    def monkey_business(self) -> list[tuple[int, int]]:
        throws: list[tuple] = []
        while self.items:
            item: int = self.items.pop(0)
            self.inspection_count += 1

            value: int = self.calculate(item)
            value = value // 3

            if value % self.division_test == 0:
                throws.append((self.division_true, value))
            else:
                throws.append((self.division_false, value))

        return throws

    def calculate(self, item: int) -> int:
        operation, val = self.operation

        if val.isnumeric():
            value: int = int(val)
        else:
            value = item

        if operation == "+":
            value = item + value
        if operation == "*":
            value = item * value

        return value

    def receive_item(self, item: int) -> None:
        self.items.append(item)


def main() -> None:
    input: dict[int, Monkey] = _get_input()

    i: int = 0
    while i < 20:
        for index in input:
            monkey: Monkey = input[index]
            throw: list[tuple[int, int]] = monkey.monkey_business()
            for item in throw:
                input[item[0]].receive_item(item[1])

        i += 1

    top: list[int] = [0, 0]
    for index in input:
        heappushpop(top, input[index].inspection_count)

    print(top[0] * top[1])


def _get_input() -> dict[int, Monkey]:
    input: list[str] = (
        open("Advent of Code 2022\Day 11\\input.txt").read().split("\n\n")
    )
    monkeys: dict[int, Monkey] = {}

    for monkey in input:
        num: int = -1
        operation: tuple[str, str]
        starting_items: list[int] = []
        division_test: int = -1
        division_true: int = -1
        division_false: int = -1

        for line in monkey.split("\n"):
            if "Monkey " in line:
                num = int(line[-2])

            if "Starting items" in line:
                starting_items = list(map(int, line.split(":")[1].split(",")))

            if "Operation" in line:
                x = line.split(" = ")[1]
                operation = (x.split(" ")[-2], x.split(" ")[-1])

            if "Test" in line:
                division_test = int(line.split(" ")[-1])

            if "true" in line:
                division_true = int(line.split(" ")[-1])

            if "false" in line:
                division_false = int(line.split(" ")[-1])

        monkey_obj: Monkey = Monkey(
            starting_items, operation, division_test, division_true, division_false
        )

        monkeys[num] = monkey_obj

    return monkeys


if __name__ == "__main__":
    main()
