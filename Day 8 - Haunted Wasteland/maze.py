from dataclasses import dataclass


@dataclass
class Node:
    value: str
    left: str
    right: str


def main() -> None:
    input: list[str] = open("Day 8 - Haunted Wasteland\input.txt").read().splitlines()
    instructions: str = input[0]

    nodes: dict = _get_nodes_dict(input)

    part_a(instructions, nodes, "AAA")


def _get_nodes_dict(input: list[str]) -> dict:
    nodes: dict = {}

    for item in input[2:]:
        value: str = item.split(" =")[0]
        left: str = item.split("(")[1].split(",")[0]
        right: str = item.split("(")[1].split(", ")[1].split(")")[0]
        node: Node = Node(value, left, right)

        if value not in nodes:
            nodes[value] = node

    return nodes


def part_a(instructions: str, nodes: dict, actual_value: str) -> None:
    steps: int = 0

    run: bool = True
    while run:
        i = 0
        while i < len(instructions):
            if nodes[actual_value].value == "ZZZ":
                run = False
                break

            if instructions[i] == "L":
                actual_value = nodes[actual_value].left
            else:
                actual_value = nodes[actual_value].right

            i += 1
            steps += 1

    print(f"part a: {steps}")


if __name__ == "__main__":
    main()
