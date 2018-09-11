# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 16:51:25 2018
最长回文子串:
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。
---------------------------------------------------------------------------
示例 1：
输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"
@author: Wan G.S
"""
# =============================================================================
# class Solution:
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         if not s:
#             return ''
#         start = maxLength = 0
#         for i in range(len(s)):
#             for j in (0, 1):
#                 _start, _maxLength = self.expandAroundCenter(s, i-j, i+1)
#                 if _maxLength > maxLength:
#                     start, maxLength = _start, _maxLength
#         return s[start:start+maxLength]
#
#     def expandAroundCenter(self, s, l, r):
#         while l >= 0 and r < len(s) and s[l] == s[r]:
#             l -= 1
#             r += 1
#         return l+1, r-l-1
# =============================================================================

# =============================================================================
# class Solution:
#     def longestPalindrome(self, s):
#         if not s:
#             return ''
#         start = end = 0
#         for i in range(len(s)):
#             len1 = self.expandAroundCenter(s, i, i+1)
#             len2 = self.expandAroundCenter(s, i-1, i+1)
#             length = max(len1, len2)
#             if length > (end-start):
#                 start = i - (length-1)//2
#                 end = i + (length)//2
#         return s[start:end + 1]
#
#     def expandAroundCenter(self, s, l, r):
#         while l >= 0 and r <len(s) and s[l] == s[r]:
#             l -= 1
#             r += 1
#         return r - l - 1
# =============================================================================

class Solution:
    def longestPalindrome(self, s):
        """动态规划法"""
        dp = [[0] * len(s) for _ in range(len(s))]
        start, maxLength = 0, 1

        for i in range(len(s)):
            dp[i][i] = 1
            if i < len(s)-1 and s[i] == s[i+1]:
                dp[i][i+1] = 1
                start, maxLength = i, 2

        for j in range(len(s)):
            for i in range(j-1):
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = 1
                    if maxLength < j - i + 1:
                        start, maxLength = i, j-i+1

        return s[start: start+maxLength]


if __name__ == '__main__':
    print(Solution().longestPalindrome('babad'))

