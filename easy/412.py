from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []

        for num in range(1, n + 1):
            item = str(num)

            if num % 3 == 0 and num % 5 == 0:
                item = 'FizzBuzz'
            elif num % 3 == 0:
                item = 'Fizz'
            elif num % 5 == 0:
                item = 'Buzz'

            output.append(item)

        return output
