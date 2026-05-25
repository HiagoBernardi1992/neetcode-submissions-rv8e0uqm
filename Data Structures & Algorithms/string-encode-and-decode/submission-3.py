class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(str(len(word)))
            res.append("|")
            res.append(word)
        return "".join(res)
        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "|":
                j += 1
            wordSize = int(s[i:j])
            startindex = j + 1
            endIndex = startindex + wordSize
            word = s[startindex: endIndex]
            res.append(word)
            i = endIndex

        return res

        
    
            
