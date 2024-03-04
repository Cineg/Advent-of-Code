from dataclasses import dataclass


@dataclass
class Hail:
    pos_x: int
    pos_y: int
    pos_z: int

    vel_x: int
    vel_y: int
    vel_z: int

    start_pos_x: int = 0
    end_pos_x: int = 0

    start_pos_y: int = 0
    end_pos_y: int = 0

    start_pos_z: int = 0
    end_pos_z: int = 0

    def calculate_end_positions(self, start: int, end: int) -> None:
        # guard clauses

        if (
            self.pos_x < start
            and self.vel_x <= 0
            and self.pos_x > end
            and self.vel_x >= 0
            and self.pos_y < start
            and self.vel_y >= 0
            and self.pos_y > end
            and self.vel_x >= 0
        ):
            return

        current_x: int = self.pos_x
        current_y: int = self.pos_y

        started: bool = False
        run: bool = True
        while run:
            if self.start_pos_x != 0:
                started = True

            if (
                started
                and start > current_x
                or start > current_y
                or end < current_x
                or end < current_y
            ):
                run = False
                continue

            if start <= current_x <= end and start <= current_y <= end:
                if self.start_pos_x == 0:
                    self.start_pos_x = current_x
                else:
                    self.start_pos_x = min(current_x, self.start_pos_x)

                if self.end_pos_x == 0:
                    self.end_pos_x = current_x
                else:
                    self.end_pos_x = max(current_x, self.end_pos_x)

                if self.start_pos_y == 0:
                    self.start_pos_y = current_x
                else:
                    self.start_pos_y = min(current_y, self.start_pos_y)

                if self.end_pos_y == 0:
                    self.end_pos_y = current_y
                else:
                    self.end_pos_y = max(current_y, self.end_pos_y)

            current_x += self.vel_x
            current_y += self.vel_y


def main() -> None:
    data: list[Hail] = get_input_data()

    for item in data:
        item.calculate_end_positions(7, 27)

    print("UwU")


def will_cross(hail1: Hail, hail2: Hail) -> bool:
    cross_x: bool = False
    cross_y: bool = False

    if hail1.pos_x < hail2.pos_x:
        if hail1.vel_x <= hail2.vel_x:
            return False
        if hail1.vel_x > hail2.vel_x:
            cross_x = True

    if hail1.pos_x > hail2.pos_x:
        if hail1.vel_x >= hail2.vel_x:
            return False
        if hail1.vel_x < hail2.vel_x:
            cross_x = True

    if hail1.pos_y < hail2.pos_y:
        if hail1.vel_y <= hail2.vel_y:
            return False
        if hail1.vel_y > hail2.vel_y:
            cross_y = True

    if hail1.pos_y > hail2.pos_y:
        if hail1.vel_y >= hail2.vel_y:
            return False
        if hail1.vel_y < hail2.vel_y:
            cross_y = True

    if hail1.pos_x == hail2.pos_x:
        cross_x = True
    if hail1.pos_y == hail2.pos_y:
        cross_x = True

    return cross_x == True and cross_y == True


def get_input_data() -> list[Hail]:
    input: list[str] = (
        open("Day 24 - Never Tell Me The Odds\input.txt").read().splitlines()
    )
    items: list[Hail] = []
    for hail in input:
        item = list(map(int, hail.replace(" @ ", ",").split(",")))
        items.append(Hail(item[0], item[1], item[2], item[3], item[4], item[5]))

    return items


if __name__ == "__main__":
    main()
