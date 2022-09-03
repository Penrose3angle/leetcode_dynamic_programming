# https://leetcode.com/problems/fibonacci-number/?envType=study-plan&id=dynamic-programming-i
# .The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
#
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).
#
#
#
# Example 1:
#
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:
#
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 3:
#
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3..


class Solution:
    def fib(self, n: int) -> int:
        memo = {0: 0,
                1: 1}

        def get_fib(j):
            if memo.get(j):
                return memo[j]
            if j <= 1:
                return j
            memo[j] = get_fib(j - 1) + get_fib(j - 2)
            return memo[j]

        return get_fib(n)
