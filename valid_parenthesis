class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {')': '(', ']': '[', '}': '{'}
        for c in list(s):
            if len(stack) == 0 and c in matches.keys():
                return False
            elif c in matches.keys() and matches[c] == stack[-1]:
                stack.pop(-1)
            else:
                stack.append(c)
        return len(stack) == 0
