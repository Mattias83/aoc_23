GAMES: list[str] = [
    line for line in open("puzzle_input.txt", "r").read().splitlines()
]


class Set:
    def __init__(self, red: int = 0, green: int = 0, blue: int = 0) -> None:
        self.red = red
        self.green = green
        self.blue = blue


class Game:
    def __init__(self, game_row: str) -> None:
        self.game_row = game_row
        self.game_id: int = self._set_game_id()
        self.sets: list[Set] = self._set_game_sets()

    def _set_game_id(self) -> int:
        return int(
            self.game_row[self.game_row.find(" ") : self.game_row.find(":")]
        )

    def _set_game_sets(self) -> None:
        sets_string: str = self.game_row[self.game_row.find(":") + 2 :]
        sets: list[str] = sets_string.split("; ")
        game_sets = []
        for set in sets:
            game_set = set.split(" ")
            new_set = Set()
            for index in range(len(game_set)):
                if game_set[index].replace(",", "") == "red":
                    new_set.red = int(game_set[index - 1])
                elif game_set[index].replace(",", "") == "green":
                    new_set.green = int(game_set[index - 1])
                elif game_set[index].replace(",", "") == "blue":
                    new_set.blue = int(game_set[index - 1])
            game_sets.append(new_set)
        return game_sets

    def is_possible(self) -> int:
        max_red = 12
        max_green = 13
        max_blue = 14

        game_possible = False

        for set in self.sets:
            if (
                set.red <= max_red
                and set.green <= max_green
                and set.blue <= max_blue
            ):
                game_possible = True
            else:
                game_possible = False
                break
        if game_possible:
            return self.game_id
        else:
            return 0


games = [Game(game) for game in GAMES]

total_value = 0

for game in games:
    total_value += game.is_possible()

print(f"Total: {total_value}")
