# exempel puzzle_input (skall bli 281)
# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# Regler:
# Första och sista siffran skall läggas ihop från varje rad ex rad ett (two1nine) blir 29
# one - nine räknas också som siffror så jag omvandlar dessa.
# om det bara finns en siffra exempelvis 7 så blir talet 77.

calibration_document: list[str] = [
    line for line in open("puzzle_input.txt", "r").read().splitlines()
]

numbers: dict[str, int] = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
answer: int = 0

for line in calibration_document:
    digits: list[int] = []
    for i, c in enumerate(line):
        if c.isdigit():
            digits.append(int(c))
        else:
            for number in numbers:
                if line[i:].startswith(number):
                    digits.append(numbers[number])
    if digits:
        answer += int(str(digits[0]) + str(digits[-1]))

print(answer)
