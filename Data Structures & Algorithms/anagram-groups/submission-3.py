class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]

        groups = {}
        for word in strs:
            word_array = [0] * 26
            for char in word:
                index = ord(char) - ord("a")
                word_array[index] += 1
            key = "|".join(map(str, word_array))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        return list(groups.values())
