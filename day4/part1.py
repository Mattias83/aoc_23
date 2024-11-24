def main(scratchcards: list[str]) -> None:

    total_value: int = 0
    card_points: int = 0

    for scratchcard in scratchcards:
        row: str = scratchcard[scratchcard.find(":") + 2 :]
        my_numbers = row.split(" | ")[0]
        winning_numbers = row.split(" | ")[1]
        my_numbers = my_numbers.split(" ")
        winning_numbers = winning_numbers.split(" ")

        for my_number in my_numbers:
            if len(my_number) > 0:
                if my_number in winning_numbers:
                    if card_points == 0:
                        card_points = 1
                    else:
                        card_points = card_points + card_points
        total_value += card_points
        card_points = 0

    print(total_value)


if __name__ == "__main__":
    real_scratchcards: str = "puzzle_input.txt"
    with open(real_scratchcards, "r") as puzzle_input:
        main([row.strip() for row in puzzle_input])
