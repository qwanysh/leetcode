from typing import List
from math import inf


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = -inf
        second_max = -inf
        third_max = -inf

        for num in set(nums):
            if num > first_max:
                third_max = second_max
                second_max = first_max
                first_max = num
            elif num > second_max:
                third_max = second_max
                second_max = num
            elif num > third_max:
                third_max = num

        if third_max == -inf:
            return first_max

        return third_max
