class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        count = 0
        for letter in text1:
            if letter in text2:
                count += 1

        return count
        