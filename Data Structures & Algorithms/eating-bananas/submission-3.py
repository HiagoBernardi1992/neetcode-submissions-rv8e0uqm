class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def getHours(speed):
            hours = 0
            for pile in piles:
                hours += (pile + speed - 1) // speed
            return hours

        while l <= r:
            m = l + (r - l) // 2

            if getHours(m) <= h:
                r = m - 1
            else:
                l = m + 1

        return l