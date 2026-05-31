class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        counT = Counter(t)

        window = {}
        have = 0
        need = len(counT) 

        res = [-1, -1]
        resLen = float("inf")

        l = 0
        for r in range(len(s)):
            caracter = s[r]
            window[caracter] = window.get(caracter, 0) + 1;

            if caracter in counT and counT[caracter] == window[caracter]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1

                if s[l] in counT and window[s[l]] < counT[s[l]]:
                    have -= 1
                
                l += 1

        l, r = res
        return s[l: r+1] if resLen != float("inf") else ""



        

                
