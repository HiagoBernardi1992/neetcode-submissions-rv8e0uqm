class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = []

        for c in count.values():
            heapq.heappush_max(max_heap, c)

        time = 0
        q = deque()

        while max_heap or q:
            time += 1

            if q and q[0][0] == time:
                _, remaining = q.popleft()
                heapq.heappush_max(max_heap, remaining)

            if max_heap:
                remaining = heapq.heappop_max(max_heap) - 1
                if remaining > 0:
                    q.append((time + n + 1, remaining))            

        return time
