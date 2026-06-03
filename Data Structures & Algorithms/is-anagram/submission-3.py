class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return Counter(s) == Counter(t)
        countLetter = {}
        for letter in s:
            if letter in countLetter:
                countLetter[letter] += 1
            else:
                countLetter[letter] = 1

        for letter in t:
            if letter not in countLetter or countLetter[letter] <= 0:
                return False;
            if letter in countLetter:
                countLetter[letter] -= 1
        
        return True
            