class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        mapping = {}
        for r in range(len(s)):
            mapping[s[r]] = mapping.get(s[r], 0) + 1

            while mapping[s[r]] > 1:
                mapping[s[l]] -= 1
                if mapping[s[l]] == 0:
                    del mapping[s[l]]
                l += 1
            longest = max(longest, (r - l + 1))
        return longest