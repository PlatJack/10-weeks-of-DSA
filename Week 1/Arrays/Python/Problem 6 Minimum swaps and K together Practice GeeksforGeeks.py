# https://practice.geeksforgeeks.org/problems/minimum-swaps-required-to-bring-all-elements-less-than-or-equal-to-k-together4847/1?page=2&difficulty[]=1&category[]=Arrays&sortBy=submissions

class Solution:
    def minSwap(arr, n, k):
        winsize = 0
        for i in arr:
            if i <= k:
                winsize += 1

        cnt = 0

        for i in arr[: winsize]:
            if i > k:
                cnt += 1

        ans = cnt

        for i in range(winsize, n):
            if arr[i - winsize] <= k and arr[i] > k:
                cnt += 1
            elif arr[i - winsize] > k and arr[i] <= k:
                cnt -= 1
            ans = min(ans, cnt)

        return ans

# Time Complexity O(n)
# Space Complexity O(n)
