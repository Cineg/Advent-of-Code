from dataclasses import dataclass
from enum import Enum


class Hand_Strength(Enum):
    default = 0
    high_card = 1
    one_pair = 2
    two_pair = 3
    three_of_a_kind = 4
    full_house = 5
    four_of_a_kind = 6
    five_of_a_kind = 7


@dataclass
class Hand:
    cards: str
    bid: int
    strength: Hand_Strength = Hand_Strength.default

    def get_strength(self) -> None:
        dct_cards: dict = {}
        for card in self.cards:
            if card in dct_cards:
                dct_cards[card] += 1
            else:
                dct_cards[card] = 1

        if len(dct_cards) == 5:
            self.strength = Hand_Strength.high_card
        if len(dct_cards) == 4:
            self.strength = Hand_Strength.one_pair
        if len(dct_cards) == 3:
            is_three: bool = False
            for card in dct_cards:
                if dct_cards[card] == 3:
                    is_three = True
                    break
            if is_three:
                self.strength = Hand_Strength.three_of_a_kind
            else:
                self.strength = Hand_Strength.two_pair

        if len(dct_cards) == 2:
            for card in dct_cards:
                if dct_cards[card] == 3 or dct_cards[card] == 2:
                    self.strength = Hand_Strength.full_house
                else:
                    self.strength = Hand_Strength.four_of_a_kind
                break

        if len(dct_cards) == 1:
            self.strength = Hand_Strength.five_of_a_kind


def main() -> None:
    input: list[str] = open("Day 7 - Camel Cards//input.txt").read().splitlines()
    hands: list[Hand] = []
    total: int = 0

    index: int = 1
    for line in input:
        hand: Hand = Hand(line.split()[0], int(line.split()[1]))
        hand.get_strength()
        hands.append(hand)
        index += 1

    sort_cards(hands)

    index: int = 1
    for hand in hands:
        hand_total: int = hand.bid * index
        total += hand_total
        index += 1

    print(total)


def isHand1Better(hand1: Hand, hand2: Hand) -> bool:
    if hand1.strength.value > hand2.strength.value:
        return True
    if hand1.strength.value < hand2.strength.value:
        return False

    dct_values: dict = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
    }

    index: int = 0
    while index < len(hand1.cards):
        if dct_values[hand1.cards[index]] > dct_values[hand2.cards[index]]:
            return True
        if dct_values[hand1.cards[index]] < dct_values[hand2.cards[index]]:
            return False
        index += 1

    return False


def sort_cards(array: list[Hand]) -> None:
    length: int = len(array)
    for i in range(0, length - 1):
        for j in range(0, length - i - 1):
            if isHand1Better(array[j], array[j + 1]):
                temp: Hand = array[j + 1]
                array[j + 1] = array[j]
                array[j] = temp


if __name__ == "__main__":
    main()
