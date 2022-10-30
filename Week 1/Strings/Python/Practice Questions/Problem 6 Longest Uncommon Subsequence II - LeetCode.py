# https://leetcode.com/problems/longest-uncommon-subsequence-ii/

class Solution:
    def findLUSlength(self, strs: list[str]) -> int:
        def isSub(x, y):
            i = j = 0
            while i < len(x) and j < len(y):
                if x[i] == y[j]:
                    i += 1
                j += 1
            return i == len(x)

        strs.sort(key=len, reverse=True)
        n = len(strs)

        for i in range(n):
            stat = True
            for j in range(n):
                if (i != j and isSub(strs[i], strs[j])):
                    stat = False
                    break
            if stat:
                return len(strs[i])

        return -1

# Time Complexity O(n ^ 2)
# Space Complexity O(1)
