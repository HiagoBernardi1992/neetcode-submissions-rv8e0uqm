class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n + 1)}
        for src, trg, time in times:
            adj[src].append([trg, time])

        min_heap = []
        heapq.heappush(min_heap, [0, k])
        res = 0
        visited = set()
        while min_heap:
            path, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            res = max(res, path)
            for nei, time in adj[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, [path + time, nei])
        return res if len(visited) == n else -1

        
        
