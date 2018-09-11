# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 20:27:21 2018
最小路径和：
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
--------------------------------------------------------------------------------------
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
@author: Wan G.S
"""
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        for i in range(1, m):
            grid[i][0] += grid[i-1][0]

        for j in range(1, n):
            grid[0][j] += grid[0][j-1]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[-1][-1]
# =============================================================================
# class Solution:
#     def minPathSum(self, grid):
#         m, n = len(grid), len(grid[0])
#         dp = [[0] * n for _ in range(m)]
#
#         for i in range(m):
#             for j in range(n):
#                 if i == 0 and j == 0:
#                     dp[0][0] = grid[0][0]
#                 elif i == 0:
#                     dp[i][j] = dp[i][j-1] + grid[i][j]
#                 elif j == 0:
#                     dp[i][j] = dp[i-1][j] + grid[i][j]
#                 else:
#                     dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
#         return dp[-1][-1]
# =============================================================================




if __name__ == '__main__':
    print(Solution().minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))
