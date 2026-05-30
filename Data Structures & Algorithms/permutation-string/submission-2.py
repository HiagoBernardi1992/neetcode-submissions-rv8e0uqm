class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)

        if len1 > len2:
            return False

        count1 = Counter(s1)
        window = Counter(s2[:len1])

        if window == count1:
            return True

        l = 0
        for r in range(len1, len2):
            window[s2[r]] += 1          
            window[s2[l]] -= 1          

            if window[s2[l]] == 0:
                del window[s2[l]]

            l += 1

            if window == count1:
                return True

        return False
        