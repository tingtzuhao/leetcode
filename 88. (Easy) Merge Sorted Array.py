class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        lastD = m + n - 1
        while p1 > -1 and p2 > -1:
            if nums1[p1] > nums2[p2]:
                nums1[lastD] = nums1[p1]
                p1 -= 1
            else:
                nums1[lastD] = nums2[p2]
                p2 -= 1
            lastD -= 1
        while p2 > -1:
            nums1[lastD] = nums2[p2]
            p2 -= 1
            lastD -= 1

# Pythonic
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         for i in range(n):
#             nums1[i+m] = nums2[i]
#         nums1.sort()