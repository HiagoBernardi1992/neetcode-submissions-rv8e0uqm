class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            if x != y:
                remaining = x - y
                heapq.heappush_max(stones, remaining)

        return 0 if len(stones) == 0 else stones[0]