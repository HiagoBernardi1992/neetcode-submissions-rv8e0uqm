# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start, end = 0, n
        while True:
            m = start + (end - start) // 2
            result = guess(m)
            if result == 0:
                return m
            elif result == - 1:
                end = m - 1
            else:
                start = m + 1