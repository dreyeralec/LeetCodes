class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        rd = digits[::-1]
        for i in range(len(rd)):
            if i == len(rd) - 1 and rd[i] == 9:
                rd[i] = 0
                rd.append(1)
                break
            elif rd[i] == 9:
                rd[i] = 0
            else:
                rd[i] += 1
                break
        return rd[::-1]
