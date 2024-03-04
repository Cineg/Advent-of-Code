def main():
    input: list[str] = open("Day 19 - Aplenty\input.txt").read().split("\n\n")
    workflows: dict = {}
    workflows = get_workflows(input[0].splitlines())
    ratings: list[tuple] = get_ratings(input[1].splitlines())

    accepted_stack: list = []
    rejected_stack: list = []

    for item in ratings:
        node: tuple = workflows["in"]

        index: int = 0
        while index < len(node):
            condition = node[index]
            if item in accepted_stack or item in rejected_stack:
                break

            if condition[0] == "":
                if condition[1] == "A":
                    accepted_stack.append(item)
                    break
                if condition[1] == "R":
                    rejected_stack.append(item)
                    break
                else:
                    node = workflows[condition[1]]
                    index = 0
                    continue

            if condition[0][1] == "<":
                if int(condition[0][2:]) > int(item[condition[0][0]]):
                    if condition[1] == "A":
                        accepted_stack.append(item)
                        break
                    if condition[1] == "R":
                        rejected_stack.append(item)
                        break

                    node = workflows[condition[1]]
                    index = 0
                    continue

            if condition[0][1] == ">":
                if int(condition[0][2:]) < int(item[condition[0][0]]):
                    if condition[1] == "A":
                        accepted_stack.append(item)
                        break
                    if condition[1] == "R":
                        rejected_stack.append(item)
                        break

                    node = workflows[condition[1]]
                    index = 0
                    continue

            index += 1

    print(count_accepted(accepted_stack))


def get_workflows(input: list[str]) -> dict:
    workflows: dict = {}
    for line in input:
        name, rules = line.split("{")
        rules: str = rules.replace("}", "")

        rule_arr: list = []
        for rule in rules.split(","):
            if len(rule.split(":")) == 1:
                value: str = rule.split(":")[0]
                condition: str = ""
            else:
                condition, value = rule.split(":")

            rule_arr.append((condition, value))

        workflows[name] = rule_arr

    return workflows


def get_ratings(input) -> list:
    ratings: list = []
    for line in input:
        rating: dict = {}
        line: str = line.replace("{", "").replace("}", "")

        for item in line.split(","):
            rating[item[0]] = item[2:]

        ratings.append(rating)

    return ratings


def count_accepted(accepted_stack: list[dict]) -> int:
    total: int = 0
    for item in accepted_stack:
        for key in item:
            total += int(item[key])

    return total


if __name__ == "__main__":
    main()
