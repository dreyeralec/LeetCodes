class Solution:
    def mySqrt(self, x: int) -> int:
        # can be simplified
        if x == 1: return 1
        left = 0
        right = (x // 2) + 1
        while left <= right:
            if left + 1 == right: 
                return left
            mid = (left + right) // 2
            if mid * mid > x:
                right = mid
            elif mid * mid < x:
                left = mid
            else:
                return mid
        return left
