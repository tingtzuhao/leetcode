class Solution:
    def romanToInt(self, s: str) -> int:
        m = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i, r in enumerate(s):
            if (i <= len(s)-2) and (m[r] < m[s[i+1]]):
                res -= m[r]
            else:
                res += m[r]
        return res