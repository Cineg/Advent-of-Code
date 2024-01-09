class Brick:
    def __init__(self, startpos: list[int], endpos: list[int], name: str) -> None:
        self.x_coordinates: list[int] = [startpos[0], endpos[0]]
        self.y_coordinates: list[int] = [startpos[1], endpos[1]]
        self.z_coordinates: list[int] = [startpos[2], endpos[2]]
        self.start_z = startpos[2]
        self.brick_name: str = name

    def update_z_coordinates(self, z_pos_level: int) -> None:
        self.z_coordinates[1] -= self.z_coordinates[0] - z_pos_level
        self.z_coordinates[0] = z_pos_level


def main() -> None:
    input: list[str] = open("Day 22 - Sand Slabs\input.txt").read().split("\n")

    snapshot: list[Brick] = get_bricks(input)
    snapshot.sort(key=lambda x: x.z_coordinates[0])
    fallen_bricks: list[Brick] = get_final_brick_pos(snapshot)
    fallen_bricks.sort(key=lambda x: x.z_coordinates[0])

    supports: dict = {}
    get_support: dict = {}

    disintegrate: list = []

    for brick in fallen_bricks:
        supports[brick.brick_name] = []
        get_support[brick.brick_name] = []

    i: int = 0
    for i, upper_brick in enumerate(fallen_bricks):
        for j, lower_brick in enumerate(fallen_bricks[:i]):
            if (
                is_in_bounds(lower_brick, upper_brick)
                and lower_brick.z_coordinates[1] + 1 == upper_brick.z_coordinates[0]
            ):
                get_support[upper_brick.brick_name].append(lower_brick.brick_name)
                supports[lower_brick.brick_name].append(upper_brick.brick_name)

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

    print(chain_reaction(get_support, supports))


def chain_reaction(supported_by: dict, is_supporting: dict) -> int:
    total = 0

    for start_brick in supported_by:
        queue: list[str] = []
        falling_bricks: list[str] = []

        queue.append(start_brick)
        falling_bricks.append(start_brick)

        while queue:
            supported_bricks: list[str] = is_supporting[queue[0]]
            queue.pop(0)

            for supported_brick in supported_bricks:
                supported_brick_support_count: int = len(supported_by[supported_brick])
                for additional_support_bricks in supported_by[supported_brick]:
                    if (
                        additional_support_bricks == supported_brick
                        or additional_support_bricks in falling_bricks
                    ):
                        supported_brick_support_count -= 1

                if supported_brick_support_count == 0:
                    if supported_brick not in queue:
                        queue.append(supported_brick)

                    if supported_brick not in falling_bricks:
                        falling_bricks.append(supported_brick)

        total += len(falling_bricks) - 1

    return total


def get_bricks(input: list[str]) -> list[Brick]:
    bricks: list = []
    for name, line in enumerate(input):
        start_pos, end_pos = line.split("~")
        start_pos = list(map(int, start_pos.split(",")))
        end_pos = list(map(int, end_pos.split(",")))

        bricks.append(Brick(start_pos, end_pos, str(name)))

    return bricks


def is_in_bounds(base_brick: Brick, falling_brick: Brick) -> bool:
    return max(base_brick.x_coordinates[0], falling_brick.x_coordinates[0]) <= min(
        base_brick.x_coordinates[1], falling_brick.x_coordinates[1]
    ) and max(base_brick.y_coordinates[0], falling_brick.y_coordinates[0]) <= min(
        base_brick.y_coordinates[1], falling_brick.y_coordinates[1]
    )


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
