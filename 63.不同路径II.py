# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 14:03:44 2018
不同路径2：
一个机器人位于一个 m x n 网格的左上角。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。
说明：m 和 n 的值均不超过 100。
----------------------------------------------------------------------------
输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
@author: Wan G.S
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                elif i == 0:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

# =============================================================================
# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid):

#         if not obstacleGrid or obstacleGrid[0][0] == 1:
#             return 0
#         m, n = len(obstacleGrid), len(obstacleGrid[0])
#         dp = [[0] * n for _ in range(m)]
#         dp[0][0] = 1
#         for i in range(m):
#             for j in range(n):
#                 if obstacleGrid[i][j] == 1:
#                     dp[i][j] = 0
#                 else:
#                     if i-1 >= 0:
#                         dp[i][j] += dp[i-1][j]
#                     if j-1 >= 0:
#                         dp[i][j] += dp[i][j-1]
#         return dp[-1][-1]
# =============================================================================


if __name__ == '__main__':
    print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))


