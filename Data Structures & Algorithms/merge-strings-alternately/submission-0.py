class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)
        start = 0
        new = ""
        while start < l1 and start < l2:
            new += word1[start] + word2[start]
            start += 1

        if (l1 - 1) - start > 0:
            new += word1[start:]
        if (l2 - 1) - start > 0:
            new += word2[start:]

        return new