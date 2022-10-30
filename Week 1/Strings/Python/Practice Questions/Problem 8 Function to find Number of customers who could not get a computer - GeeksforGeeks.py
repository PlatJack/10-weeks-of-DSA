# https://www.geeksforgeeks.org/function-to-find-number-of-customers-who-could-not-get-a-computer/

from collections import defaultdict


class Solution:
    def customerSimulation(self, n: int, s: str) -> int:
        d = defaultdict(lambda: 0)
        ans = occ = 0
        for i in s:
            if d[i] == 0:
                d[i] = 1

                if occ < n:
                    occ += 1
                    d[i] = 2

                else:
                    ans += 1
            else:
                if d[i] == 2:
                    occ -= 1
                d[i] = 0
        return ans

# Time Complexity O(n)
# Space Complexity O(n)
