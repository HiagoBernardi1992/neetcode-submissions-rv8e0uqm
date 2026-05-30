class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        mostFreq = 0
        mapC = {}
        longestString = 0
        for r in range(len(s)):
            mapC[s[r]] = mapC.get(s[r], 0) + 1
            mostFreq = max(mostFreq, mapC[s[r]] )
            replacementsNeeded = len(s[l: r + 1]) - mostFreq
            if replacementsNeeded <= k:
                longestString = max(longestString, len(s[l: r + 1]))
            else:
                while replacementsNeeded > k:
                    mapC[s[l]] -= 1 
                    l += 1
                    replacementsNeeded = len(s[l: r + 1]) - mostFreq
                    

        return longestString

