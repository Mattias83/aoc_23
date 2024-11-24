class Node:
    def __init__(self, name: str, value: tuple[str, str]):
        self.name = name
        self.value = value


# Puzzle input
pz = open("puzzle_input.txt", "r").read().splitlines()

# Instructions converted R & L to 1 & 0
instructions: list[int] = [
    1 if instruction == "R" else 0 for instruction in pz[0]
]

# List of network nodes created from puzzle input
network: list[Node] = [
    Node(row[0:3], (row[7:10], row[12:15])) for row in pz[2:]
]


def get_network_node(name, instruction) -> str:
    network_node: str = ""
    for node in network:
        if node.name == name:
            network_node = node.value[instruction]

    return network_node


def main() -> None:
    zzz_found: bool = False
    steps: int = 0

    instruction_step: int = 0  # instructions repat until ZZZ is found

    # Initial network node is always "AAA"
    network_node: str = "AAA"

    while not zzz_found:
        steps += 1
        instruction: int = instructions[instruction_step]
        if get_network_node(network_node, instruction) == "ZZZ":
            zzz_found = True

        network_node = get_network_node(network_node, instruction)
        instruction_step += 1
        if instruction_step == len(instructions):
            instruction_step = 0

    print(f"Steps to find ZZZ {steps}")


if __name__ == "__main__":
    main()
