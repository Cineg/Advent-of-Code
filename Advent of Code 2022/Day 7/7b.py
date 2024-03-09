from dataclasses import dataclass, field


@dataclass
class Directory:
    name: str
    parent_dir: str = ""
    dirs: list[str] = field(default_factory=list)
    files: dict[str, int] = field(default_factory=dict)

    def add_folder(self, dir_name: str) -> None:
        if dir_name not in self.dirs:
            self.dirs.append(dir_name)

    def add_file(self, file_name: str, size: int) -> None:
        if file_name not in self.files:
            self.files[file_name] = size

    def get_dir_size(self, directories: dict) -> int:
        size: int = 0
        for file in self.files:
            size += self.files[file]

        for folder in self.dirs:
            dir: Directory = directories[folder]
            size += dir.get_dir_size(directories=directories)

        return size


def main() -> None:
    input: list[str] = open("Advent of Code 2022\\Day 7\\input.txt").read().split("\n")

    root: Directory = Directory("/", "/")
    dirs: dict = {"/": root}
    dir: Directory = root

    for line in input:
        if line[0] == "$":
            if "$ cd " in line:
                cd_dir: str = line.split("$ cd ")[1]

                if cd_dir == "/":
                    dir = dirs["/"]
                    continue

                if cd_dir == "..":
                    cd_dir = dir.parent_dir
                    dir = dirs[cd_dir]
                    continue

                cd_dir = f"{dir.name}/{cd_dir}"

                if cd_dir not in dirs:
                    new_dir: Directory = Directory(cd_dir, dir.name)
                    dirs[cd_dir] = new_dir

                else:
                    dir = dirs[cd_dir]

            if "$ ls" in line:
                pass
        else:
            if "dir " in line:
                name: str = line.split(" ")[1]
                name = f"{dir.name}/{name}"
                dir.add_folder(dir_name=name)
                new_dir: Directory = Directory(name, dir.name)
                dirs[name] = new_dir
            else:
                name: str = line.split(" ")[1]
                size: int = int(line.split(" ")[0])
                dir.add_file(name, size)

    target_to_remove: int = 30000000 - (70000000 - dirs["/"].get_dir_size(dirs))
    remove: int = dirs["/"].get_dir_size(dirs)
    for dir in dirs:
        directory: Directory = dirs[dir]
        dir_size: int = directory.get_dir_size(dirs)

        if dir_size >= target_to_remove:
            remove = min(remove, dir_size)

    print(remove)


if __name__ == "__main__":
    main()
