class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        mostFreq = 0
        characters = {}
        for r in range(len(s)):
            characters[s[r]] = characters.get(s[r], 0) + 1
            mostFreq = max(mostFreq, characters[s[r]])

            while (r - l + 1) - mostFreq > k:
                characters[s[l]] -= 1
                l += 1

            res = max(res, (r - l + 1))

        return res

