from dataclasses import dataclass
from input import INPUT


@dataclass
class Game:
    blue: int = 0
    red: int = 0
    green: int = 0

    max_blue: int = 14
    max_red: int = 12
    max_green: int = 13

    def IsValidGame(self) -> bool:
        if (
            self.blue > self.max_blue
            or self.red > self.max_red
            or self.green > self.max_green
        ):
            return False
        return True


def main():
    total_result: int = 0
    data: list[str] = INPUT.splitlines()
    for line in data:
        games: list[str] = _get_games(line)
        if _get_result(games):
            total_result += _get_gameID(line)

    print(total_result)


def _get_gameID(line: str) -> int:
    return int(line.split(":")[0].split(" ")[1])


def _get_games(line: str) -> list[str]:
    game_line: str = line.split(":")[1]
    return game_line.split(";")


def _get_result(games: list[str]) -> bool:
    for game in games:
        dct: dict[str, int] = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        dices: list[str] = game.split(",")
        for dice in dices:
            for color in dct:
                if dice.find(color) != -1:
                    txt: str = dice.replace(color, "")
                    dct[color] = int(txt.strip())

            game_check: Game = Game(
                red=dct["red"], green=dct["green"], blue=dct["blue"]
            )
            if game_check.IsValidGame() == False:
                return False

    return True


if __name__ == "__main__":
    main()
