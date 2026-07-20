class Solution:
    def reorganizeString(self, s: str) -> str:
        count_s = Counter(s)
        max_heap = []
        for key, val in count_s.items():
            heapq.heappush_max(max_heap, (val, key))
        res = ''
        while max_heap:
            val, key = heapq.heappop(max_heap);
            if len(res) > 0 and res[-1] == key:
                if not max_heap:
                    return ""
                secondVal, secondKey = heapq.heappop(max_heap);
                res += secondKey
                secondVal -= 1
                if secondVal > 0:
                    heapq.heappush_max(max_heap, (secondVal, secondKey))
            res += key
            val -= 1
            if val > 0:
                heapq.heappush_max(max_heap, (val, key))
        return res

