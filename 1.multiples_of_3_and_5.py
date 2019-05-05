"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

class Solution:
  def sum_of_multiples(self, limit: int) -> int:
    res = 0

    for n in range(1, limit):
      if not n%3 or not n%5:
        res += n

    return res

solution = Solution()
solution.sum_of_multiples(1000)
# >>> 233168
