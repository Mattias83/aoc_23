from enum import Enum


class Position:
    """
    Position class determine location of tile in GRID.
    """

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, position: "Position") -> "Position":
        return Position(self.x + position.x, self.y + position.y)


class Direction(Enum):
    """
    Simplifies direction with enum class, use UP,RIGHT, DOWN, LEFT to
    navigate GRID.
    """

    UP = Position(0, -1)
    RIGHT = Position(1, 0)
    DOWN = Position(0, 1)
    LEFT = Position(-1, 0)

    # Method for returning opposite direction to current instance
    def opposite(self) -> "Direction":
        if self == Direction.UP:
            return Direction.DOWN
        elif self == Direction.DOWN:
            return Direction.UP
        elif self == Direction.RIGHT:
            return Direction.LEFT
        elif self == Direction.LEFT:
            return Direction.RIGHT


# Dictionary to lookup directions for specified pipes.
PIPES: dict[str, dict[Direction, Direction]] = {
    "|": [Direction.UP, Direction.DOWN],
    "-": [Direction.LEFT, Direction.RIGHT],
    "L": [Direction.UP, Direction.RIGHT],
    "J": [Direction.UP, Direction.LEFT],
    "7": [Direction.DOWN, Direction.LEFT],
    "F": [Direction.DOWN, Direction.RIGHT],
    "S": [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT],
}


class Tile:
    """
    Tile class contains information about tile, like position in GRID
    and if its a pipe.
    """

    def __init__(self, tile: str, position: Position) -> None:
        self.tile = tile
        self.position = position
        self.is_pipe = self.tile in PIPES

    def can_move(self, direction) -> bool:
        return direction in PIPES[self.tile]

    def __str__(self) -> str:
        return self.tile


"""
Generates the GRID. 
Looks like:
[ 
    [Tile, Tile, Tile, Tile ...], 
    ... 
]
"""
GRID: list[list[Tile]] = [
    [Tile(tile, Position(x, y)) for x, tile in enumerate(row)]
    for y, row in enumerate(open("puzzle_input.txt", "r").read().splitlines())
]


def get_starting_position(grid: list[list[Tile]] = GRID) -> Position:
    """
    Returns starting position in GRID "S".
    """
    return next(
        (tile.position for row in grid for tile in row if tile.tile == "S"),
        None,
    )


def get_tile(grid: list[list[Tile]], position: Position) -> Tile:
    """
    Return a tile from the GRID
    """
    x = position.x
    y = position.y
    if x >= 0 and x <= len(grid[0]) and y >= 0 and y <= len(grid):
        return grid[y][x]


starting_position = get_starting_position()
current_pos = starting_position
moves = []
last_successful_direction = None
done = False

while not done:
    current_tile = get_tile(GRID, current_pos)

    # Tries available direction for current pipe
    for direction in PIPES[current_tile.tile]:
        # Skip direction if its opposite to last successful direction move.
        if (
            last_successful_direction
            and direction == last_successful_direction.opposite()
        ):
            continue

        # Get tile from next position
        next_pos = current_tile.position + direction.value
        dest_tile = get_tile(GRID, next_pos)

        # Skips direction if dest_tile is None or not a pipe
        if not dest_tile or not dest_tile.is_pipe:
            continue

        if dest_tile.can_move(direction.opposite()):
            # We have reached starting position and are done.
            if dest_tile.tile == "S":
                done = True
                break

            # Update current position to the new tile and start over.
            current_pos = next_pos
            moves.append(dest_tile)
            last_successful_direction = direction
            break

# Puzzle answer
print("Farthest move from starting position", int((len(moves) + 1) / 2))
