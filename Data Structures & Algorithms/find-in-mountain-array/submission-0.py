class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        mountainArr_length = mountainArr.length() - 1
        l, r = 0, mountainArr_length
        peak_idx = None
        while l <= r:
            m = l + (r - l) // 2
            val = mountainArr.get(m)
            next = mountainArr.get(m + 1)

            if val < next:
                l = m + 1
            elif val > next:
                r = m - 1

        peak_idx = l

        l, r = 0, peak_idx
        while l <= r:
            m = l + (r - l) // 2
            val = mountainArr.get(m)
            if val == target:
                return m
            elif val > target:
                r = m - 1
            else:
                l = m + 1

        l, r = peak_idx, mountainArr_length
        while l <= r:
            m = l + (r - l) // 2
            val = mountainArr.get(m)
            if val == target:
                return m
            elif val > target:
                l = m + 1                
            else:
                r = m - 1                

        return -1


        