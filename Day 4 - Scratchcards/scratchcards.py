from input import INPUT
from dataclasses import dataclass


@dataclass
class Card:
    copies: int = 1
    winning_points: int = 0


def main():
    data: list[str] = INPUT.splitlines()
    total_points: int = 0
    data_cards: list[Card] = []
    total_cards: int = 0

    for card in data:
        winning_numbers: dict = get_winning_numers(card)
        card_numbers: dict = get_card_numbers(card)
        card_matches: int = -1
        for item in card_numbers:
            if item in winning_numbers:
                card_matches += 1

        if card_matches != -1:
            total_points += pow(2, card_matches)

        item: Card = Card(winning_points=card_matches + 1)
        data_cards.append(item)

    index: int = 0
    while index < len(data_cards):
        i: int = 1
        copies_to_add: int = data_cards[index].winning_points
        if copies_to_add != 0:
            while index + i <= len(data_cards):
                data_cards[index + i].copies += 1 * data_cards[index].copies
                if i != copies_to_add:
                    i += 1
                else:
                    break
        total_cards += data_cards[index].copies
        index += 1

    print(total_cards)
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
