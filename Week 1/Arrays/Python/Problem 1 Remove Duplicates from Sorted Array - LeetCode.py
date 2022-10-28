# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        prev, j = nums[0], 1
        k = 1
        n = len(nums)
        for i in range(1, n):
            if nums[i] != prev:
                k += 1
                nums[j] = nums[i]
                j += 1
                prev = nums[i]
        return k

# Time Complexity O(n)
# Space Complexity O(1)
