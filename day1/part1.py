print(
    sum(
        int(f"{digit[0]}{digit[-1]}")
        for digit in [
            [int(digit) for digit in row if digit.isdigit()]
            for row in open("puzzle_input.txt", "r").read().splitlines()
        ]
    )
)
