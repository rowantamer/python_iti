def reduce_adjacent_duplicates(nums):
    reduced_nums = []
    prev_num = None
    for num in nums:
        if num != prev_num:
            reduced_nums.append(num)
            prev_num = num
    return reduced_nums

nums = [1, 2, 3, 3]
nums =reduce_adjacent_duplicates(nums)
print (nums)