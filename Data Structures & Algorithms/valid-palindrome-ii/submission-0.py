class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        deleteChoice = 1
        while l <= r:
            if s[l] != s[r]:
                if deleteChoice < 1:
                    return False
                else:
                    deleteChoice -= 1
            l += 1
            r -= 1

        return True