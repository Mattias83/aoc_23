# Puzzle input
reports: list[list[int]] = [
    [int(num) for num in row.split(" ")]
    for row in open("puzzle_input.txt", "r").read().splitlines()
]


def solve(nums: list[int]) -> int:
    if all(num == 0 for num in nums):
        return 0
    diff: list[int] = []
    for index in range(len(nums) - 1):
        diff.append(nums[index + 1] - nums[index])
    print(diff)
    return nums[-1] + solve(diff)


def main() -> None:

    print(sum(solve(num) for num in reports))


if __name__ == "__main__":
    main()
