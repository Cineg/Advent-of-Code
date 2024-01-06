from collections import Counter
from dataclasses import dataclass, field


@dataclass
class Module:
    prefix: str = ""
    name: str = ""
    destination_modules: list[str] = field(default_factory=list)
    input_modules: list[str] = field(default_factory=list)
    received_pulses: list[str] = field(default_factory=list)

    state: bool = False

    def relay_pulse(self, signal: str = "", node_name="") -> str:
        if self.prefix == "":
            return "low"

        if signal == "":
            return ""

        if self.prefix == "%":
            if signal == "high":
                return ""

            self.state = not self.state

            if self.state:
                return "high"
            if not self.state:
                return "low"

        if self.prefix == "&":
            index: int = self.input_modules.index(node_name)
            self.received_pulses[index] = signal
            received: dict = Counter(self.received_pulses)

            if len(received) > 1:
                return "high"

            if "low" in received:
                return "high"
            else:
                return "low"


def main() -> None:
    input: list[str] = open("Day 20 - Pulse Propagation\input.txt").read().splitlines()
    modules: dict[str, Module] = get_modules_dict(input)

    pulse_high: int = 0
    pulse_low: int = 0

    # from; where; signal;
    queue: list[tuple[str, str, str]] = []

    for _ in range(1000):
        queue = [("", "button", "low")]
        while queue:
            if queue[0][1] not in modules:
                queue.pop(0)
                continue

            node: Module = modules[queue[0][1]]
            signal: str = queue[0][2]
            received_from: str = queue[0][0]
            queue.pop(0)

            relayed: str = node.relay_pulse(signal, received_from)

            if relayed == "":
                continue

            for item in node.destination_modules:
                if relayed == "high":
                    pulse_high += 1
                else:
                    pulse_low += 1

                queue.append((node.name, item, relayed))

    print(pulse_high * pulse_low)


def get_modules_dict(input: list[str]) -> dict[str, Module]:
    modules: dict = {}
    input_modules: dict = {}
    for item in input:
        a, b = item.split(" -> ")

        if a[0] == "%" or a[0] == "&":
            prefix: str = a[0]
            name: str = a[1:]
        else:
            prefix = ""
            name = a

        output_nodes: list[str] = b.split(", ")

        node = Module(prefix, name, output_nodes)
        modules[name] = node

    for item in modules:
        input_modules[item] = []

    for item in modules:
        for node in modules[item].destination_modules:
            if node in input_modules:
                input_modules[node].append(item)

    for item in modules:
        modules[item].input_modules = input_modules[item]

        received_state: list[str] = []
        for node in modules[item].input_modules:
            received_state.append("low")

        modules[item].received_pulses = received_state

    modules["button"] = Module("", "button", ["broadcaster"])

    return modules


if __name__ == "__main__":
    main()
