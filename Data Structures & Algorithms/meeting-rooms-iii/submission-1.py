class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = list(range(n))
        heapq.heapify(available)

        used = []  # (endTime, room)
        count = [0] * n

        for start, end in meetings:
            duration = end - start

            while used and used[0][0] <= start:
                end_time, room = heapq.heappop(used)
                heapq.heappush(available, room)

            if not available:
                end_time, room = heapq.heappop(used)
                start = end_time
                end = start + duration
                heapq.heappush(available, room)

            room = heapq.heappop(available)
            heapq.heappush(used, (start + duration, room))
            count[room] += 1

        return count.index(max(count))
