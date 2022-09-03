# https://leetcode.com/problems/word-break/
# .Given a string s and a dictionary of subsequences wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
#
#
#
# Example 1:
#
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:
#
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # track whether s[0: i] can be constructed with wordDict
        track = [0] * (n + 1)
        # s[0:0] is null, set it to true
        track[0] = 1

        for i in range(1, n + 1):
            # track[i] = True if there's a j<i s.t.
            # track[j] == 1 (i.e. s[0:j] can be constructed) AND
            # s[j:i] in wordDict
            for j in range(i):
                if track[j] == 1 and s[j:i] in wordDict:
                    track[i] = 1
                    break
            # no j track[i] = 0 as default

        print(track)
        return bool(track[-1])