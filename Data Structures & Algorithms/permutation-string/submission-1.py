class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0        
        for r in range(len(s1) - 1, len(s2)):
            if Counter(s1) == Counter(s2[l: r + 1]):
                return True
            else:
                l += 1
        
        return False
        