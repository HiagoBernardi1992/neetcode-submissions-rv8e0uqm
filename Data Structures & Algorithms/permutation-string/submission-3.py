class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count2 = {}
        count1 = Counter(s1)  
        l = 0
        for r in range(len(s2)):
            count2[s2[r]] = count2.get(s2[r], 0) + 1
            
            while (r - l + 1) > len(count1):
                count2[s2[l]] -= 1
                if count2[s2[l]] <= 0:
                    del count2[s2[l]]
                l += 1

            if count1 == count2:
                return True

        return False