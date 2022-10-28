# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ''
        for i in s:
            if i.isalpha():
                temp += i.lower()
            if i.isdigit():
                temp += i
        return temp == temp[::-1]

# Time Complexity O(n)
# Space Complexity O(n)
