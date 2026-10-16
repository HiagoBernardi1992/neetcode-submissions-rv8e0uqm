class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        candidate = None
        while k > 0:
            candidate = heapq.heappop_max(nums)
            k -= 1
        return candidate
        