from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        digits[i] += 1

        while True:
            if digits[i] < 10:
                break

            digits[i] = 0

            if i == 0:
                digits.insert(0, 1)
                break

            digits[i - 1] += 1
            i -= 1

        return digits
