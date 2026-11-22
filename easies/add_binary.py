class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # far from most elegant solution but its what I came up with
        carry = 0
        top = list(a) if len(a) >= len(b) else list(b)
        bot = a if len(a) < len(b) else b
        for i in range(len(top)):
            if i >= len(bot) and i != len(top):
                s = carry + int(top[-1 - i])
            else:
                s = carry + int(top[-1 - i]) + int(bot[-1 - i])
            if s == 1:
                top[-1 - i] = 1
                carry = 0
            elif s == 2:
                top[-1 - i] = 0
                carry = 1
            elif s == 3:
                top[-1 - i] = 1
                carry = 1
        if carry == 1:
            top.insert(0, 1)
        return "".join(map(str, top))
