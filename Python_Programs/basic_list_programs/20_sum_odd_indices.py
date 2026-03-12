nums = [1, 2, 3, 4, 5, 6]
odd_indices_sum = sum(nums[i] for i in range(len(nums)) if i % 2 != 0)
print(odd_indices_sum)
