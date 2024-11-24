from collections import Counter

# Example puzzle input
puzzle_input: list[str] = [
    "32T3K 765",  # One pair (33)
    "T55J5 684",  # Three of a kind (555)
    "KK677 28",  # Two pair (KK & 77)
    "KTJJT 220",  # Two pair (TT & JJ)
    "QQQJA 483",  # Three of a kind (QQQ)
]

# Real puzzle input (Comment out to use Example input...)
puzzle_input: list[str] = open("puzzle_input.txt", "r").read().splitlines()


# card values dict adding card values from 2 - 9
card_values: dict[str, int] = {
    str(key): value for key, value in zip(range(2, 10), range(2, 10))
}
# Adds T, J, Q, K & A cards
card_values.update({"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14})


class Hand:
    def __init__(self, puzzle_input_row: str) -> None:
        self.cards: list[str] = [*puzzle_input_row.split(" ")[0]]
        self.cards_as_values = list(map(self._get_card_value, self.cards))
        self.bid: int = int(puzzle_input_row.split(" ")[1])
        self.hand_type = self._get_hand_type()

    def _get_card_value(self, card) -> int:
        return card_values[card]

    def get_hand_rank(self) -> int:
        ranks = {
            "Five of a kind": 7,
            "Four of a kind": 6,
            "Full house": 5,
            "Three of a kind": 4,
            "Two pair": 3,
            "One pair": 2,
            "High card": 1,
        }
        return ranks[self.hand_type]

    def _get_hand_type(self) -> str:
        counted_cards: list[int] = sorted(
            Counter(self.cards).values(), reverse=True
        )
        if counted_cards == [5]:
            return "Five of a kind"
        elif counted_cards == [4, 1]:
            return "Four of a kind"
        elif counted_cards == [3, 2]:
            return "Full house"
        elif counted_cards == [3, 1, 1]:
            return "Three of a kind"
        elif counted_cards == [2, 2, 1]:
            return "Two pair"
        elif counted_cards == [2, 1, 1, 1]:
            return "One pair"
        return "High card"


def rank_hands(hands: list[Hand]) -> list[Hand]:
    """
    Given a list of Hand objects, returns the list sorted from
    strongest to weakest hand based on hand rank (Five of a kind -
    High card) and card values where cards are read from left to right.

    The sorted list contains the strongest hand as the first element
    and the weakest hand as the last element.
    """
    return sorted(
        hands,
        key=lambda hand: (hand.get_hand_rank(), hand.cards_as_values),
        reverse=True,
    )


def main() -> None:
    ranked_hands: list[Hand] = rank_hands(
        hands=[Hand(row) for row in puzzle_input]
    )

    total_winnings: int = sum(
        hand.bid * (len(ranked_hands) - index)
        for index, hand in enumerate(ranked_hands)
    )

    if len(puzzle_input) > 5:
        assert total_winnings == 247815719
    else:
        assert total_winnings == 6440

    print(f"Total winnings: {total_winnings}")


if __name__ == "__main__":
    main()
