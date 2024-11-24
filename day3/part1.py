class PartNumber:
    def __init__(self, number: int, locations: list[tuple]) -> None:
        self.number = number
        self.locations = locations

    def adjecent_to_symbol(self, symbol_locations: list[tuple]) -> bool:

        adjecent: bool = False

        for symbol_coordinate in symbol_locations:
            symbol_x, symbol_y = symbol_coordinate
            for partnr_coordinate in self.locations:
                part_x, part_y = partnr_coordinate
                if symbol_y == part_y:
                    # kolla på samma rad
                    if part_x + 1 == symbol_x or part_x - 1 == symbol_x:
                        adjecent = True
                if symbol_y == (part_y - 1) or symbol_y == (part_y + 1):
                    # kolla ovanför och under nuvarande rad.
                    if (
                        symbol_x == part_x
                        or symbol_x == (part_x - 1)
                        or symbol_x == (part_x + 1)
                    ):
                        adjecent = True

        return adjecent


def is_symbol(character: str) -> bool:
    symbols: list[str] = ["*", "&", "$", "%", "@", "=", "+", "-", "/", "#"]
    return character in symbols


def main() -> None:
    engine_schematic: list[str] = []
    with open("puzzle_input.txt", "r") as schematic:
        engine_schematic = [row.strip() for row in schematic]

    number: str = ""
    x: int = 0
    y: int = 0

    partnumbers: list[PartNumber] = []
    partnr_locations: list[tuple] = []
    symbol_locations: list[tuple] = []

    for row in engine_schematic:
        for c in row:
            if is_symbol(c):
                symbol_locations.append((x, y))
            if c.isdigit():
                number += c
                partnr_locations.append((x, y))
            else:
                if len(number) > 0:
                    partnumbers.append(
                        PartNumber(int(number), partnr_locations.copy())
                    )
                    number = ""
                    partnr_locations.clear()
            x += 1
        y += 1
        x = 0

    total_value: int = 0

    for partnr in partnumbers:
        if partnr.adjecent_to_symbol(symbol_locations):
            total_value += partnr.number

    print(f"Total value: {total_value}")


if __name__ == "__main__":
    main()
