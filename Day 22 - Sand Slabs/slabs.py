class Brick:
    def __init__(self, startpos: list[int], endpos: list[int], name: str) -> None:
        self.x_coordinates: list[int] = [startpos[0], endpos[0]]
        self.y_coordinates: list[int] = [startpos[1], endpos[1]]
        self.z_coordinates: list[int] = [startpos[2], endpos[2]]
        self.start_z: int = startpos[2]
        self.end_z: int
        self.brick_name: str = name

    def update_z_coordinates(self, z_pos_level: int) -> None:
        if z_pos_level > 0:
            slide: int = abs(z_pos_level - self.z_coordinates[0])
            self.z_coordinates[0] -= slide
            self.z_coordinates[1] -= slide

            self.end_z = self.z_coordinates[0]


def main():
    input: list[str] = open("Day 22 - Sand Slabs\input.txt").read().split("\n")

    snapshot: list[Brick] = get_bricks(input)
    sorted(snapshot, key=lambda x: x.start_z)
    fallen_bricks: list[Brick] = get_final_brick_pos(snapshot)
    sorted(fallen_bricks, key=lambda x: x.end_z)

    supports: dict = {}
    get_support: dict = {}

    disintegrate: list = []

    for brick in fallen_bricks:
        supports[brick.brick_name] = []
        get_support[brick.brick_name] = []

    i: int = len(fallen_bricks) - 1
    while i >= 0:
        base_brick: Brick = fallen_bricks[i]
        for j in range(i - 1, -1, -1):
            fallen_brick: Brick = fallen_bricks[j]

            if base_brick.z_coordinates[1] + 1 != fallen_brick.z_coordinates[0]:
                continue
            if is_in_bounds(base_brick, fallen_brick):
                get_support[fallen_brick.brick_name].append(base_brick.brick_name)
                supports[base_brick.brick_name].append(fallen_brick.brick_name)
        i -= 1

    for key in get_support:
        to_disintegrate: bool = True
        if len(get_support[key]) > 1:
            for supported in supports[key]:
                if len(get_support[supported]) == 1:
                    to_disintegrate = False
                    break
        else:
            for supported in supports[key]:
                if len(get_support[supported]) == 1:
                    to_disintegrate = False
                    break

        if to_disintegrate:
            disintegrate.append(key)

    print(len(disintegrate))

    print("UwU")


def get_bricks(input: list[str]) -> list[Brick]:
    bricks: list = []
    for name, line in enumerate(input):
        start_pos, end_pos = line.split("~")
        start_pos = list(map(int, start_pos.split(",")))
        end_pos = list(map(int, end_pos.split(",")))

        bricks.append(Brick(start_pos, end_pos, str(name)))

    return bricks


def is_in_bounds(base_brick: Brick, falling_brick: Brick) -> bool:
    if base_brick.x_coordinates[1] < falling_brick.x_coordinates[0]:
        return False

    if base_brick.y_coordinates[1] < falling_brick.y_coordinates[0]:
        return False

    return True


def get_final_brick_pos(snapshot: list[Brick]) -> list[Brick]:
    final_pos: list[Brick] = []

    i = 0
    while i < len(snapshot):
        falling_brick: Brick = snapshot[i]

        highest_z: int = 1
        for base_brick in final_pos:
            if is_in_bounds(base_brick, falling_brick):
                highest_z = max(highest_z, base_brick.z_coordinates[1] + 1)

        falling_brick.update_z_coordinates(highest_z)
        final_pos.insert(0, falling_brick)

        i += 1

    return final_pos


if __name__ == "__main__":
    main()
