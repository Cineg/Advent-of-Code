def main():
    input: list[str] = open("Advent of Code 2022\Day 2\input.txt").read().split("\n")

    figures: dict = {"A": "Rock", "B": "Paper", "C": "Scissors"}
    win_combo: dict = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}
    lose_combo: dict = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
    points: dict = {"Rock": 1, "Paper": 2, "Scissors": 3}

    total_points: int = 0
    for line in input:
        p1, p2 = line.split(" ")

        p1: str = figures[p1]

        if p2 == "Y":
            total_points += points[p1] + 3

        if p2 == "X":
            total_points += points[lose_combo[p1]]

        if p2 == "Z":
            total_points += points[win_combo[p1]] + 6

    print(total_points)
    return total_points


if __name__ == "__main__":
    main()
