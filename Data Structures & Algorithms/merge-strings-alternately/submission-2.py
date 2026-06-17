class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)
        start = 0
        res = []
        
        while start < l1 and start < l2:
            res.append(word1[start])
            res.append(word2[start])
            start += 1

        res.append(word1[start:])
        res.append(word2[start:])

        return "".join(res)