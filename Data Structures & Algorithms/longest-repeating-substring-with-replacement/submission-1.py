class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        longestString = 0
        mostFreqChar = 0
        countLetters = {}        
        for right in range(len(s)):
            countLetters[s[right]] = countLetters.get(s[right], 0) + 1
            mostFreqChar = max(mostFreqChar, countLetters[s[right]])
            windowLength = right - left + 1
            replacementNumber = windowLength - mostFreqChar

            if replacementNumber <= k:
                longestString = max(longestString, windowLength)
            else:
                while replacementNumber > k:
                    countLetters[s[left]] = countLetters.get(s[left]) - 1
                    left += 1
                    windowLength = right - left + 1
                    replacementNumber = windowLength - mostFreqChar
        return longestString