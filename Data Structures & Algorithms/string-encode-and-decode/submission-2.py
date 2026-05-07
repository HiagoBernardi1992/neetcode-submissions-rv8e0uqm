class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded = encoded + str(len(word)) + "#"  + word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0 
        while i < len(s):
            j = i

            while s[j] != "#":
                j+=1
        
            wordSize = int(s[i:j])
            wordStart = j + 1
            wordEnd = wordStart + wordSize
            word = s[wordStart: wordEnd]
            decoded.append(word)
            i = wordEnd

        return decoded
    
            
