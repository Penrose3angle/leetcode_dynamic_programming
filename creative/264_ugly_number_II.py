# https://leetcode.com/problems/ugly-number-ii/
# .An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
#
# Given an integer n, return the nth ugly number.
#
#
#
# Example 1:
#
# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
# Example 2:
#
# Input: n = 1
# Output: 1
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5..

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # uglies must be a multiple of 2,3,or 5 with another uglies
        multiples = [2, 3, 5]
        uglies = [1]
        # track position of idx_2, idx_3, idx_5
        idx_2, idx_3, idx_5 = 0, 0, 0
        track_idx = [0] * 3

        while len(uglies) < n:
            # keep only 3 candidates to find minimum numbers as next number
            # candidates = [uglies[idx_2]*2, uglies[idx_3]*3, uglies[idx_5]*5]
            candidates = [uglies[track_idx[i]] * multiples[i] for i in range(3)]
            # print(candidates)
            next_ugly = min(candidates)
            for i, cand in enumerate(candidates):
                if cand == next_ugly:
                    # shift index
                    track_idx[i] += 1
            uglies.append(next_ugly)
            # print(uglies, track_idx)

        # print(uglies)
        return uglies[-1]
