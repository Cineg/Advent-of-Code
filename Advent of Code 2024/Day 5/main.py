from pathlib import Path

data: str = open(Path(Path(__file__).parent, "input.txt")).read()


class Node:
    def __init__(self, page_number: int) -> None:
        self.page_number: int = page_number
        self.before: set[int] = set()
        self.after: set[int] = set()
        self.value: int = 0


def day1() -> int:
    page_order, page_queue = data.split("\n\n")
    order: dict[int, Node] = get_page_order(page_order)
    order = _update_order(order, True)
    order = _update_order(order, False)

    total = 0
    pq: list[str] = page_queue.split("\n")
    for q in pq:
        queue: list[int] = [int(item) for item in q.split(",")]
        if is_correct_order(queue, order):
            total += queue[round(len(queue) // 2)]

    return total


def get_page_order(page_order: str) -> dict[int, Node]:
    data: dict = {}
    instructions: list[str] = page_order.split("\n")
    for instruction in instructions:
        first, second = tuple(map(lambda x: int(x), instruction.split("|")))

        if first not in data:
            data[first] = Node(first)
        if second not in data:
            data[second] = Node(second)

        data[first].before.add(second)
        data[second].after.add(first)

    return data


def is_correct_order(page_queue: list[int], order: dict[int, Node]):
    i = 0
    while i < len(page_queue) - 1:
        prev: Node = order[page_queue[i]]
        after: Node = order[page_queue[i + 1]]
        if prev.page_number in after.before:
            return False

        i += 1

    return True


def _update_order(data: dict[int, Node], before_after: bool) -> dict[int, Node]:
    for _, node in data.items():
        new_set: set[int] = node.after.copy() if before_after else node.before.copy()
        seen: set = set()
        q: set[int] = node.after.copy() if before_after else node.before.copy()
        while q:
            idx: int = q.pop()
            if idx in seen:
                continue

            if idx == _:
                continue

            check: set[int] = node.before.copy() if before_after else node.after.copy()
            if idx == check:
                continue

            seen.add(idx)
            new: set[int] = (
                data[idx].after.copy().difference(node.before)
                if before_after
                else data[idx].before.copy().difference(node.after)
            )
            new_set.update(new)

            if before_after:
                q.update(data[idx].after)
            else:
                q.update(data[idx].before)

        if before_after:
            node.after = new_set
        else:
            node.before = new_set

    return data


if __name__ == "__main__":
    print(day1())
