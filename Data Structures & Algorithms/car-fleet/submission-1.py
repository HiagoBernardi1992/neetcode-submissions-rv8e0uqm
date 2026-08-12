class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        N = len(position)
        pairs = []
        for i in range(N):
            heapq.heappush_max(pairs, (position[i], speed[i]))

        stack = []
        while pairs:
            p, s = heapq.heappop_max(pairs)
            destination = (target - p) / s
            if not stack or destination > stack[-1]:
                stack.append(destination)

        return len(stack) 