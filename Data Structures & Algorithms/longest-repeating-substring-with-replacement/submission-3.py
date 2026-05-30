class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        mostFreq = 0
        mapC = {}
        longestString = 0
        for r in range(len(s)):
            mapC[s[r]] = mapC.get(s[r], 0) + 1
            mostFreq = max(mostFreq, mapC[s[r]] )
            windowSize = r - l + 1
            replacementsNeeded = windowSize - mostFreq
            if replacementsNeeded <= k:
                longestString = max(longestString, windowSize)
            else:
                while replacementsNeeded > k:
                    mapC[s[l]] -= 1 
                    l += 1
                    windowSize = r - l + 1 
                    replacementsNeeded = windowSize - mostFreq
                    

        return longestString

