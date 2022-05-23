class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True

# Pythonic
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         newS = ''.join([char.lower() for char in s if char.isalnum()])
#         return newS == newS[::-1]