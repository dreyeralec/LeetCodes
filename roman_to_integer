class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        out = 0
        rsl = list(s[::-1])
        for i, c in enumerate(rsl):
            if i == 0: out += nums[c]
            elif nums[rsl[i-1]] > nums[c]:
                out -= nums[c]
            else:
                out += nums[c]
        return out
