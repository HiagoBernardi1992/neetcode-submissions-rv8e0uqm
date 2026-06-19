class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0
        while l <= r:
            m = l + (r - l) // 2
            result = m**2
            if  result > x:
                r = m - 1
            elif result < x:
                l = m + 1
                res = m
            else:
                return m

        return res