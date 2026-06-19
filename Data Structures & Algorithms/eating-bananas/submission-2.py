class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        def getHours(hour):
            quantity = 0
            for pile in piles:
                quantity += math.ceil(pile / hour)
            return quantity


        while l <= r:
            m = l + (r - l) // 2
            q = getHours(m)
            if q <= h:
                res = min(res, m)
                r = m - 1                
            else:
                l = m + 1                

        return res

            