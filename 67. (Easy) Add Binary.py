class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        carry = 0
        res = ''

        for i in range(max(len(a), len(b))):
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0
            digSum = digitA + digitB + carry
            res = str(digSum % 2) + res
            carry = digSum // 2
        if carry == 1:
            res = '1' + res
        return res

# Pythonic
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         return f'{int(a, 2) + int(b, 2):b}'