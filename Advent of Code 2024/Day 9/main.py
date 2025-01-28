from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from pathlib import Path


data: str = open(Path(Path(__file__).parent, "input.txt"), "r").read()


@dataclass
class Node:
    id: int
    slots: int
    isFile: bool = False


def part1() -> int:
    indexes = [Node(idx // 2, int(i), idx % 2 == 0) for idx, i in enumerate(data)]
    checksum: int = 0

    indexes = deque(indexes)
    remaining_node: Node = Node(-1, -1, False)
    remaining_slots: int = -1

    iteration: int = 0
    while indexes:
        node: Node = indexes.popleft()
        if node.isFile:
            while node.slots > 0:
                addition = node.id * iteration
                checksum += addition
                iteration += 1
                node.slots -= 1

        if not node.isFile:
            remaining_slots = node.slots
            while remaining_slots > 0:
                if remaining_node.slots <= 0:
                    remaining_node = _get_right_data(indexes)

                addition = remaining_node.id * iteration
                checksum += addition
                iteration += 1
                remaining_slots -= 1
                remaining_node.slots -= 1

    while remaining_node.slots > 0:
        checksum += remaining_node.id * iteration
        iteration += 1
        remaining_node.slots -= 1

    return checksum


def part2():
    blanks: list[tuple[int, int]] = []
    files: dict[int, tuple[int, int]] = {}
    fid: int = 0
    position: int = 0

    for index, char in enumerate(data):
        space = int(char)
        if index % 2 == 0:
            if space == 0:
                raise ValueError("?")
            files[fid] = (position, space)
            fid += 1
        else:
            if space != 0:
                blanks.append((position, space))

        position += space

    while fid > 0:
        fid -= 1
        pos, size = files[fid]

        i = 0
        while i < len(blanks):
            start, length = blanks[i]
            if start > pos:
                blanks.pop()
                break

            if length < size:
                i += 1
                continue

            if size <= length:
                if size == length:
                    blanks.pop(i)
                else:
                    blanks[i] = (start + size, length - size)

                files[fid] = (start, size)
                break

            i += 1

    total = 0
    for id, (start, size) in files.items():
        for i in range(start, start + size):
            total += id * i

    return total


def _get_right_data(indexes) -> Node:
    data = indexes.pop() if len(indexes) > 0 else Node(-1, -1, False)
    if data.isFile:
        return data
    else:
        return _get_right_data(indexes)


if __name__ == "__main__":
    print(part1())
    print(part2())
