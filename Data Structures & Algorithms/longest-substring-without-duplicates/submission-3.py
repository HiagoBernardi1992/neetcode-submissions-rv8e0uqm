class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        characters = set()
        l = 0
        for r in range(len(s)):
            while s[r] in characters:
                characters.remove(s[l])
                l += 1
            characters.add(s[r])
            res = max(res, (r - l) + 1)

        return res