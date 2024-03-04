MULTIPLIER: int = 17
DIVIDER: int = 256


def main() -> None:
    input: list[str] = open("Day 15 - Lens Library\input.txt").read().split(",")

    total: int = 0
    boxes: dict = dict([(i, []) for i in range(256)])
    sort_boxes(input, boxes)

    for key in boxes:
        box_total: int = 0
        box_multiplier: int = key + 1
        for i, dic in enumerate(boxes[key]):
            position: int = i + 1
            value = int(list(dic.values())[0])

            box_total += box_multiplier * position * value

        total += box_total

    print(total)


def box_label(item: str) -> int:
    item_total: int = 0
    for char in item:
        value: int = item_total
        value += ord(char)
        value *= MULTIPLIER
        value = value % DIVIDER
        item_total = value

    return item_total


def clear_input(item: str) -> tuple[str, str, str]:
    splitter: str = ""
    if "-" in item:
        splitter = "-"
    else:
        splitter = "="

    return item.split(splitter)[0], item.split(splitter)[1], splitter


def get_index_of_dict(key: str, box: list[dict]) -> int:
    for index, value in enumerate(box):
        if key in value:
            return index

    return -1


def sort_boxes(input: list[str], boxes: dict) -> None:
    for item in input:
        item_data: tuple[str, str, str] = clear_input(item)
        box_index: int = box_label(item_data[0])
        box_contents: list[dict] = boxes[box_index]

        item_dct: dict = {item_data[0]: item_data[1]}

        item_index: int = get_index_of_dict(item_data[0], box_contents)
        # remove
        if item_data[2] == "-":
            if item_index != -1:
                box_contents.pop(item_index)

        if item_data[2] == "=":
            if item_index != -1:
                box_contents[item_index] = item_dct
            else:
                box_contents.append(item_dct)

        boxes[box_index] = box_contents


if __name__ == "__main__":
    main()
