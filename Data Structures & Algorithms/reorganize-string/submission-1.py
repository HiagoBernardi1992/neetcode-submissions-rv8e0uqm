class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        max_heap = []
        for char, freq in count.items():
            heapq.heappush_max(max_heap, (freq, char))

        res = []
        prev = None

        while max_heap:
            freq, char = heapq.heappop_max(max_heap)

            res.append(char)
            freq -= 1

            # Recoloca o caractere usado na iteração anterior
            if prev:
                heapq.heappush_max(max_heap, prev)
                prev = None

            # Se ainda restam ocorrências, guarda para a próxima rodada
            if freq > 0:
                prev = (freq, char)

        # Se ainda sobrou um caractere, não foi possível reorganizar
        if prev:
            return ""

        return "".join(res)

