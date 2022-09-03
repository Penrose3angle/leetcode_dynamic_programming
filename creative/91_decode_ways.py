# https://leetcode.com/problems/decode-ways/
#
# .A message containing letters from A-Z can be encoded into numbers using the following mapping:
#
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
#
# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
#
# Given a string s containing only digits, return the number of ways to decode it.
#
# The test cases are generated so that the answer fits in a 32-bit integer.
#
#
#
# Example 1:
#
# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
# Example 2:
#
# Input: s = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
# Example 3:
#
# Input: s = "06"
# Output: 0
# Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06")..

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # leading zero case
        if s[0] == '0':
            return 0

        # track ways that index i can be in single/double state
        track_single = [0] * n
        # first digit always in single state
        track_single[0] = 1
        track_double = [0] * n

        for i in range(1, n):
            # if s[i] can be the second digit (can be in double state)
            if (int(s[i - 1: i + 1]) >= 10) and (int(s[i - 1: i + 1]) <= 26):
                # double from (single, nocut)
                track_double[i] = track_single[i - 1]
            # s[i] can be in single only if it's not 0
            if int(s[i]) != 0:
                # single either from (single, cut) or (double, cut)
                track_single[i] = track_single[i - 1] + track_double[i - 1]

        print(track_single)
        print(track_double)
        # count the number of ways the last digit can be in for each state
        return track_single[-1] + track_double[-1]
