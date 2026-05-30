class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        mostFreq = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            mostFreq = max(mostFreq, count[s[r]])

            while (r - l + 1) - mostFreq > k:
                count[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest

