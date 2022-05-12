class Solution:
    def isValid(self, s: str) -> bool:
        opening = []
        for char in s:
            if opening:
                if opening[-1] == '(' and char == ')':
                    opening.pop()
                elif opening[-1] == '[' and char == ']':
                    opening.pop()
                elif opening[-1] == '{' and char == '}':
                    opening.pop()
                else:
                    opening.append(char)
            else:
                opening.append(char)
        return len(opening) == 0