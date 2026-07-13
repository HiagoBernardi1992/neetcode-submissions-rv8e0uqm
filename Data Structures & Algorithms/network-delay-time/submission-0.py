class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}
        for node, nei, path in times:
            adj[node].append((path, nei))

        min_heap = []
        heapq.heappush(min_heap, (0, k))
        visited = set()
        res = 0

        while min_heap:
            path, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            res = max(res, path)

            for pathNei, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (path + pathNei, nei))

        return res if len(visited) == n else -1
