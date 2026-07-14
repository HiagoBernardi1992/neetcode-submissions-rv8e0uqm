class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        mapS = set()
        for r in range(len(s)):
            while s[r] in mapS:
                mapS.remove(s[l])
                l += 1

            mapS.add(s[r])
            res = max(res, len(s[l : r + 1]))

        return res
                
                

        