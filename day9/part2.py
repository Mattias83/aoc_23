test = [[10, 13, 16, 21, 30, 45], [1, 3, 6, 10, 15, 21], [0, 3, 6, 9, 12, 15]]

reports = [
    [int(num) for num in row.split(" ")]
    for row in open("puzzle_input.txt", "r").read().splitlines()
]


def calc(nums):
    if all(num == 0 for num in nums):
        return 0
    diff = []
    for index in range(len(nums) - 1):
        diff.append(nums[index + 1] - nums[index])
    return nums[0] - calc(diff)


print(sum(calc(num) for num in reports))
