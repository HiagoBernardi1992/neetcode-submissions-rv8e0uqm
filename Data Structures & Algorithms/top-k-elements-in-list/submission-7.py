class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countFreq = {}
        for n in nums:
            countFreq[n] = countFreq.get(n, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]
        for n, freq in countFreq.items():
            bucket[freq].append(n)

        res = []

        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)

                if len(res) == k:
                    return res