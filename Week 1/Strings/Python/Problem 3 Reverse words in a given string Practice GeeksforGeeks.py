# https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1

class Solution:

    # Function to reverse words in a given string.
    def reverseWords(self, S):
        # code here
        words = S.split('.')
        ans = ''
        for w in words[::-1]:
            ans += w
            ans += '.'
        return ans[: -1]

# Time Complexity O(n)
# Space Complexity O(n)
