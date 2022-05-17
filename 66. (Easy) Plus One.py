class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        i, carry = 0, 1
        while carry == 1:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = 0
            else:
                digits.append(1)
                carry = 0
            i += 1
        return digits[::-1]

### Pythonic ##
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         addOne = int(''.join([str(d) for d in digits])) + 1
#         return [d for d in str(addOne)]