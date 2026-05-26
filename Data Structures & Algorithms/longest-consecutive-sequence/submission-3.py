class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxFreq = 0
        for n in numsSet:
            if n - 1 not in numsSet:
                counter = 1
                while n + counter in numsSet:
                    counter += 1
                maxFreq = max(maxFreq, counter)

        return maxFreq
        