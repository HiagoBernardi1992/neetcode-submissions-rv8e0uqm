class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        maxFreq = 0
        for num in setNums:            
            if (num - 1) not in setNums:
                length = 0
                while (num + length) in setNums:
                    length += 1
                maxFreq = max(maxFreq, length)
        return maxFreq
        