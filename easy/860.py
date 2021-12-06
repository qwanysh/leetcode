from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0

        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if not fives:
                    return False

                fives -= 1
                tens += 1
            elif bill == 20:
                if tens and fives:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False

        return True
