# https://codeforces.com/problemset/problem/1746/B

class Solution:
    def solve():
        for _ in range(int(input())):
            n = int(input())
            a = list(map(int, input().split()))
            i, j = 0, n - 1
            ans = 0
            while i < n and a[i] == 0:
                i += 1
            while j >= 0 and a[j] == 1:
                j -= 1
            ans = 0
            while i < j:
                while i < n and a[i] == 0:
                    i += 1
                while j >= 0 and a[j] == 1:
                    j -= 1
                if i < j:
                    ans += 1
                    i += 1
                    j -= 1
            print(ans)

# Time Complexity O(n ^ 2)
# Space Complexity O(1)
