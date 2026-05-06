class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]

        groupedAnagrams = {}
        
        for word in strs:
            wordArray = [0] * 26
            for letter in word:
                index = ord(letter) - ord('a')
                wordArray[index] += 1
            key = '|'.join(map(str, wordArray))
            if key not in groupedAnagrams:
                groupedAnagrams[key] = [word]
            else:
                groupedAnagrams[key].append(word)

        return list(groupedAnagrams.values())

        
        