class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        i = 0

        while True:
            if i >= len(strs[0]):
                return ''.join(res)

            letter = strs[0][i]

            for s in strs:
                if i >= len(s) or s[i] != letter:
                    return ''.join(res)

            res.append(letter)
            i += 1

        