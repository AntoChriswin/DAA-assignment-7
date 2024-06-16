from math import gcd


def countSubarrays(nums, k):
    def lcm(a, b):
        return abs(a * b) // gcd(a, b)

    count = 0
    for i in range(len(nums)):
        current_lcm = 1
        for j in range(i, len(nums)):
            current_lcm = lcm(current_lcm, nums[j])
            if current_lcm == k:
                count += 1
    return count


# Example 1
nums1 = [3, 6, 2, 7, 1]
k1 = 6
print(countSubarrays(nums1, k1))  # Output: 4

# Example 2
nums2 = [3]
k2 = 2
print(countSubarrays(nums2, k2))  # Output: 0
