from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first = m - 1
        second = n - 1

        for i in range(m + n - 1, -1, -1):
            if second < 0:
                break

            if first < 0:
                nums1[i] = nums2[second]
                second -= 1
                continue

            if nums2[second] > nums1[first]:
                nums1[i] = nums2[second]
                second -= 1
            else:
                nums1[i] = nums1[first]
                first -= 1
