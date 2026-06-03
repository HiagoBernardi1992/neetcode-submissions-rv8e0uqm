class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #faço o mapeamento de todos os caracteres de todas as words sem repetição
        adj = {c: set() for word in words for c in word}

        #percorro as words comparando dois em dois
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]: #se a primeira palavra for maior que a segunda, e o prefixo da primeira for igual se segunda
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

            visit = {}
            res = []

            def dfs(c):
                if c in visit:
                    return visit[c]
                visit[c] = True
                for nei in adj[c]:
                    if dfs(nei):
                        return True
                visit[c] = False
                res.append(c)

        for c in adj:
            if dfs(c):
                return ""            
        res.reverse()
        return "".join(res)