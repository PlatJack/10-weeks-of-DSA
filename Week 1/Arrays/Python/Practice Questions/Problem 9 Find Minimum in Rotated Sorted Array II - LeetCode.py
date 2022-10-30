# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                return nums[i]
        return nums[0]

# Time Complexity O(n)
# Space Complexity O(1)
