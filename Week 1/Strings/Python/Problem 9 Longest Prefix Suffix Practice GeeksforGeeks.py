# https://practice.geeksforgeeks.org/problems/longest-prefix-suffix2527/1

class Solution:
    def lps(self, s):
        n = len(s)
        for res in range(n // 2, 0, -1):
            prefix = s[0: res]
            suffix = s[n - res: n]
            if (prefix == suffix):
                return res
        return 0

# Time Complexity O(n)
# Space Complexity O(n)
