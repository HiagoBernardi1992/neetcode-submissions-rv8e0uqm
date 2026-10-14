class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        max_word = 0
        l = 0
        for r in range(len(s)):
            while s[r] in letters:
                letters.remove(s[l])
                l += 1
            letters.add(s[r])
            max_word = max(max_word, r - l + 1)
        return max_word