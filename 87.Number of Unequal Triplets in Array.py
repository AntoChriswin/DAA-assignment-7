def count_good_triplets(nums):
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                    count += 1
    return count

# Example 1
nums1 = [4, 4, 2, 4, 3]
print(count_good_triplets(nums1))  # Output: 3

# Example 2
nums2 = [1, 1, 1, 1, 1]
print(count_good_triplets(nums2))  # Output: 0
