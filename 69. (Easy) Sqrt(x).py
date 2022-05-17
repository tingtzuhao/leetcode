class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        l, r = 1, x
        while l <= r:
            mid = (l + r) // 2
            mid_sqr = mid * mid
            if mid_sqr == x:
                return mid
            elif mid_sqr > x:
                r = mid - 1
            else:
                l = mid + 1
        return r