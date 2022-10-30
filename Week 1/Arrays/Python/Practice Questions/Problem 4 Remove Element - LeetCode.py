# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        j = 0
        n = len(nums)
        for i in nums:
            if i != val:
                nums[j] = i
                j += 1
        return j

# Time Complexity O(n)
# Space Complexity O(1)
