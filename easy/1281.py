class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        total = 0
        product = 1

        while n > 0:
            last_digit = n % 10

            total += last_digit
            product *= last_digit

            n //= 10

        return product - total
