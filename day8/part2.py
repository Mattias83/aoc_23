from math import lcm


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


def get_network_node(name: str, instruction: int) -> str:
    network_node: str = ""
    for node in network:
        if node.name == name:
            network_node = node.value[instruction]

    return network_node


def main() -> None:
    # Get starting nodes that end with "A"
    starting_nodes: list[str] = [
        node.name for node in network if node.name.endswith("A")
    ]

    steps: list[int] = []

    for node in starting_nodes:
        step: int = 0
        instruction_step: int = 0
        done: bool = False
        current_node: str = node
        while not done:
            step += 1
            instruction: int = instructions[instruction_step]
            instruction_step = (instruction_step + 1) % len(instructions)
            if get_network_node(current_node, instruction).endswith("Z"):
                steps.append(step)
                done = True
            current_node = get_network_node(current_node, instruction)

    print(lcm(*steps))


if __name__ == "__main__":
    main()
