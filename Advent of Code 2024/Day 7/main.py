from collections import deque
from pathlib import Path

data: list[str] = (
    open(Path(Path(__file__).parent, "input.txt"), "r").read().splitlines()
)


def day1() -> int:
    total: int = 0
    for row in data:
        result, items = row.split(": ")
        result = int(result)

        numbers = deque([int(i) for i in items.split(" ")])

        results: list[int] = [numbers.popleft()]
        while numbers:
            num: int = numbers.popleft()
            temp: list[int] = []
            while results:
                x: int = results.pop()
                temp.append(num * x)
                temp.append(num + x)

            results = temp

        if result in results:
            total += result

    return total


def day2() -> int:
    total: int = 0
    for row in data:
        result, items = row.split(": ")
        result = int(result)

        numbers = deque([int(i) for i in items.split(" ")])

        results: list[int] = [numbers.popleft()]
        while numbers:
            num: int = numbers.popleft()
            temp: list[int] = []
            while results:
                x: int = results.pop()
                temp.append(num * x)
                temp.append(num + x)
                temp.append(int(str(x) + str(num)))

            results = temp

        if result in results:
            total += result

    return total


if __name__ == "__main__":
    print(day1())
    print(day2())
