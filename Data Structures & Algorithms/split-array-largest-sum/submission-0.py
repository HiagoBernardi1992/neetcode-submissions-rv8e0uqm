class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            sub_array = 0
            cur_sum = 0
            for n in nums:
               cur_sum += n
               if cur_sum > largest:
                sub_array += 1
                cur_sum = n
            return sub_array + 1 <= k
        
        l = max(nums)
        r = sum(nums)
        res = float('inf')
        while l <= r:
            m = l + (r - l) // 2
            if canSplit(m):
                res = m
                r = m - 1
            else:
                l = m + 1        

        return res

        