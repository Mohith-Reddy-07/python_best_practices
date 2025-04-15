def two_sum(nums, target):
    num_map = {}  # to store num: index
    for i, num in enumerate(nums):
        diff = target - num
        if diff in num_map:
            return [num_map[diff], i]
        num_map[num] = i

print(two_sum([2, 7, 11, 15], 9)) 