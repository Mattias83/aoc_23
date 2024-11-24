def main(scratchcards: list[str]) -> None:
    total_cards: list[int] = [1] * len(scratchcards)
    for card_index, card in enumerate(scratchcards):
        my_numbers: list[int] = [
            int(index)
            for index in card[card.find(":") + 2 :].split(" | ")[0].split(" ")
            if index.isdigit()
        ]

        winning_numbers: list[int] = [
            int(index)
            for index in card[card.find(":") + 2 :].split(" | ")[1].split(" ")
            if index.isdigit()
        ]

        wins: int = 0

        for num in my_numbers:
            for win in winning_numbers:
                if num == win:
                    wins += 1

        for index in range(wins):
            total_cards[card_index + 1 + index] += total_cards[card_index]

    print(sum(total_cards))


if __name__ == "__main__":
    real_scratchcards = "puzzle_input.txt"
    with open(real_scratchcards, "r") as puzzle_input:
        main([row.strip() for row in puzzle_input])
