class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return Counter(s) == Counter(t)
        if len(s) != len(t):
            return False

        countLetter = {}

        for letter in s:
            countLetter[letter] = countLetter.get(letter, 0) + 1

        for letter in t:
            if letter not in countLetter or countLetter[letter] <= 0:
                return False

            countLetter[letter] -= 1

        return True
            