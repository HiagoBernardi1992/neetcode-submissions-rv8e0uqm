class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        for count, char in [[a, 'a'], [b, 'b'], [c, 'c']]:
            if count > 0:
                heapq.heappush_max(max_heap, [count, char])

        res = []

        while max_heap:
            count, char = heapq.heappop_max(max_heap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not max_heap:
                    break
                count2, char2  = heapq.heappop_max(max_heap)
                res.append(char2)
                if count2 > 1:
                    heapq.heappush_max(max_heap, [count2 - 1, char2])
            res.append(char)
            if count > 1:
                heapq.heappush_max(max_heap, [count - 1, char])

        return ''.join(res)