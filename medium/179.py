from typing import List


class StrComporator(str):
    def __lt__(self, value: str):
        return self + value > value + self


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = map(str, nums)
        sorted_nums = sorted(str_nums, key=StrComporator)

        if sorted_nums[0] == '0':
            return '0'

        return ''.join(sorted_nums)
