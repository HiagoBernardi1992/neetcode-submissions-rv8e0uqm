class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0

        while l <= r:
            m = l + (r - l) // 2
            square = m * m

            if square > x:
                r = m - 1
            else:
                res = m
                l = m + 1

        return res
