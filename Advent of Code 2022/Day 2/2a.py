def main():
    input: list[str] = open("Advent of Code 2022\Day 2\input.txt").read().split("\n")

    figures: dict = {
        "X": "Rock",
        "Y": "Paper",
        "Z": "Scissors",
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",
    }

    # for the second player
    wins: set = {("Rock", "Paper"), ("Paper", "Scissors"), ("Scissors", "Rock")}
    points: dict = {"Rock": 1, "Paper": 2, "Scissors": 3}

    total_points: int = 0
    for line in input:
        p1, p2 = line.split(" ")

        p1: str = figures[p1]
        p2: str = figures[p2]

        total_points += points[p2]

        if p1 == p2:
            total_points += 3

        if (p1, p2) in wins:
            total_points += 6

    print(total_points)
    return total_points


if __name__ == "__main__":
    main()
