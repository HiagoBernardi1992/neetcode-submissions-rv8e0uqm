class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count_palindromes = 0

        def isPalindrome(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.count_palindromes += 1
                l -= 1
                r += 1
                
        for i in range(len(s)):
            l, r = i, i
            isPalindrome(l, r)

            l, r = i, i + 1
            isPalindrome(l, r)

        return self.count_palindromes