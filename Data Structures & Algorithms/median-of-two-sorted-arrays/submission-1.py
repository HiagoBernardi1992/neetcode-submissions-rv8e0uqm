class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        total = len(nums1) + len(nums2)
        half = total // 2

        l, r = 0, len(nums1) - 1

        while True:
            m1 = (l + r) // 2
            m2 = half - m1 - 2

            m1L = nums1[m1] if m1 >= 0 else float('-inf')
            m1R = nums1[m1 + 1] if m1 + 1 < len(nums1) else float('inf')

            m2L = nums2[m2] if m2 >= 0 else float('-inf')
            m2R = nums2[m2 + 1] if m2 + 1 < len(nums2) else float('inf')

            if m1L <= m2R and m2L <= m1R:

                if total % 2:
                    return min(m1R, m2R)

                return (max(m1L, m2L) + min(m1R, m2R)) / 2

            elif m1L > m2R:
                r = m1 - 1
            else:
                l = m1 + 1
