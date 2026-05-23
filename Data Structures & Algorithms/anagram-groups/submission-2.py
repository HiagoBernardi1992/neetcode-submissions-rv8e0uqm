class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]

        grouped = {}

        for s in strs:
            wArray = [0] * 26
            for c in s:
                index = ord(c) - ord("a")
                wArray[index] += 1
            key = "|".join(map(str, wArray))
            if key not in grouped:
                grouped[key] = [s]
            else: 
                grouped[key].append(s)
        
        return list(grouped.values())