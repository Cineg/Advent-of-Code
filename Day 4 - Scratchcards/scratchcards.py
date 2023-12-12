from input import INPUT


def main():
    data: list[str] = INPUT.splitlines()

    total_points: int = 0

    for card in data:
        winning_numbers: dict = get_winning_numers(card)
        card_numbers: dict = get_card_numbers(card)
        card_matches: int = -1
        for item in card_numbers:
            if item in winning_numbers:
                card_matches += 1

        if card_matches != -1:
            total_points += pow(2, card_matches)

    return total_points


def get_winning_numers(card: str) -> dict:
    numbers: str = card.split("|")[0]
    numbers = numbers.split(":")[1]

    winning_numbers: dict = {}
    for number in numbers.split(" "):
        if number.isnumeric() and number not in winning_numbers:
            winning_numbers[number] = number

    return winning_numbers


def get_card_numbers(card: str) -> dict:
    numbers: str = card.split("|")[1]

    card_numbers: dict = {}
    for number in numbers.split(" "):
        if number.isnumeric() and number not in card_numbers:
            card_numbers[number] = number

    return card_numbers


if __name__ == "__main__":
    main()
