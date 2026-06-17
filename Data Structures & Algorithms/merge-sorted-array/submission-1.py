class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        start1 = m - 1
        start2 = n - 1
        i = len(nums1) -1

        while start1 >= 0 and start2 >= 0:
            if nums1[start1] >= nums2[start2]:
                nums1[i] = nums1[start1]
                start1 -= 1
            else:
                nums1[i] = nums2[start2]
                start2 -= 1
            i -= 1

        while start2 >= 0:
            nums1[i] = nums2[start2]
            start2 -= 1
            i -= 1







        