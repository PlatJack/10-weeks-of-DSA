# https://leetcode.com/problems/maximum-gap/

import collections


class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        n = len(nums)
        l, h = min(nums), max(nums)

        if n <= 2 or l == h:
            return h - l

        d = collections.defaultdict(list)

        for i in nums:
            buc = n - 1 if i == h else (i - l) * (n - 1) // (h - l)
            d[buc].append(i)

        poss = [[min(d[i]), max(d[i])] for i in range(n) if d[i]]

        return max(x[0] - y[1] for x, y in zip(poss[1:], poss))

# Time Complexity O(nlogn)
# Space Complexity O(n ^ 2)
