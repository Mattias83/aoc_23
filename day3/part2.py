class PartNumber:
    def __init__(self, number: int, coordinates: list[tuple]) -> None:
        self.number = number
        self.coordinates = coordinates
        self.adjacent_gear_coordiante: tuple = (0, 0)

    def is_adjacent_to_gear(self, gear_coordinates: list[tuple]) -> bool:
        adjacent: bool = False
        for part_coordinate in self.coordinates:
            part_x, part_y = part_coordinate
            for gear_coordinate in gear_coordinates:
                gear_x, gear_y = gear_coordinate
                if gear_y == part_y:
                    # same row
                    if gear_x == (part_x + 1) or gear_x == (part_x - 1):
                        adjacent = True
                        self.adjacent_gear_coordiante = (gear_x, gear_y)
                if gear_y == (part_y + 1) or gear_y == (part_y - 1):
                    # row below or over current row
                    if (
                        gear_x == part_x
                        or gear_x == (part_x - 1)
                        or gear_x == (part_x + 1)
                    ):
                        adjacent = True
                        self.adjacent_gear_coordiante = (gear_x, gear_y)
        return adjacent


def get_gear_coordinates(engine_schematic: list[str]) -> list[tuple]:
    x: int = 0
    y: int = 0
    gear_coordinates: list[tuple] = []
    for row in engine_schematic:
        for c in row:
            if c == "*":
                gear_coordinates.append((x, y))
            x += 1
        y += 1
        x = 0

    return gear_coordinates


def get_partnumbers(engine_schematic: list[str]) -> list[PartNumber]:
    part_numbers: list[PartNumber] = []
    coordinates: list[tuple] = []
    number: str = ""
    x: int = 0
    y: int = 0

    for row in engine_schematic:
        for c in row:
            if c.isdigit():
                number += c
                coordinates.append((x, y))
            else:
                if len(number) > 0:
                    part_numbers.append(
                        PartNumber(int(number), coordinates.copy())
                    )
                    number = ""
                    coordinates.clear()
            x += 1
        y += 1
        x = 0

    return part_numbers


def main(engine_schematic: list[str]) -> None:
    gear_coordinates: list[tuple] = get_gear_coordinates(engine_schematic)
    part_numbers: list[PartNumber] = get_partnumbers(engine_schematic)

    total_value: int = 0

    for partnr in part_numbers:
        if partnr.is_adjacent_to_gear(gear_coordinates):
            for index in range(len(part_numbers)):
                if (
                    partnr.adjacent_gear_coordiante
                    == part_numbers[index].adjacent_gear_coordiante
                    and partnr.number != part_numbers[index].number
                ):
                    gear_ratio: int = (
                        partnr.number * part_numbers[index].number
                    )
                    total_value += gear_ratio

    print(total_value)


if __name__ == "__main__":
    schematic: str = "puzzle_input.txt"
    with open(schematic, "r") as schematic:
        main([row.strip() for row in schematic])
