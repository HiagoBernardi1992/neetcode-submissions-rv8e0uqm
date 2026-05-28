class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCount = 0
        seen = set()
        i = 0
        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            maxCount = max(maxCount, len(s[i : j + 1]))

        return maxCount
