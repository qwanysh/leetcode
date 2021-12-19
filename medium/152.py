from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = max(nums)
        curr_min = 1
        curr_max = 1

        for num in nums:
            temp = curr_min * num
            curr_min = min(num, curr_min * num, curr_max * num)
            curr_max = max(num, temp, curr_max * num)

            max_product = max(max_product, curr_max)

        return max_product
